from silx.gui import qt as Qt

import numpy as np

from ...widgets.PlotGrabber import PlotGrabber

from ...model.ModelDef import ModelRoles
from ...model.Model import Model, RootNode

from ...project.Hdf5Nodes import H5File
from ...project.Hdf5Nodes import H5Base, H5NodeClassDef

from ....io.FitH5 import FitH5
from ....process.fit import FitStatus


@H5NodeClassDef("FitH5")
class FitH5Node(H5File):
    """
    Node linked to a FitH5 file.
    """

    # TODO : check the file format (make sure that all required
    # groups/datasets are there)

    def _loadChildren(self):
        base = self.h5Path.rstrip("/")
        children = []
        with FitH5(self.h5File, mode="r") as h5f:
            entries = h5f.entries()

        for entry in entries:
            child = FitEntryNode(self.h5File, base + "/" + entry)
            children.append(child)

        return children


@H5NodeClassDef("FitEntry")
class FitEntryNode(H5Base):
    """
    Node linked to an entry in a FitH5 file.
    """

    entry = property(lambda self: self.h5Path.lstrip("/").split("/")[0])

    def _loadChildren(self):
        base = self.h5Path.rstrip("/")
        entry = self.entry
        children = []

        with FitH5(self.h5File, mode="r") as h5f:
            processes = h5f.processes(entry)
        for process in processes:
            child = FitProcessNode(self.h5File, base + "/" + process)
            children.append(child)

        statusNode = FitStatusNode(self.h5File, base)
        children.append(statusNode)

        return children

    def mimeData(self, column, stream):
        if column not in (1, 2, 3):
            raise ValueError("Unexpected column.")
        q_axis = column - 1

        h5file = self.h5File
        entry = self.entry

        stream.writeQString(h5file)
        stream.writeQString(entry)
        stream.writeInt(q_axis)

        return True


class FitProcessNode(FitEntryNode):
    """
    Node linked to a process group in a FitH5 file.
    """

    process = property(lambda self: self.h5Path.lstrip("/").split("/")[1])

    def _loadChildren(self):
        base = self.h5Path.rstrip("/")
        entry = self.entry
        process = self.process
        children = []
        with FitH5(self.h5File, mode="r") as h5f:
            results = h5f.get_result_names(entry, process)
        for result in results:
            child = FitResultNode(self.h5File, base + "/" + result)
            children.append(child)

        return children


class FitStatusNode(FitEntryNode):
    """
    Preview of the points where the fit has failed.
    """

    def __init__(self, *args, **kwargs):
        self.dragEnabledColumns = [False, True, True, True]
        super(FitStatusNode, self).__init__(*args, **kwargs)
        self.nodeName = "Status"

        self.__nErrors = [0, 0, 0]

    def _setupNode(self):
        width = 100
        plot = PlotGrabber()
        plot.setFixedSize(Qt.QSize(width, 100))
        plot.toPixmap()

        qApp = Qt.QApplication.instance()
        qApp.processEvents()

        with FitH5(self.h5File) as fitH5:
            x, y = fitH5.sample_positions(self.entry)

            for iax, axis in enumerate(fitH5.get_qspace_dimension_names(self.entry)):
                status = fitH5.get_status(self.entry, iax)
                errorPts = np.where(status != FitStatus.OK)[0]
                self.__nErrors[iax] = len(errorPts)
                if len(errorPts) != 0:
                    plot.setPlotData(x[errorPts], y[errorPts], status[errorPts])
                    plot.replot()
                    pixmap = plot.toPixmap()
                else:
                    label = Qt.QLabel("No errors")
                    label.setFixedWidth(width)
                    label.setAlignment(Qt.Qt.AlignCenter)
                    label.setAttribute(Qt.Qt.WA_TranslucentBackground)
                    pixmap = label.grab()
                self._setDataInternal(iax + 1, pixmap, Qt.Qt.DecorationRole)
                qApp.processEvents()

    def _loadChildren(self):
        return []

    def mimeData(self, column, stream):
        if column < 1 or column > 3:
            return False

        if self.__nErrors[column - 1] == 0:
            return False

        if not FitEntryNode.mimeData(self, column, stream):
            return False

        stream.writeQString("status")

        return True


class FitResultNode(FitProcessNode):
    """
    Node linked to a result group in a FitH5 file.
    """

    result = property(lambda self: self.h5Path.split("/")[-1])

    def __init__(self, *args, **kwargs):
        self.dragEnabledColumns = [False, True, True, True]
        super(FitResultNode, self).__init__(*args, **kwargs)

    def _setupNode(self):
        plot = PlotGrabber()
        plot.setFixedSize(Qt.QSize(100, 100))
        plot.toPixmap()

        qApp = Qt.QApplication.instance()
        qApp.processEvents()

        with FitH5(self.h5File) as fitH5:
            x, y = fitH5.sample_positions(self.entry)

            xBorder = np.array([x.min(), x.max()])
            yBorder = np.array([y.min(), y.max()])

            for iax, axis in enumerate(fitH5.get_qspace_dimension_names(self.entry)):
                data = fitH5.get_axis_result(self.entry, self.process, self.result, iax)

                plot.addCurve(
                    xBorder,
                    yBorder,
                    linestyle=" ",
                    symbol=".",
                    color="white",
                    legend="__border",
                    z=-1,
                )
                plot.setPlotData(x, y, data)

                # WARNING, DO NOT REMOVE
                # for some reason the first thumbnail is empty if we dont call
                # replot.
                # ============
                plot.replot()
                # ============
                # WARNING END

                pixmap = plot.toPixmap()
                self._setDataInternal(iax + 1, pixmap, Qt.Qt.DecorationRole)
                qApp.processEvents()

    def _loadChildren(self):
        return []

    def mimeData(self, column, stream):
        if not FitProcessNode.mimeData(self, column, stream):
            return False

        process = self.process
        result = self.result
        stream.writeQString("result")
        stream.writeQString(process)
        stream.writeQString(result)

        return True


class FitRootNode(RootNode):
    """
    Root node for the FitModel
    """

    ColumnNames = ["", "", "", ""]  # Needed for init

    def __init__(self, *args, **kwargs):
        self.ColumnNames = list(kwargs.pop("columnNames"))
        super(FitRootNode, self).__init__(*args, **kwargs)


class FitModel(Model):
    """
    Model displaying a FitH5 file contents.
    """

    RootNode = FitRootNode
    ColumnsWithDelegates = [1, 2, 3]

    def __init__(self, columnNames, parent=None):
        super(FitModel, self).__init__(parent, columnNames=columnNames)

    def mimeData(self, indexes):
        if len(indexes) > 1:
            raise ValueError("Drag&Drop of more than one item is not" "supported yet.")

        mimeData = Qt.QMimeData()

        index = indexes[0]
        node = index.data(ModelRoles.InternalDataRole)

        if not isinstance(node, (FitResultNode, FitStatusNode)):
            return super(Model, self).mimeData(indexes)

        data = Qt.QByteArray()
        stream = Qt.QDataStream(data, Qt.QIODevice.WriteOnly)
        if node.mimeData(index.column(), stream):
            mimeData.setData("application/FitModel", data)

        return mimeData
