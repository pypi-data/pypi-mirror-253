import logging
from abc import ABC, abstractmethod
import numpy as np

from autoconf import conf

from autofit import exc
from autofit.mapper.prior_model.abstract import AbstractPriorModel
from autofit.non_linear.samples import Samples
from autofit.text import text_util


class Placeholder:
    def __getattr__(self, item):
        """
        Placeholders return None to represent the missing result's value
        """
        return None

    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        pass

    def __gt__(self, other):
        return False

    def __lt__(self, other):
        return True

    @property
    def samples(self):
        return self

    @property
    def log_likelihood(self):
        return -np.inf

    def summary(self):
        return self


class AbstractResult(ABC):
    @property
    def sigma(self):
        return self.samples.sigma

    @property
    @abstractmethod
    def samples(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    def info(self) -> str:
        return text_util.result_info_from(
            samples=self.samples,
        )

    def __gt__(self, other):
        """
        Results are sorted by their associated log_likelihood.

        Placeholders are always low.
        """
        if isinstance(other, Placeholder):
            return True
        return self.log_likelihood > other.log_likelihood

    def __lt__(self, other):
        """
        Results are sorted by their associated log_likelihood.

        Placeholders are always low.
        """
        if isinstance(other, Placeholder):
            return False
        return self.log_likelihood < other.log_likelihood

    @property
    def log_likelihood(self):
        return max(self.samples.log_likelihood_list)

    @property
    def instance(self):
        try:
            return self.samples.instance
        except AttributeError as e:
            logging.warning(e)
            return None

    @property
    def max_log_likelihood_instance(self):
        return self.instance

    def model_absolute(self, a: float) -> AbstractPriorModel:
        """
        Returns a model where every free parameter is a `GaussianPrior` with `mean` the previous result's
        inferred maximum log likelihood parameter values and `sigma` the input absolute value `a`.

        For example, a previous result may infer a parameter to have a maximum log likelihood value of 2.

        If this result is used for search chaining, `model_absolute(a=0.1)` will assign this free parameter
        `GaussianPrior(mean=2.0, sigma=0.1)` in the new model, where `sigma` is linked to the input `a`.

        Parameters
        ----------
        a
            The absolute width of gaussian priors

        Returns
        -------
        A model mapper created by taking results from this search and creating priors with the defined absolute
        width.
        """
        return self.samples.model_absolute(a)

    def model_relative(self, r: float) -> AbstractPriorModel:
        """
        Returns a model where every free parameter is a `GaussianPrior` with `mean` the previous result's
        inferred maximum log likelihood parameter values and `sigma` a relative value from the result `r`.

        For example, a previous result may infer a parameter to have a maximum log likelihood value of 2 and
        an error at the input `sigma` of 0.5.

        If this result is used for search chaining, `model_relative(r=0.1)` will assign this free parameter
        `GaussianPrior(mean=2.0, sigma=0.5*0.1)` in the new model, where `sigma` is the inferred error times `r`.

        Parameters
        ----------
        r
            The relative width of gaussian priors

        Returns
        -------
        A model mapper created by taking results from this search and creating priors with the defined relative
        width.
        """
        return self.samples.model_relative(r)

    def model_bounded(self, b: float) -> AbstractPriorModel:
        """
        Returns a model where every free parameter is a `UniformPrior` with `lower_limit` and `upper_limit the previous
        result's inferred maximum log likelihood parameter values minus and plus the bound `b`.

        For example, a previous result may infer a parameter to have a maximum log likelihood value of 2.

        If this result is used for search chaining, `model_bound(b=0.1)` will assign this free parameter
        `UniformPrior(lower_limit=1.9, upper_limit=2.1)` in the new model.

        Parameters
        ----------
        b
            The size of the bounds of the uniform prior

        Returns
        -------
        A model mapper created by taking results from this search and creating priors with the defined bounded
        uniform priors.
        """
        return self.samples.model_bounded(b)

class Result(AbstractResult):
    def __init__(self, samples: Samples):
        """
        The result of a non-linear search, which includes:

        - The samples of the non-linear search (E.g. MCMC chains, nested sampling samples) which are used to compute
        the maximum likelihood model, posteriors and other properties.

        - The model used to fit the data, which uses the samples to create specific instances of the model (e.g.
        an instance of the maximum log likelihood model).

        - The non-linear search used to perform the model fit.

        Parameters
        ----------
        samples
            The samples of the non-linear search
        """
        self._samples = samples

        self.__model = None

        self.child_results = None

    def dict(self) -> dict:
        """
        Human-readable dictionary representation of the results
        """
        return {
            "max_log_likelihood": self.samples.max_log_likelihood_sample.model_dict(),
        }

    @property
    def samples(self):
        return self._samples

    @property
    def projected_model(self) -> AbstractPriorModel:
        """
        Create a new model with the same structure as the previous model,
        replacing each prior with a new prior created by calculating sufficient
        statistics from samples and corresponding weights for that prior.
        """
        weights = self.samples.weight_list
        arguments = {
            prior: prior.project(
                samples=np.array(self.samples.values_for_path(path)),
                weights=weights,
            )
            for path, prior in self.samples.model.path_priors_tuples
        }
        return self.samples.model.mapper_from_prior_arguments(arguments)

    @property
    def model(self):
        use_errors = conf.instance["general"]["prior_passer"]["use_errors"]
        use_widths = conf.instance["general"]["prior_passer"]["use_widths"]

        if self.__model is None:
            tuples = self.samples.gaussian_priors_at_sigma(sigma=self.sigma)
            self.__model = self.samples.model.mapper_from_gaussian_tuples(
                tuples, use_errors=use_errors, use_widths=use_widths
            )
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def __str__(self):
        return "Analysis Result:\n{}".format(
            "\n".join(
                ["{}: {}".format(key, value) for key, value in self.__dict__.items()]
            )
        )

    def __getitem__(self, item):
        return self.child_results[item]

    def __iter__(self):
        return iter(self.child_results)

    def __len__(self):
        return len(self.child_results)


class ResultsCollection:
    def __init__(self, result_list=None):
        """
        A collection of results from previous searches. Results can be obtained using an index or the name of the search
        from whence they came.
        """
        self.__result_list = []
        self.__result_dict = {}

        if result_list is not None:
            for result in result_list:
                self.add(name="", result=result)

    def copy(self):
        collection = ResultsCollection()
        collection.__result_dict = self.__result_dict
        collection.__result_list = self.__result_list
        return collection

    @property
    def reversed(self):
        return reversed(self.__result_list)

    @property
    def last(self):
        """
        The result of the last search
        """
        if len(self.__result_list) > 0:
            return self.__result_list[-1]
        return None

    @property
    def first(self):
        """
        The result of the first search
        """
        if len(self.__result_list) > 0:
            return self.__result_list[0]
        return None

    def add(self, name, result):
        """
        Add the result of a search.

        Parameters
        ----------
        name: str
            The name of the search
        result
            The result of that search
        """
        try:
            self.__result_list[self.__result_list.index(result)] = result
        except ValueError:
            self.__result_list.append(result)
        self.__result_dict[name] = result

    def __getitem__(self, item):
        """
        Get the result of a previous search by index

        Parameters
        ----------
        item: int
            The index of the result

        Returns
        -------
        result: Result
            The result of a previous search
        """
        return self.__result_list[item]

    def __len__(self):
        return len(self.__result_list)

    def from_name(self, name):
        """
        Returns the result of a previous search by its name

        Parameters
        ----------
        name: str
            The name of a previous search

        Returns
        -------
        result: Result
            The result of that search

        Raises
        ------
        exc.PipelineException
            If no search with the expected result is found
        """
        try:
            return self.__result_dict[name]
        except KeyError:
            raise exc.PipelineException(
                "No previous search named {} found in results ({})".format(
                    name, ", ".join(self.__result_dict.keys())
                )
            )

    def __contains__(self, item):
        return item in self.__result_dict
