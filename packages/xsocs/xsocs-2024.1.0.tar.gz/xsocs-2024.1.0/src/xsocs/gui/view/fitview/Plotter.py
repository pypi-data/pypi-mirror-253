import numpy

from ....util import gaussian


class Plotter(object):
    """Base class for fit result plotting"""

    def plotFit(self, plot, x, params, background):
        """Update a plot to display fit/COM results

        :param plot: PlotWidget to update
        :param numpy.ndarray x: X values
        :param List[float] params: Parameters of the fit/COM
        :param Union[None,numpy.ndarray] background:
           The background estimation or None if no background
        """
        raise NotImplementedError("Not implemented")

    def getPlotTitle(self):
        """Returns the title to use for the plot

        :rtype: str
        """
        raise NotImplementedError("Not implemented")


class GaussianPlotter(Plotter):
    """Plot gaussian fit results"""

    def plotFit(self, plot, x, params, background):
        for peakName, peak in params.items():
            height = peak.get("Area")
            position = peak.get("Center")
            width = peak.get("Sigma")

            gaussian_params = [height, position, width]

            if numpy.all(numpy.isfinite(gaussian_params)):
                fitted = gaussian(x, *gaussian_params)
                if background is not None:
                    fitted += background
                plot.addCurve(x, fitted, legend="{0}".format(peakName), color="red")

    def getPlotTitle(self):
        return "Gaussian"


class CentroidPlotter(Plotter):
    """Plot center-of-mass/Max results"""

    def plotFit(self, plot, x, params, background):
        for peakName, peak in params.items():
            center = peak.get("COM")
            xmax = peak.get("Pos_max")

            if numpy.isfinite(center):
                plot.addXMarker(center, legend="center of mass", text="com")
                plot.addXMarker(
                    xmax, legend="maximum position", text="max", color="gray"
                )

    def getPlotTitle(self):
        return "Center Of Mass"
