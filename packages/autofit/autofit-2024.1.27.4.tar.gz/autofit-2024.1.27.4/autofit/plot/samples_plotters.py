import matplotlib.pyplot as plt
from functools import wraps
import logging
import os

from autofit.plot.output import Output

logger = logging.getLogger(__name__)

def skip_plot_in_test_mode(func):
    """
    Skips visualization plots of non-linear searches if test mode is on.

    Parameters
    ----------
    func
        A function which plots a result of a non-linear search.

    Returns
    -------
        A function that plots a visual, or None if test mode is on.
    """

    @wraps(func)
    def wrapper(
        obj: object,
        *args,
        **kwargs
    ):
        """
        Skips visualization plots of non-linear searches if test mode is on.

        Parameters
        ----------
        obj
            An plotter object which performs visualization of a non-linear search.

        Returns
        -------
            A function that plots a visual, or None if test mode is on.
        """

        if os.environ.get("PYAUTOFIT_TEST_MODE") == "1":
            return

        return func(obj, *args, **kwargs)

    return wrapper



class SamplesPlotter:
    def __init__(
            self, 
            samples,
            output : Output = Output()
    ):

        self.samples = samples
        self.output = output

    @property
    def model(self):
        return self.samples.model

    def close(self):
        if plt.fignum_exists(num=1):
            plt.close()

    def log_plot_exception(self, plot_name : str):
        """
        Plotting the results of a ``dynesty`` model-fit before they have converged on an
        accurate estimate of the posterior can lead the ``dynesty`` plotting routines
        to raise a ``ValueError``.

        This exception is caught in each of the plotting methods below, and this
        function is used to log the behaviour.

        Parameters
        ----------
        plot_name
            The name of the ``dynesty`` plot which raised a ``ValueError``
        """

        logger.info(
            f"{self.__class__.__name__} unable to produce {plot_name} visual: posterior estimate therefore"
            "not yet sufficient for this model-fit is not yet robust enough to do this. Visual"
            "should be produced in later update, once posterior estimate is updated."
        )

class MCMCPlotter(SamplesPlotter):

    def _plot_trajectories(self, samples, log_posterior_list, **kwargs):

        fig, axes = plt.subplots(self.samples.model.prior_count, figsize=(10, 7))

        for i in range(self.samples.model.prior_count):

            for walker_index in range(log_posterior_list.shape[1]):

                ax = axes[i]
                ax.plot(samples[:, walker_index, i], log_posterior_list[:, walker_index], alpha=0.3)

            ax.set_ylabel("Log Likelihood")
            ax.set_xlabel(self.model.parameter_labels_with_superscripts_latex[i])

        self.output.to_figure(structure=None, auto_filename="tracjectories")
        self.close()

    def _plot_likelihood_series(self, log_posterior_list, **kwargs):

        fig, axes = plt.subplots(1, figsize=(10, 7))

        for walker_index in range(log_posterior_list.shape[1]):

            axes.plot(log_posterior_list[:, walker_index], alpha=0.3)

        axes.set_ylabel("Log Likelihood")
        axes.set_xlabel("step number")

        self.output.to_figure(structure=None, auto_filename="likelihood_series")
        self.close()

    def _plot_time_series(self, samples, **kwargs):

        fig, axes = plt.subplots(self.samples.model.prior_count, figsize=(10, 7), sharex=True)

        for i in range(self.samples.model.prior_count):
            ax = axes[i]
            ax.plot(samples[:, :, i], alpha=0.3)
            ax.set_ylabel(self.model.parameter_labels_with_superscripts_latex[i])

        axes[-1].set_xlabel("step number")

        self.output.to_figure(structure=None, auto_filename="time_series")
        self.close()