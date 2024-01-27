from .XsocsPlot2D import XsocsPlot2D


class PlotGrabber(XsocsPlot2D):
    """
    XsocsPlot2D that can be converted to a pixmap.
    """

    def __init__(self, *args, **kwargs):
        super(PlotGrabber, self).__init__(*args, **kwargs)
        self._backend._enableAxis("left", False)
        self._backend._enableAxis("right", False)
        self._backend.ax.get_xaxis().set_visible(False)
        self._backend.ax.set_xmargin(0)
        self._backend.ax.set_ymargin(0)
        self.setActiveCurveHandling(False)
        self.setKeepDataAspectRatio(True)
        self.setDataMargins(0, 0, 0, 0)
        self.setCollaspibleMenuVisible(False)
        self.setPointWidgetVisible(False)

    def toPixmap(self):
        """
        Returns a pixmap of the widget.
        :return:
        """
        return self.grab()
