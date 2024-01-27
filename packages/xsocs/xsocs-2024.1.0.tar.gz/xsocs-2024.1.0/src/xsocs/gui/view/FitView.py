from collections import OrderedDict
import logging

import numpy as np

from silx.gui import qt as Qt

from ..widgets.Containers import GroupBox
from ..widgets.XsocsPlot2D import XsocsPlot2D
from ..model.TreeView import TreeView
from ..project.QSpaceGroup import QSpaceItem
from .fitview.FitModel import FitModel, FitH5Node
from .fitview.DropPlotWidget import DropPlotWidget

from .fitview.Plotter import GaussianPlotter, CentroidPlotter
from ...process.fit import background_estimation, BackgroundTypes
from ...util import project


_logger = logging.getLogger(__name__)


class FitTreeView(TreeView):
    def sizeHint(self):
        return Qt.QSize(400, 175)


class FitView(Qt.QMainWindow):
    sigPointSelected = Qt.Signal(object)

    def __init__(self, parent, fitItem, **kwargs):
        super(FitView, self).__init__(parent, **kwargs)

        self.__firstShow = True

        self.setWindowTitle("[XSOCS] {0}:{1}".format(fitItem.filename, fitItem.path))

        self.__fitH5 = fitItem.fitH5
        self.__fitItem = fitItem

        # TODO : improve
        qspaceItem = fitItem.parent(classinfo=QSpaceItem)
        if qspaceItem is None:
            raise ValueError("This fitItem is not part of a project.")

        self.__qspaceH5 = qspaceItem.qspaceH5

        with self.__fitH5:
            # only one entry per file supposed right now
            self.__entry = self.__fitH5.entries()[0]
            self.__axis_names = self.__fitH5.get_qspace_dimension_names(self.__entry)

        treeDock = Qt.QDockWidget()

        columns = [name.capitalize() for name in self.__axis_names]
        self.__model = FitModel(columnNames=["Param"] + columns)
        rootNode = FitH5Node(fitItem.fitFile)
        self.__model.appendGroup(rootNode)

        tree = self.__tree = FitTreeView()
        tree.setMinimumWidth(410)  # TODO: is there a better way?
        # tree.resize(420, tree.height())

        tree.setModel(self.__model)
        # tree.setRootIndex(self.__model.index(0, 0, tree.rootIndex()))
        tree.setSelectionBehavior(Qt.QAbstractItemView.SelectItems)
        tree.header().setStretchLastSection(False)
        tree.setShowUniqueGroup(True)
        tree.setDragDropMode(Qt.QAbstractItemView.DragDrop)

        treeDock.setWidget(tree)
        self.addDockWidget(Qt.Qt.LeftDockWidgetArea, treeDock)

        centralWid = Qt.QWidget()
        layout = Qt.QGridLayout(centralWid)

        self.__plots = []
        self.__fitPlots = []

        grpBox = GroupBox("Maps")
        grpLayout = Qt.QVBoxLayout(grpBox)

        for _ in self.__axis_names:
            plot = DropPlotWidget(
                grid=False,
                curveStyle=False,
                colormap=False,
                roi=False,
                mask=False,
                yInverted=False,
            )
            grpLayout.addWidget(plot)
            self.__plots.append(plot)
            plot.sigPointSelected.connect(self.__slotPointSelected)

        layout.addWidget(grpBox, 0, 1)

        # =================================
        # =================================

        grpBox = GroupBox("Fit")
        grpLayout = Qt.QVBoxLayout(grpBox)

        for axis in self.__axis_names:
            plot = XsocsPlot2D()
            plot.setKeepDataAspectRatio(False)
            grpLayout.addWidget(plot)
            self.__fitPlots.append(plot)
            plot.setGraphTitle("%s fit" % axis.capitalize())
            plot.setShowMousePosition(True)

        layout.addWidget(grpBox, 0, 2)

        # =================================
        # =================================

        # centralWid.resize(500, centralWid.height())
        self.setCentralWidget(centralWid)

    def getFitItem(self):
        return self.__fitItem

    def showEvent(self, event):
        """
        Overload method from Qt.QWidget.showEvent to set up the widget the
        first time it is shown. Also starts the model in a queued slot, so that
        the window is shown right away, and the thumbnails are drawn
        afterwards.

        :param event:
        """
        super(FitView, self).showEvent(event)
        if self.__firstShow:
            self.__firstShow = False
            Qt.QTimer.singleShot(0, self.__firstInit)

    def __firstInit(self):
        """Called the first time the window is shown."""
        initDiag = Qt.QProgressDialog(
            "Setting up fit view.", "cc", 0, 100, parent=self.parent()
        )
        initDiag.setWindowTitle("Please wait...")
        initDiag.setCancelButton(None)
        initDiag.setModal(True)
        initDiag.setAttribute(Qt.Qt.WA_DeleteOnClose)
        initDiag.show()
        initDiag.setValue(10)
        self.__initPlots()
        initDiag.setValue(40)
        self.__startModel()
        initDiag.setValue(70)
        tree = self.__tree
        root = self.__model.index(0, 0, tree.rootIndex())
        tree.setRootIndex(self.__model.index(0, 0, root))
        initDiag.setValue(90)
        tree.expandAll()
        initDiag.setValue(100)
        initDiag.accept()
        initDiag.close()

    def __startModel(self):
        """Starts the model (in this case draws the thumbnails"""
        self.__model.startModel()

    def __initPlots(self):
        """Initializes the "map" plots."""
        entry = None
        process = None
        with self.__fitH5:
            entries = self.__fitH5.entries()
            if entries:
                entry = entries[0]
                processes = self.__fitH5.processes(entry)
                if processes:
                    process = processes[0]

        if entry in ("Gaussian", "SilxFit"):
            _initGaussian(self.__plots, self.__fitH5.filename, entry, process)
        elif entry == "Centroid":
            _initCentroid(self.__plots, self.__fitH5.filename, entry, process)
        else:
            _logger.error("Unsupported entry: %s, process: %s", entry, process)

    def __slotPointSelected(self, point):
        """Called when a point is selected on one of the "map" plots.

        :param point:
        """
        sender = self.sender()
        for plot in self.__plots:
            if plot != sender:
                plot.selectPoint(point.x, point.y)

        self.__plotFitResults(point.xIdx)
        self.sigPointSelected.emit(point)

    def __plotFitResults(self, xIdx):
        """Plots the fit results for the selected point on the plot.

        :param xIdx:
        """
        entry = self.__entry

        # Get fit result
        with self.__fitH5:
            backgroundMode = self.__fitH5.get_background_mode(entry)

            xFitQX, xFitQY, xFitQZ = self.__fitH5.get_qspace_dimension_values(entry)
            roi_indices = self.__fitH5.get_roi_indices(entry)

            qxPeakParams = OrderedDict()
            qyPeakParams = OrderedDict()
            qzPeakParams = OrderedDict()

            processes = self.__fitH5.processes(entry)

            for process in processes:
                results = self.__fitH5.get_result_names(entry, process)
                qxPeakParams[process] = {}
                qyPeakParams[process] = {}
                qzPeakParams[process] = {}
                for result in results:
                    qxPeakParams[process][result] = self.__fitH5.get_axis_result(
                        entry, process, result, 0
                    )[xIdx]
                    qyPeakParams[process][result] = self.__fitH5.get_axis_result(
                        entry, process, result, 1
                    )[xIdx]
                    qzPeakParams[process][result] = self.__fitH5.get_axis_result(
                        entry, process, result, 2
                    )[xIdx]

        # Get QSpace data and project to axes
        with self.__qspaceH5:
            xAcqQX, xAcqQY, xAcqQZ = self.__qspaceH5.qspace_dimension_values
            cube = self.__qspaceH5.qspace_slice(xIdx)
            histo = self.__qspaceH5.histo

        yAcqQX, yAcqQY, yAcqQZ = project(cube, histo)

        if roi_indices is None:
            qslice = np.s_[:, :, :]
        else:
            qslice = np.s_[
                roi_indices[0][0] : roi_indices[0][1],
                roi_indices[1][0] : roi_indices[1][1],
                roi_indices[2][0] : roi_indices[2][1],
            ]
            yAcqQroi = project(cube[qslice], histo[qslice])

        # Get plotter
        if entry == "Gaussian":
            plotterKlass = GaussianPlotter
        elif entry == "Centroid":
            plotterKlass = CentroidPlotter
        else:
            raise RuntimeError("Unsupported entry: %s" % entry)
        plotter = plotterKlass()
        title = plotter.getPlotTitle()

        # Update plot with gathered information
        idim = 0
        for plot, name, xAcq, yAcq, xFit, peakParams in zip(
            self.__fitPlots,
            self.__axis_names,
            (xAcqQX, xAcqQY, xAcqQZ),
            (yAcqQX, yAcqQY, yAcqQZ),
            (xFitQX, xFitQY, xFitQZ),
            (qxPeakParams, qyPeakParams, qzPeakParams),
        ):
            plot.clearCurves()
            plot.clearMarkers()

            plot.setGraphTitle("{0} ({1})".format(title, name))
            plot.addCurve(xAcq, yAcq, legend="measured", color="blue", linestyle=":")

            yAcqroi = yAcq  # default
            xAcqroi = xAcq

            if roi_indices is not None:
                xAcqroi = xAcq[qslice[idim]]
                yAcqroi = yAcqQroi[idim]
                plot.addCurve(
                    xAcqroi,
                    yAcqroi,
                    legend="measured (ROI)",
                    color="blue",
                    linestyle="-",
                )

            background = None
            if backgroundMode != BackgroundTypes.NONE:  # Display background
                background = background_estimation(backgroundMode, yAcqroi)
                plot.addCurve(
                    xAcqroi,
                    background,
                    legend="background",
                    linestyle="--",
                    color="black",
                )

            plotter.plotFit(plot, xFit, peakParams, background)
            idim += 1


def _initGaussian(plots, fitH5Name, entry, process):
    """Sets up the plots when the interface is shown for the first time.

    :param plots: the plot widgets
    :param fitH5Name: fitH5 file name
    :param entry: name of the entry in the fitH5
    :param process: name of the process in the fitH5
    """
    # hard coded result name, this isn't satisfactory but I can't think
    # of any other way right now.

    qApp = Qt.QApplication.instance()

    for index in range(3):
        qApp.processEvents()
        plots[index].plotFitResult(fitH5Name, entry, process, "Center", index)


def _initCentroid(plots, fitH5Name, entry, process):
    """Sets up the plots when the interface is shown for the first time.

    :param plots: the plot widgets
    :param fitH5Name: fitH5 file name
    :param entry: name of the entry in the fitH5
    :param process: name of the process in the fitH5
    """
    # hard coded result name, this isn't satisfactory but I can't think
    # of any other way right now.
    qApp = Qt.QApplication.instance()

    for index in range(3):
        qApp.processEvents()
        plots[index].plotFitResult(fitH5Name, entry, process, "COM", index)
