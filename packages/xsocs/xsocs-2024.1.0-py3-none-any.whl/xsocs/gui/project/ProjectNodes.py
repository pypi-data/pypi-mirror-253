import os
import weakref


import h5py

from silx.gui import qt as Qt, icons
from silx.gui.qt import inspect

from ..model.Node import Node
from ..model.ModelDef import ModelColumns
from ..model.NodeEditor import EditorMixin

from .IntensityGroup import IntensityItem
from .XsocsH5Factory import h5NodeToProjectItem
from .Hdf5Nodes import H5GroupNode, H5NodeClassDef, H5DatasetNode

from ..view.FitView import FitView
from ..view.QspaceView import QSpaceView
from ..view.intensity.IntensityView import IntensityView

from ..project.QSpaceGroup import QSpaceItem
from ..project.FitGroup import FitItem
from ..project.ProjectItem import ProjectItem
from ..project.IntensityGroup import IntensityGroup


class ProjectNode(H5GroupNode):
    """
    A base node class for xsocs project items.
    """

    def __init__(self, *args, **kwargs):
        self.__isInit = False

        super(ProjectNode, self).__init__(*args, **kwargs)

        itemName = self.getProjectItem().getItemName()

        if itemName:
            self._setDataInternal(ModelColumns.NameColumn, itemName)
            self._setDataInternal(
                ModelColumns.NameColumn, itemName, role=Qt.Qt.EditRole
            )

    def getProjectItem(self):
        """
        Returns an instance of the project item associated with
        this ProjectNode.
        :return: a project item, or None
        """
        # item = ProjectItem(self.h5File, self.h5Path)
        item = h5NodeToProjectItem(self)
        if item:
            return item.cast()
        return None

    def setData(self, column, data, role=Qt.Qt.DisplayRole):
        if (
            role == Qt.Qt.EditRole or role == role.EditRole
        ) and column == ModelColumns.NameColumn:
            if not data:
                data = os.path.basename(self.getProjectItem().path)

            self.getProjectItem().setItemName(data)
        return super(ProjectNode, self).setData(column, data, role=role)


class ScatterPlotButton(EditorMixin, Qt.QWidget):
    persistent = True

    sigValueChanged = Qt.Signal()

    def __init__(self, parent, option, index):
        super(ScatterPlotButton, self).__init__(parent, option, index)
        layout = Qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        icon = icons.getQIcon("plot-widget")
        button = Qt.QToolButton()
        button.setIcon(icon)
        layout.addWidget(button)
        layout.addStretch(1)

        button.clicked.connect(self.__clicked)

    def __clicked(self):
        # node = self.node
        event = {"event": "scatter"}
        self.notifyView(event)


class QSpaceButton(EditorMixin, Qt.QWidget):
    persistent = True

    sigValueChanged = Qt.Signal()

    def __init__(self, parent, option, index):
        super(QSpaceButton, self).__init__(parent, option, index)
        layout = Qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        icon = icons.getQIcon("item-ndim")
        button = Qt.QToolButton()
        button.setIcon(icon)
        layout.addWidget(button)
        layout.addStretch(1)

        button.clicked.connect(self.__clicked)

    def __clicked(self):
        # node = self.node
        event = {"event": "qspace"}
        self.notifyView(event)


@H5NodeClassDef(
    "IntensityGroupNode", attribute=("XsocsClass", "IntensityGroup"), icons="math-sigma"
)
class IntensityGroupNode(H5GroupNode):
    editors = ScatterPlotButton

    def __init__(self, *args, **kwargs):
        super(IntensityGroupNode, self).__init__(*args, **kwargs)

        self.__viewWidget = None

    def getView(self, parent=None):
        """
        Returns a IntensityView for this item's data.
        :param parent:
        :return:
        """

        view = self.__viewWidget
        if view is None or view() is None or not inspect.isValid(view()):
            iGroup = IntensityGroup(self.h5File, nodePath=self.h5Path)
            view = weakref.ref(IntensityView(iGroup, parent))
            self.__viewWidget = view
        return view()

    def _loadChildren(self):
        return []


@H5NodeClassDef("IntensityNode", attribute=("XsocsClass", "IntensityItem"))
class IntensityNode(H5DatasetNode):
    # editors = ScatterPlotButton

    def _setupNode(self):
        with IntensityItem(self.h5File, self.h5Path, mode="r") as item:
            self._setDataInternal(
                ModelColumns.NameColumn,
                str(item.projectRoot().shortName(item.entry)),
                Qt.Qt.DisplayRole,
            )


class QSpaceInfoNode(Node):
    """
    Simple node displaying the qspace conversion parameters.
    """

    recurseDeletion = False
    icons = Qt.QStyle.SP_FileDialogInfoView

    def _loadChildren(self):
        # This node is created by a QSpaceItemNode, which is a H5Node
        # and H5Node have themselves as subject, and the groupClasses
        # inherit their parent's subject.
        qspaceNode = self.subject
        qspaceItem = ProjectItem(qspaceNode.h5File, qspaceNode.h5Path).cast()

        qspaceFile = qspaceItem.qspaceFile
        node = Node(nodeName="Filename")
        node._setDataInternal(ModelColumns.ValueColumn, os.path.basename(qspaceFile))
        node._setDataInternal(
            ModelColumns.NameColumn, qspaceFile, role=Qt.Qt.ToolTipRole
        )
        node._setDataInternal(
            ModelColumns.ValueColumn, qspaceFile, role=Qt.Qt.ToolTipRole
        )
        dirNode = Node(nodeName="Directory")
        dirNode._setDataInternal(ModelColumns.ValueColumn, os.path.dirname(qspaceFile))
        node.appendChild(dirNode)
        children = [node]

        if not isinstance(qspaceItem, QSpaceItem):
            node = Node(nodeName="Error, invalid file.")
            icon = (
                Qt.QApplication.instance()
                .style()
                .standardIcon(Qt.QStyle.SP_MessageBoxCritical)
            )
            node._setDataInternal(0, icon, Qt.Qt.DecorationRole)
            children.append(node)
            return children

        qspaceH5 = qspaceItem.qspaceH5

        ##################################################
        # Adding selected/discarded entries.
        ##################################################

        selected = qspaceH5.selected_entries
        discarded = qspaceH5.discarded_entries

        # support for previous versions.
        # TODO : remove sometimes...
        if selected is None or len(selected) == 0:
            selected = qspaceItem.projectRoot().xsocsH5.entries()
        if discarded is None:
            discarded = []

        nSelected = len(selected)
        nDiscarded = len(discarded)

        selectedList = Node(nodeName="Selected entries")
        selectedList._setDataInternal(
            0, "Entries used for the conversion.", role=Qt.Qt.ToolTipRole
        )
        selectedList._setDataInternal(ModelColumns.ValueColumn, "{0}".format(nSelected))
        for entry in selected:
            node = Node(nodeName=entry)
            selectedList.appendChild(node)
        children.append(selectedList)

        discardedList = Node(nodeName="Discarded entries")
        discardedList._setDataInternal(
            0, "Discarded input entries.", role=Qt.Qt.ToolTipRole
        )
        discardedList._setDataInternal(
            ModelColumns.ValueColumn, "{0}".format(nDiscarded)
        )
        for entry in discarded:
            node = Node(nodeName=entry)
            discardedList.appendChild(node)
        children.append(discardedList)

        ##################################################
        # Adding shift info
        ##################################################

        shifts = qspaceH5.shifts

        shiftNode = Node(nodeName="Shift")

        if shifts is None:
            shiftNode.setData(ModelColumns.ValueColumn, "No.", role=Qt.Qt.DisplayRole)
        else:
            shiftNode.setData(ModelColumns.ValueColumn, "Yes.", role=Qt.Qt.DisplayRole)
            style = Qt.QApplication.instance().style()
            icon = style.standardIcon(Qt.QStyle.SP_MessageBoxWarning)
            shiftNode.setData(ModelColumns.ValueColumn, icon, role=Qt.Qt.DecorationRole)

            for entry in selected:
                eShiftNode = Node(nodeName=entry)
                shift = shifts[entry]
                sampleShift = shift["shift"]
                gridShift = shift["grid_shift"]

                text = ""
                if sampleShift is not None:
                    text = "sample:[{0:6g}, {1:6g}]".format(*sampleShift)
                if gridShift is not None:
                    if text:
                        text += ", "
                    text += "grid:{0}".format(gridShift)

                if not text:
                    text = "unknown"

                eShiftNode.setData(
                    ModelColumns.ValueColumn, text, role=Qt.Qt.DisplayRole
                )
                shiftNode.appendChild(eShiftNode)

        children.append(shiftNode)

        ##################################################
        # Add acquisition parameters
        ##################################################

        node = Node(nodeName="Beam energy")
        beamEnergy = qspaceH5.beam_energy
        # support for previous versions
        text = "N/A" if beamEnergy is None else "{0}".format(beamEnergy)
        node._setDataInternal(ModelColumns.ValueColumn, text)
        children.append(node)

        for name, value in (
            ("Center channels", qspaceH5.direct_beam),
            ("Channels/degree", qspaceH5.channels_per_degree),
        ):
            node = Node(nodeName=name)
            # support for previous versions
            text = "N/A" if value is None else "{0}, {1}".format(*value)
            node._setDataInternal(ModelColumns.ValueColumn, text)
            children.append(node)

        ##################################################
        # Adding ROI info
        ##################################################

        sampleRoi = qspaceH5.sample_roi
        toolTip = """<ul>
                    <li>xMin : {0:.7g}
                    <li>xMax : {1:.7g}
                    <li>yMin : {2:.7g}
                    <li>yMax : {3:.7g}
                    </ul>
                  """.format(
            *sampleRoi
        )
        roiNode = Node(nodeName="Roi")
        text = "{0:6g}, {1:6g}, {2:6g}, {3:6g}".format(*sampleRoi)
        roiNode._setDataInternal(ModelColumns.ValueColumn, text)
        roiNode._setDataInternal(ModelColumns.NameColumn, toolTip, Qt.Qt.ToolTipRole)
        node = Node(nodeName="xMin")
        node._setDataInternal(ModelColumns.ValueColumn, "{0:.7g}".format(sampleRoi[0]))
        roiNode.appendChild(node)
        node = Node(nodeName="xMax")
        node._setDataInternal(ModelColumns.ValueColumn, "{0:.7g}".format(sampleRoi[1]))
        roiNode.appendChild(node)
        node = Node(nodeName="yMin")
        node._setDataInternal(ModelColumns.ValueColumn, "{0:.7g}".format(sampleRoi[2]))
        roiNode.appendChild(node)
        node = Node(nodeName="yMax")
        node._setDataInternal(ModelColumns.ValueColumn, "{0:.7g}".format(sampleRoi[3]))
        roiNode.appendChild(node)

        children.append(roiNode)

        ##################################################
        # Adding maxipix correction
        ##################################################
        node = Node(nodeName="Maxipix correction")
        node._setDataInternal(
            ModelColumns.ValueColumn,
            "Enabled" if qspaceH5.maxipix_correction else "Disabled",
        )
        children.append(node)

        ##################################################
        # Adding image normalization.
        ##################################################
        node = Node(nodeName="Normalization")
        imageNormalizer = qspaceH5.image_normalizer
        # No normalization (also support previous versions)
        if not imageNormalizer:
            imageNormalizer = "None"
        node._setDataInternal(ModelColumns.ValueColumn, imageNormalizer)
        children.append(node)

        ##################################################
        # Adding image binning if available (deprecated)
        ##################################################
        imageBinning = qspaceH5.image_binning
        # support for previous versions
        if imageBinning is not None:
            node = Node(nodeName="Image binning")
            text = "{0}x{1}".format(*imageBinning)
            node._setDataInternal(ModelColumns.ValueColumn, text)
            children.append(node)

        ##################################################
        # Adding medfilt.
        ##################################################
        node = Node(nodeName="Median filter")
        medfiltDims = qspaceH5.medfilt_dims
        # support for previous versions
        # TODO : remove eventualy
        if medfiltDims is None:
            text = "unavailable (3x3?)"
        else:
            text = "{0}x{1}".format(*medfiltDims)
        node._setDataInternal(ModelColumns.ValueColumn, text)
        children.append(node)

        ##################################################
        # Adding qspace dims.
        ##################################################
        qspaceDimsNode = Node(nodeName="Qspace size")
        text = "{0}x{1}x{2} ({3}, {4}, {5})".format(
            *(qspaceH5.qspace_dimensions + qspaceH5.qspace_dimension_names)
        )
        qspaceDimsNode._setDataInternal(ModelColumns.ValueColumn, text)
        children.append(qspaceDimsNode)

        return children


@H5NodeClassDef("QSpaceItem", attribute=("XsocsClass", "QSpaceItem"))
class QSpaceItemNode(ProjectNode):
    editors = QSpaceButton
    groupClasses = [("Infos", QSpaceInfoNode)]
    editableColumns = [True]
    deletable = True

    def __init__(self, *args, **kwargs):
        super(QSpaceItemNode, self).__init__(*args, **kwargs)
        self.__viewWidget = None

        projectItem = self.getProjectItem()

        try:
            qspaceFile = projectItem.qspaceFile
            valid = os.path.exists(qspaceFile)
            if not valid:
                self._setIsValid(valid, errorMsg="File not found.")
        except Exception as ex:
            self._setIsValid(False, errorMsg=str(ex))

    def getQMenu(self, view, qMenu=None, persistentIndex=None):
        """
        Adds :
        - "show folder"
        - "copy file name"
        - "rename item"
        :return:
        """
        qMenu = super(QSpaceItemNode, self).getQMenu(
            view, qMenu=qMenu, persistentIndex=persistentIndex
        )

        if not qMenu:
            qMenu = Qt.QMenu()

        qMenu.addAction("Show folder").triggered.connect(
            lambda checked: Qt.QDesktopServices.openUrl(
                Qt.QUrl.fromLocalFile(os.path.dirname(self.h5File))
            )
        )

        qMenu.addAction("Copy file name").triggered.connect(
            lambda checked: Qt.QApplication.instance()
            .clipboard()
            .setText(os.path.abspath(self.getProjectItem().qspaceFile))
        )

        if persistentIndex is not None and persistentIndex.isValid():
            qMenu.addAction("Rename item").triggered.connect(
                lambda checked: view.edit(
                    view.model().index(
                        persistentIndex.row(),
                        persistentIndex.column(),
                        persistentIndex.parent(),
                    )
                )
            )

        if persistentIndex is not None and persistentIndex.isValid():
            qMenu.addAction("Delete item").triggered.connect(
                lambda checked: self.delete(view)
            )

        return qMenu

    def getView(self, parent=None):
        """
        Returns a QSpaceView for this item's data.
        :param parent:
        :return:
        """
        view = self.__viewWidget
        if view is None or view() is None or not inspect.isValid(view()):
            qItem = QSpaceItem(self.h5File, nodePath=self.h5Path)
            view = weakref.ref(QSpaceView(qItem, parent=parent))
            self.__viewWidget = view
        return view()

    def _loadChildren(self):
        # dirty hack to remove a legacy group from appearing in the tree
        # TODO : to be removed eventualy
        if not self.isValid():
            return []

        children = super(QSpaceItemNode, self)._loadChildren()
        filtered = [
            child for child in children if os.path.basename(child.h5Path) != "info"
        ]
        return filtered

    def _tryDelete(self, *args, **kwargs):
        """
        Calls the super class _tryDelete and forces the recursion to
        the FitGroup node only.
        :param widget:
        :param confirm:
        :param force:
        :return:
        """
        deleteReply = super(QSpaceItemNode, self)._tryDelete(*args, **kwargs)
        deleteReply.childClasses.append(FitGroupNode)
        return deleteReply

    def _doDelete(self):
        """
        Deletes this QSpaceItem from the project file.
        :return:
        """
        projectItem = self.getProjectItem()

        if projectItem:
            qspaceFile = projectItem.qspaceFile
        else:
            qspaceFile = None

        if qspaceFile:
            try:
                os.remove(qspaceFile)
            except OSError as ex:
                Qt.QMessageBox.warning(
                    None, "Error.", "Failed to remove file.\n" "{0}".format(ex)
                )
                return os.path.exists(qspaceFile)

        try:
            with h5py.File(projectItem.filename, mode="a") as h5f:
                del h5f[self.h5Path]
        except KeyError:
            pass

        return True


class FitButton(EditorMixin, Qt.QWidget):
    persistent = True

    sigValueChanged = Qt.Signal()

    def __init__(self, parent, option, index):
        super(FitButton, self).__init__(parent, option, index)
        layout = Qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        icon = icons.getQIcon("plot-widget")
        button = Qt.QToolButton()
        button.setIcon(icon)
        button.clicked.connect(self.__clicked)
        layout.addWidget(button)

        button = Qt.QToolButton()
        style = Qt.QApplication.style()
        icon = style.standardIcon(Qt.QStyle.SP_DialogSaveButton)
        button.setIcon(icon)
        button.clicked.connect(self.__export)
        layout.addWidget(button)
        layout.addStretch(1)

    def __clicked(self):
        event = {"event": "fit"}
        self.notifyView(event)

    def __export(self):
        fitItem = h5NodeToProjectItem(self.node)
        workdir = fitItem.projectRoot().workdir
        itemBasename = os.path.basename(fitItem.fitFile).rsplit(".")[0]
        itemBasename += ".txt"
        dialog = Qt.QFileDialog(self, "Export fit results.")
        dialog.setFileMode(Qt.QFileDialog.AnyFile)
        dialog.setAcceptMode(Qt.QFileDialog.AcceptSave)
        dialog.selectFile(os.path.join(workdir, itemBasename))
        if dialog.exec_():
            csvPath = dialog.selectedFiles()[0]
            fitItem.fitH5.export_csv(fitItem.fitH5.entries()[0], csvPath)


@H5NodeClassDef("FitGroup", attribute=("XsocsClass", "FitGroup"), icons="math-fit")
class FitGroupNode(H5GroupNode):
    def _tryDelete(self, *args, **kwargs):
        """
        Calls the super class _tryDelete and forces the recursion to
        the FitItem nodes only.
        :param widget:
        :param confirm:
        :param force:
        :return:
        """
        deleteReply = super(FitGroupNode, self)._tryDelete(*args, **kwargs)
        deleteReply.childClasses.append(FitItemNode)
        return deleteReply


@H5NodeClassDef("FitItem", attribute=("XsocsClass", "FitItem"), icons="math-fit")
class FitItemNode(ProjectNode):
    editors = FitButton
    deletable = True
    recurseDeletion = False
    editableColumns = [True]

    def _loadChildren(self):
        return []

    def __init__(self, *args, **kwargs):
        super(FitItemNode, self).__init__(*args, **kwargs)
        self.__viewWidget = None

    def getView(self, parent=None):
        """
        Returns a FitView for this item's data.
        :param parent:
        :return:
        """
        view = self.__viewWidget
        if view is None or view() is None or not inspect.isValid(view()):
            fitItem = FitItem(self.h5File, nodePath=self.h5Path)
            view = weakref.ref(FitView(parent, fitItem))
            self.__viewWidget = view
        return view()

    def _doDelete(self):
        """
        Deletes this FitItem from the project.
        :return:
        """

        projectItem = self.getProjectItem()

        if projectItem:
            fitFile = projectItem.fitFile
        else:
            fitFile = None

        if fitFile:
            try:
                os.remove(fitFile)
            except OSError as ex:
                Qt.QMessageBox.warning(
                    None, "Error.", "Failed to remove file.\n" "{0}".format(ex)
                )
                return os.path.exists(fitFile)

        try:
            with h5py.File(projectItem.filename, mode="a") as h5f:
                del h5f[self.h5Path]
        except KeyError:
            pass

        return True

    def getQMenu(self, view, qMenu=None, persistentIndex=None):
        """
        Adds :
        - "show folder"
        - "copy file name"
        - "rename item"
        :return:
        """
        qMenu = super(FitItemNode, self).getQMenu(
            view, qMenu=qMenu, persistentIndex=persistentIndex
        )

        if not qMenu:
            qMenu = Qt.QMenu()

        qMenu.addAction("Show folder").triggered.connect(
            lambda checked: Qt.QDesktopServices.openUrl(
                Qt.QUrl.fromLocalFile(os.path.dirname(self.h5File))
            )
        )

        qMenu.addAction("Copy file name").triggered.connect(
            lambda checked: Qt.QApplication.instance()
            .clipboard()
            .setText(os.path.abspath(self.getProjectItem().qspaceFile))
        )

        if persistentIndex is not None and persistentIndex.isValid():
            qMenu.addAction("Rename item").triggered.connect(
                lambda checked: view.edit(
                    view.model().index(
                        persistentIndex.row(),
                        persistentIndex.column(),
                        persistentIndex.parent(),
                    )
                )
            )

        if persistentIndex is not None and persistentIndex.isValid():
            qMenu.addAction("Delete item").triggered.connect(
                lambda checked: self.delete(view)
            )

        return qMenu
