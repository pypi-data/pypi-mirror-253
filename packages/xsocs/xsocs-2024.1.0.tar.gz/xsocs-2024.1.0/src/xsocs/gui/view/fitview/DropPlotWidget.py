import numpy as np

from silx.gui import qt as Qt

from ....io.FitH5 import FitH5
from ....process.fit import FitStatus

from ...widgets.XsocsPlot2D import XsocsPlot2D


class DropPlotWidget(XsocsPlot2D):
    sigSelected = Qt.Signal(object)

    def __init__(self, *args, **kwargs):
        super(DropPlotWidget, self).__init__(*args, **kwargs)

        self.__legend = None

        self.setActiveCurveHandling(False)
        self.setKeepDataAspectRatio(True)
        self.setAcceptDrops(True)
        self.setPointSelectionEnabled(True)
        self.setShowMousePosition(True)

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if not mimeData.hasFormat("application/FitModel"):
            return super(DropPlotWidget, self).dropEvent(event)
        qByteArray = mimeData.data("application/FitModel")
        stream = Qt.QDataStream(qByteArray, Qt.QIODevice.ReadOnly)
        h5File = stream.readQString()
        entry = stream.readQString()
        q_axis = stream.readInt()

        type = stream.readQString()

        if type == "result":
            process = stream.readQString()
            result = stream.readQString()
            self.plotFitResult(h5File, entry, process, result, q_axis)
        elif type == "status":
            self.plotFitStatus(h5File, entry, q_axis)

    def dragEnterEvent(self, event):
        # super(DropWidget, self).dragEnterEvent(event)
        if event.mimeData().hasFormat("application/FitModel"):
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        super(DropPlotWidget, self).dragLeaveEvent(event)

    def dragMoveEvent(self, event):
        super(DropPlotWidget, self).dragMoveEvent(event)

    def plotFitResult(self, fitH5Name, entry, process, result, q_axis):
        with FitH5(fitH5Name) as h5f:
            data = h5f.get_axis_result(entry, process, result, q_axis)
            scan_x, scan_y = h5f.sample_positions(entry)
            axis_name = h5f.get_qspace_dimension_names(entry)[q_axis]

        xBorder = np.array([scan_x.min(), scan_x.max()])
        yBorder = np.array([scan_y.min(), scan_y.max()])
        self.addCurve(
            xBorder,
            yBorder,
            linestyle=" ",
            symbol=".",
            color="white",
            legend="__border",
            z=-1,
        )

        self.__legend = self.setPlotData(scan_x, scan_y, data)
        self.setGraphTitle(result + "[" + axis_name + "]")

    def plotFitStatus(self, fitH5Name, entry, q_axis):
        with FitH5(fitH5Name) as h5f:
            axis_name = h5f.get_qspace_dimension_names(entry)[q_axis]
            data = h5f.get_status(entry, q_axis)
            errorPts = np.where(data != FitStatus.OK)[0]
            if len(errorPts) == 0:
                return
            scan_x, scan_y = h5f.sample_positions(entry)
            scan_x = scan_x[errorPts]
            scan_y = scan_y[errorPts]
            data = data[errorPts]

        self.__legend = self.setPlotData(scan_x, scan_y, data, dataIndices=errorPts)
        self.setGraphTitle("Errors[qx]" + axis_name)
