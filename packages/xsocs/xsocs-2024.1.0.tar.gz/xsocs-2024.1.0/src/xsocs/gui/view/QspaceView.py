import logging
import os

import numpy as np

from silx.utils.weakref import WeakMethodProxy
from silx.gui import qt as Qt
from silx.gui.plot import actions, items, PlotToolButtons, PlotWidget
from silx.gui.icons import getQIcon
from silx.gui.plot.StackView import StackView
from silx.math.combo import min_max

from ... import config
from ...util import bin_centers_to_range_step
from ..widgets.XsocsPlot2D import XsocsPlot2D
from ..process.FitWidget import FitWidget

from ..Utils import nextFileName


_logger = logging.getLogger(__name__)


try:
    from silx.gui.plot3d.ScalarFieldView import ScalarFieldView
    from silx.gui.plot3d.SFViewParamTree import TreeView as SFViewParamTree
except ImportError:
    _logger.warning("Cannot import 3D visualization widgets: 3D view disabled")
    ScalarFieldView = None
    SFViewParamTree = None


def _useOpenGL():
    """Returns True if OpenGL is available and enabled

    :rtype: bool
    """
    return ScalarFieldView is not None and config.USE_OPENGL


class PlotIntensityMap(XsocsPlot2D):
    """Plot intensities as a scatter plot

    :param parent: QWidget's parent
    """

    def __init__(self, parent=None, **kwargs):
        super(PlotIntensityMap, self).__init__(parent=parent, **kwargs)
        self.setMinimumSize(150, 150)

        self.setDataMargins(0.2, 0.2, 0.2, 0.2)
        self.setShowMousePosition(True)
        self.setShowSelectedCoordinates(True)

    def sizeHint(self):
        return Qt.QSize(200, 200)


class ROIPlotIntensityMap(PlotIntensityMap):
    """Plot ROI intensities with an update button to compute it in a thread"""

    _DEFAULT_TOOLTIP = "Intensity Map: sum of the whole QSpace"
    _ROI_TOOLTIP = (
        "ROI Intensity Map: sum of the Region of Interest:\n"
        "{dim0} = [{d0_min}, {d0_max}]\n"
        "{dim1} = [{d1_min}, {d1_max}]\n"
        "{dim2} = [{d2_min}, {d2_max}]"
    )

    def __init__(self, parent, qspaceH5):
        # TODO
        self.__roiSlices = None  # qz, qy, qx ROI slices or None
        self.__roiQRange = None  # qx, qy, qz ROI range in Q space or None
        self.__qspaceH5 = qspaceH5
        super(ROIPlotIntensityMap, self).__init__(parent)
        self.setGraphTitle("ROI Intensity Map")
        self.setToolTip(self._DEFAULT_TOOLTIP)

        self.__updateButton = Qt.QPushButton(self)
        self.__updateButton.setText("Update")
        self.__updateButton.setIcon(getQIcon("view-refresh"))
        self.__updateButton.setToolTip(
            "Compute the intensity map for" " the current ROI"
        )
        self.__updateButton.clicked.connect(self.__updateClicked)

        toolBar = Qt.QToolBar("ROI Intensity Update", parent=self)
        toolBar.addWidget(self.__updateButton)
        self.addToolBar(Qt.Qt.BottomToolBarArea, toolBar)

    def roiChanged(self, selectedRegion):
        """To call when ROI has changed"""
        if selectedRegion is not None:
            self.__roiSlices = selectedRegion.getArraySlices()
            self.__roiQRange = selectedRegion.getDataRange()
        else:
            self.__roiSlices = None
            self.__roiQRange = None
        self.__updateButton.setEnabled(True)

    def __updateClicked(self, checked=False):
        """Handle button clicked"""
        if self.__roiSlices is None:
            # No ROI, use sum for the whole QSpace
            with self.__qspaceH5 as qspaceH5:
                intensities = np.array(qspaceH5.qspace_sum, copy=True)

        else:
            # Compute sum for QSpace ROI
            # This is performed as a co-routine using a QTimer

            # Show dialog
            dialog = Qt.QDialog(self)
            dialog.setWindowTitle("ROI Intensity Map")
            layout = Qt.QVBoxLayout(dialog)
            progress = Qt.QProgressBar()
            layout.addWidget(progress)

            btnBox = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Abort)
            btnBox.rejected.connect(dialog.reject)
            layout.addWidget(btnBox)

            dialog.setModal(True)
            dialog.show()

            qapp = Qt.QApplication.instance()
            with self.__qspaceH5 as qspaceH5:
                intensities = np.zeros((qspaceH5.qspace_sum.size,), dtype=np.float64)
                progress.setRange(0, qspaceH5.qspace_sum.size - 1)

                zslice, yslice, xslice = self.__roiSlices

                for index in range(qspaceH5.qspace_sum.size):
                    qspace = qspaceH5.qspace_slice(index)
                    intensities[index] = np.sum(qspace[xslice, yslice, zslice])
                    progress.setValue(index)
                    qapp.processEvents()
                    if not dialog.isVisible():
                        break  # It has been rejected by the abort button
                else:
                    dialog.accept()

            if dialog.result() == Qt.QDialog.Rejected:
                return  # Aborted, stop here

            intensities = np.array(intensities, copy=True)

        # Reset plot
        self.__updateButton.setEnabled(False)
        self.remove(kind="curve")

        # Update plot
        with self.__qspaceH5 as qsp:
            sampleX = qsp.sample_x
            sampleY = qsp.sample_y
            self.setPlotData(sampleX, sampleY, intensities)
            axis_names = qsp.qspace_dimension_names

        if self.__roiQRange is None:
            self.setToolTip(self._DEFAULT_TOOLTIP)
        else:
            self.setToolTip(
                self._ROI_TOOLTIP.format(
                    dim0=axis_names[0],
                    d0_min=self.__roiQRange[0, 0],
                    d0_max=self.__roiQRange[0, 1],
                    dim1=axis_names[1],
                    d1_min=self.__roiQRange[1, 0],
                    d1_max=self.__roiQRange[1, 1],
                    dim2=axis_names[2],
                    d2_min=self.__roiQRange[2, 0],
                    d2_max=self.__roiQRange[2, 1],
                )
            )


class CutPlanePlotWindow(PlotWidget):
    """Plot cut plane as an image

    :param parent: QWidget's parent
    """

    def __init__(self, parent=None):
        super(CutPlanePlotWindow, self).__init__(parent=parent)
        self.setMinimumSize(150, 150)

        # Create toolbar
        toolbar = Qt.QToolBar("Cut Plane Plot", self)
        self.addToolBar(toolbar)

        self.__resetZoomAction = actions.control.ResetZoomAction(parent=self, plot=self)
        toolbar.addAction(self.__resetZoomAction)
        toolbar.addWidget(PlotToolButtons.AspectToolButton(parent=self, plot=self))
        toolbar.addWidget(PlotToolButtons.YAxisOriginToolButton(parent=self, plot=self))
        toolbar.addSeparator()
        self.__copyAction = actions.io.CopyAction(parent=self, plot=self)
        toolbar.addAction(self.__copyAction)
        self.__saveAction = actions.io.SaveAction(parent=self, plot=self)
        toolbar.addAction(self.__saveAction)
        self.__printAction = actions.io.PrintAction(parent=self, plot=self)
        toolbar.addAction(self.__printAction)

        self.setKeepDataAspectRatio(True)
        self.setActiveCurveHandling(False)

    def sizeHint(self):
        return Qt.QSize(200, 200)


class _QSpaceHistogram(PlotWidget):
    """Display histogram of QSpace data

    :param parent: See QWiget
    """

    def __init__(self, parent=None):
        super(_QSpaceHistogram, self).__init__(parent=parent)
        self.setMinimumSize(150, 150)

        # Create toolbar
        toolbar = Qt.QToolBar("Cut Plane Plot", self)
        self.addToolBar(toolbar)

        for action in (
            actions.control.ResetZoomAction(parent=self, plot=self),
            actions.control.YAxisLogarithmicAction(parent=self, plot=self),
        ):
            toolbar.addAction(action)

        toolbar.addSeparator()

        for action in (
            actions.io.CopyAction(parent=self, plot=self),
            actions.io.SaveAction(parent=self, plot=self),
            actions.io.PrintAction(parent=self, plot=self),
        ):
            toolbar.addAction(action)

        self.setKeepDataAspectRatio(False)
        self.setActiveCurveHandling(False)
        self.setDataMargins(yMinMargin=0.05, yMaxMargin=0.05)
        self.getXAxis().setScale(items.Axis.LOGARITHMIC)

    def setData(self, data):
        """Set data from which to compute the histogram

        :param numpy.ndarray data:
        """
        self.clear()
        if data is not None:
            data = data[data > 0]
            result = min_max(data, min_positive=True, finite=True)
            if result.min_positive is None:
                return  # No strictly positive finite data

            edges = np.logspace(
                np.log10(result.min_positive), np.log10(result.maximum), 128
            )
            hist, edges = np.histogram(data, bins=edges)
            self.addHistogram(
                hist,
                edges,
                legend="QSpace Histogram",
                color="blue",
                fill=True,
                copy=False,
            )

    def sizeHint(self):
        return Qt.QSize(200, 200)


class QSpaceView(Qt.QMainWindow):
    """Window displaying the 3D Q space isosurfaces.

    :param qspaceItem: QspaceItem project item
    :param parent: parent widget
    """

    sigFitDone = Qt.Signal(object, object)
    """Signal emitted when the fit is done.

    Arguments : this qspace item's h5Path and the resulting FitH5 file name.
    """

    plot = property(lambda self: self.__plotWindow)

    def __init__(self, qspaceItem, parent=None):
        super(QSpaceView, self).__init__(parent)

        self.setWindowTitle(
            "[XSOCS] {0}:{1}".format(qspaceItem.filename, qspaceItem.path)
        )

        self.__projectItem = qspaceItem

        self.__qspaceH5 = self.__projectItem.qspaceH5

        self.__defaultIsoLevels = None

        # widget that are to be disabled when the fit is running
        self.__lockWidgets = []

        # plot window displaying the intensity map
        self.__plotWindow = PlotIntensityMap(parent=self)
        self.__plotWindow.setToolTip("Intensity Map integrated on whole QSpaces")
        self.__plotWindow.setPointSelectionEnabled(True)
        self.__plotWindow.sigPointSelected.connect(self.__pointSelected)

        self.__roiPlotWindow = ROIPlotIntensityMap(
            parent=self, qspaceH5=self.__projectItem.qspaceH5
        )
        self.__roiPlotWindow.setPointSelectionEnabled(True)
        self.__roiPlotWindow.sigPointSelected.connect(self.__pointSelected)

        self.__plotHistogram = _QSpaceHistogram(parent=self)
        self.__plotHistogram.setToolTip("Histogram of QSpace values")

        with self.__projectItem.qspaceH5 as qspaceH5:
            sampleX = qspaceH5.sample_x
            sampleY = qspaceH5.sample_y
            self.__setPlotData(sampleX, sampleY, qspaceH5.qspace_sum)
            firstX = sampleX[0]
            firstY = sampleY[0]

        # Create StackView
        self.__stackView = StackView()
        self.__stackView.setTitleCallback(WeakMethodProxy(self.__stackViewTitle))
        self.__stackView.setColormap("viridis")
        self.__stackView.setKeepDataAspectRatio(True)
        self.__stackView.getProfileToolbar().setVisible(False)
        self.__stackView.getColorBarAction().setVisible(False)

        plot = self.__stackView.getPlotWidget()
        plot.getMaskAction().setVisible(False)
        self.__stackView.sigPlaneSelectionChanged.connect(self.__updateStackViewROI)
        self.__stackView.sigStackChanged.connect(self.__updateStackViewROI)
        self.__stackView.sigFrameChanged.connect(self.__updateStackViewROI)

        tabWidget = Qt.QTabWidget()
        tabWidget.setTabPosition(Qt.QTabWidget.South)
        tabWidget.addTab(self.__stackView, "Image stack view")
        self.setCentralWidget(tabWidget)

        if _useOpenGL():
            # setting up the plot3D and its param tree
            self.__view3d = ScalarFieldView()
            self.__view3d.addIsosurface(self.__defaultIsoLevel1, "#FF000060")
            self.__view3d.addIsosurface(self.__defaultIsoLevel2, "#00FF00FF")
            self.__view3d.setMinimumSize(400, 400)

            sfTree = SFViewParamTree()
            sfTree.setIsoLevelSliderNormalization("arcsinh")
            sfTree.setSfView(self.__view3d)

            # Register ROIPlotIntensity
            self.__view3d.sigSelectedRegionChanged.connect(
                self.__roiPlotWindow.roiChanged
            )

            # Store the cut plane signals connection state
            self.__connectedToCutPlane = True
            self.__view3d.getCutPlanes()[0].sigPlaneChanged.connect(
                self.__cutPlaneChanged
            )
            self.__view3d.getCutPlanes()[0].sigColormapChanged.connect(
                self.__cutPlaneChanged
            )
            self.__view3d.getCutPlanes()[0].sigDataChanged.connect(
                self.__cutPlaneChanged
            )

            # Add 3D widget to QSpace widget
            tabWidget.addTab(self.__view3d, "3D view")
            tabWidget.setCurrentIndex(1)

            sfDock = Qt.QDockWidget()
            sfDock.setWindowTitle("Isosurface options")
            sfDock.setWidget(sfTree)
            features = sfDock.features() ^ Qt.QDockWidget.DockWidgetClosable
            sfDock.setFeatures(features)
            self.addDockWidget(Qt.Qt.LeftDockWidgetArea, sfDock)
            self.__lockWidgets.append(sfDock)

            self.__planePlotWindow = CutPlanePlotWindow(self)

            planePlotDock = Qt.QDockWidget("Cut Plane", self)
            planePlotDock.setWidget(self.__planePlotWindow)
            features = planePlotDock.features() ^ Qt.QDockWidget.DockWidgetClosable
            planePlotDock.setFeatures(features)
            planePlotDock.visibilityChanged.connect(
                self.__planePlotDockVisibilityChanged
            )
            self.splitDockWidget(sfDock, planePlotDock, Qt.Qt.Vertical)
            self.__lockWidgets.append(planePlotDock)

        else:
            self.__view3d = None

        self.__fitWidget = FitWidget(self.__qspaceH5.filename)
        self.__fitWidget.roiWidget().sigRoiChanged.connect(self.__slotRoiChanged)
        self.__fitWidget.roiWidget().toggled.connect(self.__slotRoiToggled)
        self.__fitWidget.sigProcessStarted.connect(self.__slotFitProcessStarted)
        self.__fitWidget.sigProcessDone.connect(self.__slotFitProcessDone)
        self.__fitWidget.sigFitTypeChanged.connect(self.__nextFitFile)
        self.__nextFitFile()
        fitDock = Qt.QDockWidget()
        fitDock.setWindowTitle("Fit")
        fitDock.setWidget(self.__fitWidget)
        features = fitDock.features() ^ Qt.QDockWidget.DockWidgetClosable
        fitDock.setFeatures(features)
        self.addDockWidget(Qt.Qt.RightDockWidgetArea, fitDock)

        # Add Plots to tabbed dock widgets
        previousDock = None if self.__view3d is None else planePlotDock
        for title, widget in (
            ("Histogram", self.__plotHistogram),
            ("ROI Intensity", self.__roiPlotWindow),
            ("Intensity", self.__plotWindow),
        ):
            dock = Qt.QDockWidget(title, self)
            dock.setWidget(widget)
            features = dock.features() ^ Qt.QDockWidget.DockWidgetClosable
            dock.setFeatures(features)
            self.__lockWidgets.append(dock)

            if previousDock is None:
                self.addDockWidget(Qt.Qt.LeftDockWidgetArea, dock)
            else:
                self.tabifyDockWidget(previousDock, dock)
            previousDock = dock

        self.__showIsoView(firstX, firstY)

    def __getDefaultIsoLevels(self, data):
        """Returns array of default isosurface levels, computing them if needed

        :param numpy.ndarray data: Data from which to compute iso levels
        :return: array of default isosurface levels
        """
        if self.__defaultIsoLevels is None:
            result = min_max(data, min_positive=True, finite=True)
            min_ = result.min_positive
            max_ = result.maximum
            if min_ is not None and max_ is not None:
                self.__defaultIsoLevels = np.logspace(
                    np.log10(min_), np.log10(max_), 4
                )[1:-1]
            else:
                self.__defaultIsoLevels = 1, 1  # Fallback no positive data

        return self.__defaultIsoLevels

    def __defaultIsoLevel1(self, data):
        """Return first isosurface default level"""
        return self.__getDefaultIsoLevels(data)[0]

    def __defaultIsoLevel2(self, data):
        """Returns second isosurface default level"""
        return self.__getDefaultIsoLevels(data)[1]

    def __setPlotData(self, x, y, data):
        """Sets the intensity maps data.

        :param x:
        :param y:
        :param data:
        """
        self.__plotWindow.setPlotData(x, y, data)
        self.__plotWindow.resetZoom()
        self.__roiPlotWindow.setPlotData(x, y, data)
        self.__roiPlotWindow.resetZoom()

    def selectPoint(self, x, y):
        """Displays the q space closest to sample coordinates x and y.

        :param x:
        :param y:
        """
        self.__showIsoView(x, y)

    def __pointSelected(self, point):
        """
        Slot called each time a point is selected on one of the intensity maps.

        Displays the corresponding q space cube.

        :param point:
        """
        xIdx = point.xIdx
        x = point.x
        y = point.y

        self.__showIsoView(x, y, xIdx)

    def __showIsoView(self, x, y, idx=None):
        """Displays the q space closest to sample coordinates x and y.

        If idx is provided, x and y are ignored. If idx is not provided, the
        closest point to x and y is selected.

        :param x: sample x coordinate of the point to select
        :param y: sample y coordinate of the point to select
        :param idx:
            index of the point to select in the array of sample coordinates.
        """
        if self.sender() == self.__roiPlotWindow:
            self.__plotWindow.selectPoint(x, y)
        elif self.sender() == self.__roiPlotWindow:
            self.__roiPlotWindow.selectPoint(x, y)
        else:
            self.__plotWindow.selectPoint(x, y)
            self.__roiPlotWindow.selectPoint(x, y)

        with self.__qspaceH5 as qspaceH5:
            if idx is None:
                sampleX = qspaceH5.sample_x
                sampleY = qspaceH5.sample_y

                idx = ((sampleX - x) ** 2 + (sampleY - y) ** 2).argmin()

            qspace = qspaceH5.qspace_slice(idx)
            histo = qspaceH5.histo
            mask = histo > 0

            # Normalize values with histogram counts
            qspace[mask] /= histo[mask]

            # When QSpace was computed with normalized value,
            # Normalize values with min
            # to get a value in the range of "photon count"
            if qspaceH5.image_normalizer:
                _logger.info("Normalize displayed values with the minimum")
                qspace /= np.nanmin(qspace[np.logical_and(mask, qspace > 0)])

            # Set scale and translation
            # Do it before setting data as corresponding
            # nodes in the SFViewParamTree are updated on sigDataChanged

            minBinEdge = []
            binSteps = []
            for array in qspaceH5.qspace_dimension_values:
                min_, _, step = bin_centers_to_range_step(array)
                minBinEdge.append(min_)
                binSteps.append(step)

            axisNames = list(qspaceH5.qspace_dimension_names)

            # Swap qspace dataset to be qz, qy, qx (was qx, qy, qz)
            # For spherical, swap from (pitch, roll, radial) to (radial, roll, pitch).
            qspace = qspace.swapaxes(0, 2)

            for widget, label in zip(
                self.__fitWidget.roiWidget().roiAxisWidgets(), axisNames
            ):
                widget.setText(label)

            if self.__view3d is not None:
                extents = np.array(binSteps) * np.array(qspace.shape)[::-1]
                if extents.max() / extents.min() > 3.0:
                    _logger.info("Rescale 3D View to display data as a cube")
                    self.__view3d.setOuterScale(*(1.0 / extents))

                self.__view3d.setScale(*binSteps)
                self.__view3d.setTranslation(*minBinEdge)

                self.__view3d.setAxesLabels(*axisNames)

                self.__defaultIsoLevels = None  # Reset default isosurface levels

                self.__view3d.setData(qspace)

            perspective = self.__stackView.getPerspective()

            wasStack = self.__stackView.getStack(copy=False) is not None
            self.__stackView.setLabels(list(reversed(axisNames)))
            self.__stackView.setStack(
                qspace,
                perspective=perspective,
                reset=False,
                calibrations=tuple(reversed(tuple(zip(minBinEdge, binSteps)))),
            )

            if not wasStack:
                self.__stackView.resetZoom()

        self.__plotHistogram.setData(qspace)

        # Update sliders histograms
        self.__fitWidget.setQSpaceIndex(idx)

    def __nextFitFile(self):
        """
        Temporary method that generated a new file name for the Fit results.
        """
        prefix = os.path.basename(self.__projectItem.path)
        project = self.__projectItem.projectRoot()

        fitName = self.__fitWidget.getFitName()

        template = "{0}_{1}_{{0:>04}}.h5".format(prefix, fitName.lower())
        output_f = nextFileName(project.workdir, template)
        self.__fitWidget.setOutputFile(output_f)

    def __slotFitProcessStarted(self):
        """Slot called when a fit is started.

        Locks all widgets that reads the XsocsProject file.
        This is necessary because that file is opened in write mode
        when the fit is done, to write the fit result.
        """
        for widget in self.__lockWidgets:
            widget.setEnabled(False)

    def __slotFitProcessDone(self, event):
        """Slot called when the fit is done.

        Event is the name of the FitH5 file that has been created.
        Unlocks the widgets locked in __slotFitProcessStarted.
        Emits QSpaceView.sigFitDone.

        :param event:
        """
        if event is not None:
            self.__nextFitFile()
            self.sigFitDone.emit(self.__projectItem.path, event)

        for widget in self.__lockWidgets:
            widget.setEnabled(True)

    def __stackViewTitle(self, index):
        """Returns StackView title

        :param ind index: Frame index
        :rtype: str
        """
        perspective = self.__stackView.getPerspective()
        label = self.__stackView.getLabels()[perspective]

        calibration = self.__stackView.getCalibrations(order="axes")[-1]

        return "%s = %f" % (label, calibration(index))

    def __updateStackViewROI(self, *args, **kwargs):
        """Update display of ROI on StackView"""
        legend = "__QSpaceView_ROI__"

        if self.__fitWidget.roiWidget().isChecked():
            # Get ROI range for currently displayed axes
            roiSliders = tuple(reversed(self.__fitWidget.roiWidget().sliders()))

            perspective = self.__stackView.getPerspective()

            # Get image axes indices
            image_dimensions = [d for d in (0, 1, 2) if d != perspective]
            yIndex, xIndex = min(image_dimensions), max(image_dimensions)

            frame = self.__stackView.getFrameNumber()
            begin, end = roiSliders[perspective].getPositions()

            if begin <= frame < end:
                # Fill for edges of the ROI
                fill = (frame == begin) or (frame == end - 1)

                xRange = roiSliders[xIndex].getValues()
                yRange = roiSliders[yIndex].getValues()

                self.__stackView.addShape(
                    xRange,
                    yRange,
                    legend="__QSpaceView_ROI__",
                    shape="rectangle",
                    color="pink",
                    fill=fill,
                    overlay=True,
                )
            else:
                self.__stackView.remove(legend, kind="item")

        else:
            self.__stackView.remove(legend, kind="item")

    def __slotRoiToggled(self, on):
        """Slot called when the Roi selection is enabled.

        :param on:
        """
        if self.__view3d is not None:
            region = self.__view3d.getSelectedRegion()

            if not on:
                # Reset selection region
                self.__view3d.setSelectedRegion()
            else:
                if region is None:  # Init region
                    data = self.__view3d.getData(copy=False)

                    if data is not None:
                        depth, height, width = data.shape
                        self.__view3d.setSelectedRegion(
                            zrange=(0, depth), yrange=(0, height), xrange_=(0, width)
                        )
                        region = self.__view3d.getSelectedRegion()

            if on and region:
                xRange, yRange, zRange = region.getDataRange()
            else:
                xRange, yRange, zRange = None, None, None
        else:
            xRange, yRange, zRange = None, None, None

        # TODO would be better to do that in fit widget
        for slider, range_ in zip(
            self.__fitWidget.roiWidget().sliders(), (xRange, yRange, zRange)
        ):
            if range_ is None:
                range_ = slider.getRange()
            slider.setValues(*range_)

        self.__updateStackViewROI()

    def __slotRoiChanged(self, event):
        """Slot called each time the ROI is modified

        :param event:
        """

        if self.__view3d is not None:
            region = self.__view3d.getSelectedRegion()
            if region is None:
                return

            roiRanges = [(state.leftIndex, state.rightIndex) for state in event]

            self.__view3d.setSelectedRegion(
                zrange=roiRanges[2], yrange=roiRanges[1], xrange_=roiRanges[0]
            )

        self.__updateStackViewROI()

    def __planePlotDockVisibilityChanged(self, visible):
        cutPlane = self.__view3d.getCutPlanes()[0]
        if visible:
            if not self.__connectedToCutPlane:  # Prevent multiple connect
                self.__connectedToCutPlane = True
                cutPlane.sigPlaneChanged.connect(self.__cutPlaneChanged)
                cutPlane.sigColormapChanged.connect(self.__cutPlaneChanged)
                cutPlane.sigDataChanged.connect(self.__cutPlaneChanged)
                self.__cutPlaneChanged()  # To sync
        else:
            if self.__connectedToCutPlane:  # Prevent multiple disconnect
                self.__connectedToCutPlane = False
                cutPlane.sigPlaneChanged.disconnect(self.__cutPlaneChanged)
                cutPlane.sigColormapChanged.connect(self.__cutPlaneChanged)
                cutPlane.sigDataChanged.disconnect(self.__cutPlaneChanged)

    def __cutPlaneChanged(self):
        plane = self.__view3d.getCutPlanes()[0]

        if plane.isVisible() and plane.isValid():
            planeImage = plane.getImageData()
            if planeImage.isValid():
                self.__planePlotWindow.setGraphXLabel(planeImage.getXLabel())
                self.__planePlotWindow.setGraphYLabel(planeImage.getYLabel())
                title = planeImage.getNormalLabel() + " = %f" % planeImage.getPosition()
                self.__planePlotWindow.setGraphTitle(title)

                colormap = plane.getColormap()
                vmin, vmax = plane.getColormapEffectiveRange()
                norm = colormap.getNormalization()
                plotColormap = {
                    "name": colormap.getName(),
                    "normalization": norm,
                    "autoscale": False,
                    "vmin": vmin,
                    "vmax": vmax,
                }

                self.__planePlotWindow.addImage(
                    planeImage.getData(copy=False),
                    legend="cutting plane",
                    colormap=plotColormap,
                    origin=planeImage.getTranslation(),
                    scale=planeImage.getScale(),
                    resetzoom=True,
                )
