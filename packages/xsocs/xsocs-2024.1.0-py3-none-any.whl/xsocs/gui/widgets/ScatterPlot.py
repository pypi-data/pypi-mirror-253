"""Plot widget used to display scatter plot in XSocs"""

import logging

from silx.gui import qt
from silx.gui.plot import PlotWidget
from silx.gui.plot import tools, actions, PlotToolButtons
from silx.gui.plot.ColorBar import ColorBarWidget

from ..widgets.PointWidget import PointWidget


_logger = logging.getLogger(__name__)


class ScatterPlot(PlotWidget):
    """PlotWidget displaying a scatter plot"""

    sigSelectedIndexChanged = qt.Signal()
    """Signal emitted when the selected point has changed"""

    def __init__(self, parent=None, backend="mpl"):
        super(ScatterPlot, self).__init__(parent, backend)

        self.__selectedIndex = None

        # Set defaults
        self.setDataMargins(0.1, 0.1, 0.1, 0.1)
        self.setKeepDataAspectRatio(True)
        self.getDefaultColormap().setName("jet")

        # Add toolbars
        self.addToolBar(tools.InteractiveModeToolBar(parent=self, plot=self))

        toolbar = qt.QToolBar()
        toolbar.addAction(actions.control.ResetZoomAction(parent=self, plot=self))
        toolbar.addWidget(PlotToolButtons.AspectToolButton(parent=self, plot=self))
        toolbar.addAction(actions.control.ColormapAction(parent=self, plot=self))
        toolbar.addWidget(PlotToolButtons.SymbolToolButton(parent=self, plot=self))
        self.addToolBar(toolbar)

        self.addToolBar(tools.OutputToolBar(parent=self, plot=self))

        # Add Colorbar
        colorBar = ColorBarWidget(parent=self, plot=self)

        # Make ColorBarWidget background white by changing its palette
        colorBar.setAutoFillBackground(True)
        palette = colorBar.palette()
        palette.setColor(qt.QPalette.Background, qt.Qt.white)
        palette.setColor(qt.QPalette.Window, qt.Qt.white)
        colorBar.setPalette(palette)

        # Add colorbar to central widget
        gridLayout = qt.QGridLayout()
        gridLayout.setSpacing(0)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.addWidget(self.getWidgetHandle(), 0, 0)
        gridLayout.addWidget(colorBar, 0, 1)
        gridLayout.setRowStretch(0, 1)
        gridLayout.setColumnStretch(0, 1)
        centralWidget = qt.QWidget(self)
        centralWidget.setLayout(gridLayout)
        self.setCentralWidget(centralWidget)

        # Add mouse/selected point position info
        widget = qt.QWidget()
        layout = qt.QFormLayout(widget)
        layout.setFormAlignment(qt.Qt.AlignLeft)
        layout.setFieldGrowthPolicy(qt.QFormLayout.FieldsStayAtSizeHint)
        layout.setContentsMargins(0, 0, 0, 0)

        self.__mousePointWidget = PointWidget()
        self.__mousePointWidget.setFrameStyle(qt.QFrame.Box)
        layout.addRow("Mouse", self.__mousePointWidget)

        self.__selectedPointWidget = PointWidget()
        self.__selectedPointWidget.setFrameStyle(qt.QFrame.Box)
        layout.addRow("Selected", self.__selectedPointWidget)

        dock = qt.QDockWidget("Position Information")
        dock.setFeatures(qt.QDockWidget.NoDockWidgetFeatures)
        dock.setWidget(widget)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, dock)

        # Connect to mouse events
        self.sigPlotSignal.connect(self.__plotWidgetEvents)
        self.sigContentChanged.connect(self.__plotWidgetContentChanged)

    def __plotWidgetEvents(self, event):
        """Handle PlotWidget mouse events"""
        if event["event"] == "mouseClicked":  # Handle selection
            self.selectPoint(event["x"], event["y"])

        if event["event"] == "mouseMoved":  # Display mouse coordinates
            self.__mousePointWidget.setPoint(event["x"], event["y"])

    def __plotWidgetContentChanged(self, action, kind, legend):
        """Handle PlotWidget content changed"""
        if kind == "scatter":
            # Refresh selection
            self.setSelectedIndex(self.getSelectedIndex())

    def selectPoint(self, x, y):
        """Select closest scatter plot point and draws a crosshair on it.

        :param float x: X data coordinate
        :param float y: Y data coordinate
        """
        scatter = self.getScatter()
        if scatter is None:
            self.setSelectedIndex(None)
            return

        xData = scatter.getXData(copy=False)
        yData = scatter.getYData(copy=False)

        if len(xData) == 0:
            self.setSelectedIndex(None)
            return

        index = ((xData - x) ** 2 + (yData - y) ** 2).argmin()
        self.setSelectedIndex(index)

    def setSelectedIndex(self, index):
        """Select a point in the scatter plot by its index

        :param Union[None,int] index:
            The index of the selected point in the scatter plot
        """
        if index != self.__selectedIndex:
            if index is not None:
                scatter = self.getScatter()
                if scatter is None:
                    _logger.warning("Cannot select index without a scatter plot")
                    index = None
                else:
                    if index >= len(scatter.getXData(copy=False)):
                        _logger.warning("Selected index is out of range")
                        index = None

            self.__selectedIndex = index

            if index is not None:
                x, y = self.getSelectedPosition()
                self.addXMarker(x, legend="__selected_x_marker__", color="pink")
                self.addYMarker(y, legend="__selected_y_marker__", color="pink")

                self.__selectedPointWidget.setPoint(x, y)
            else:
                self.remove(legend="__selected_x_marker__", kind="marker")
                self.remove(legend="__selected_y_marker__", kind="marker")
                self.__selectedPointWidget.setPoint(x=None, y=None)

            self.sigSelectedIndexChanged.emit()

    def getSelectedIndex(self):
        """Returns selected point index in the scatter plot or None

        :rtype: Union[None,int]
        """
        if self.__selectedIndex is None:
            return None

        scatter = self.getScatter()
        if scatter is None or self.__selectedIndex >= len(scatter.getXData(copy=False)):
            # Selected index is not sync with plot content
            # This should not happen
            self.setSelectedIndex(None)
            return None

        return self.__selectedIndex

    def getSelectedPosition(self):
        """Returns the position of the selected point

        :return: (x, y) position in data coordinates or
            None if there is no selection
        :rtype: Union[None,List[float]]
        """
        index = self.getSelectedIndex()
        scatter = self.getScatter()
        if index is None or scatter is None:
            return None

        x = scatter.getXData(copy=False)[index]
        y = scatter.getYData(copy=False)[index]
        return x, y
