import numpy as np

from silx.gui import qt as Qt


from .ShiftSubject import ShiftSubject

from ...view.intensity.RectRoiWidget import RectRoiWidget

from ...widgets.Containers import GroupBox
from ...widgets.XsocsPlot2D import XsocsPlot2D
from ...widgets.PlotGrabber import PlotGrabber

from ...model.Node import Node, ModelDataList
from ...model.TreeView import TreeView
from ...model.Model import Model, RootNode
from ...model.ModelDef import ModelRoles, ModelColumns


class ShiftRootNode(RootNode):
    """Root node for the ShiftModel"""

    ColumnNames = ["Scan", "Preview"]


class ShiftModel(Model):
    """Model displaying a FitH5 file contents."""

    RootNode = ShiftRootNode
    ColumnsWithDelegates = [1]


class ShiftListNode(Node):
    """Root node for a list of entries"""

    def _loadChildren(self):
        iGroup = self.subject.getIntensityGroup()
        return [
            ShiftNode(
                iGroup.getIntensityItem(entry),
                branchName=entry,
                nodeName=entry,
                subject=self.subject,
            )
            for entry in iGroup.xsocsH5.entries()
        ]


class ShiftNode(Node):
    def sizeHint(self, column):
        if column == 1:
            return Qt.QSize(150, 150)
        return super(ShiftNode, self).sizeHint(column)

    def __init__(self, iItem, **kwargs):
        super(ShiftNode, self).__init__(**kwargs)

        self.__item = iItem

        self._setDataInternal(
            ModelColumns.ValueColumn, self.sizeHint(0), role=Qt.Qt.SizeHintRole
        )

    def getShift(self):
        """Returns the shift values for this node."""
        return self.subject.getShift(self.branchName)

    def getControlPoint(self):
        """
        Returns the coordinates of the selected point, with this node's shift
        applied, or None if the selected point has not been set.
        """
        refPoint = self.subject.getReferenceControlPoint()

        if refPoint is None:
            return None

        thisPoint = np.array([refPoint["x"], refPoint["y"]])

        if refPoint["entry"] != self.getEntry():
            shift = self.getShift()
            refShift = self.subject.getShift(refPoint["entry"])
            thisPoint += [shift.dx - refShift.dx, shift.dy - refShift.dy]

        return thisPoint

    def getEntry(self):
        """Returns this node's entry."""
        return self.branchName

    def getRoiData(self, shifted=True, centered=False):
        """Returns this node's intensity data inside the ROI.

        :param shifted: True to apply shift to the ROI.
        :param centered: True to return a ROI with the same shape
            but centered on the selected point.
        """
        # TODO : cache the values
        roiData = self.subject.getRoiData(
            self.branchName, shifted=shifted, centered=centered
        )
        return roiData

    def getFullData(self):
        """Returns this node's intensity data."""
        # TODO : cache the values
        fullData = self.subject.getFullData(self.branchName)
        return fullData

    def subjectSignals(self, column):
        if column == ModelColumns.ValueColumn:
            return [
                self.subject.sigRoiChanged,
                self.subject.sigReferenceControlPointChanged,
                self.subject.sigShiftChanged,
                self.subject.sigDataChanged,
            ]
        return []

    def filterEvent(self, column, event):
        if column == ModelColumns.ValueColumn:
            accept = True
            if event:
                if event.signalId == 2 and event.args:
                    accept = event.args[0].entry == self.branchName
            return accept, event
        return super(ShiftNode, self).filterEvent(column, event)

    def pullModelData(self, column, event=None, force=False):
        # TODO : error checking
        self._setIsDirty(True)
        return ModelDataList(None, forceNotify=True)

    def _drawNode(self):
        """Draws this node's thumbnail."""
        rc = super(ShiftNode, self)._drawNode()

        plot = PlotGrabber()
        plot.setFixedSize(Qt.QSize(150, 150))

        # WARNING, DO NOT REMOVE
        # on some systems this is necessary, otherwise the widget is not
        # resized
        # ============
        plot.toPixmap()
        # ============
        # WARNING END

        roiData = self.getRoiData(shifted=True, centered=True)

        if roiData is not None:
            origin = self.subject.getReferenceControlPoint()
            shift = self.subject.getShift(self.branchName)
            plot.selectPoint(origin["x"] + shift.dx, origin["y"] + shift.dy)

            plot.setPlotData(x=roiData.x, y=roiData.y, values=roiData.z)

            plot.replot()

        self._setDataInternal(1, plot.toPixmap(), Qt.Qt.DecorationRole, notify=True)

        return rc


class ShiftSelectorPanel(Qt.QWidget):
    sigSelectionChanged = Qt.Signal(object)

    def __init__(self, shiftSubject, parent=None):
        super(ShiftSelectorPanel, self).__init__(parent)

        layout = Qt.QGridLayout(self)

        self.__tree = ShiftTree(shiftSubject)
        self.__cBox = Qt.QComboBox()
        self.__refreshBn = Qt.QPushButton()
        self.__autoRefreshCb = Qt.QCheckBox("Auto refresh")
        app = Qt.QApplication.instance()
        style = app.style()
        icon = style.standardIcon(Qt.QStyle.SP_BrowserReload)
        self.__refreshBn.setIcon(icon)

        self.__cBox.setModel(self.__tree.model())
        self.__cBox.setRootModelIndex(self.__tree.rootIndex())
        self.__cBox.setCurrentIndex(0)

        bnLayout = Qt.QHBoxLayout()
        bnLayout.addWidget(self.__cBox)
        bnLayout.addWidget(self.__refreshBn)
        bnLayout.addWidget(self.__autoRefreshCb)

        layout.addLayout(bnLayout, 0, 0, Qt.Qt.AlignCenter)
        layout.addWidget(self.__tree, 1, 0)

        self.__tree.sigCurrentChanged.connect(self.__notifySelectionChanged)
        self.__cBox.currentIndexChanged[int].connect(self.__slotIndexChanged)

        shiftSubject.sigShiftChanged.connect(self.__slotSubjectChanged)
        shiftSubject.sigRoiChanged.connect(self.__slotSubjectChanged)
        shiftSubject.sigReferenceControlPointChanged.connect(self.__slotSubjectChanged)
        shiftSubject.sigDataChanged.connect(self.__slotSubjectChanged)

        self.__refreshBn.clicked.connect(self.__slotRefreshClicked)

        self.__autoRefreshCb.setChecked(not self.__tree.isAutoRefresh())

        self.__autoRefreshCb.clicked.connect(self.__slotAutoRefreshClicked)

    def __slotAutoRefreshClicked(self, checked):
        """Slot called when the auto refresh button is unchecked/checked

        :param checked:
        """
        self.__tree.setAutoRefresh(not checked)
        if checked:
            self.__tree.drawDelayedItems()

    def __slotSubjectChanged(self):
        """Called when the state of the subject changes."""
        self.__refreshBn.setEnabled(True)

    def __slotRefreshClicked(self):
        """Called when the refresh button is clicked"""
        self.__tree.drawDelayedItems()

    def __slotIndexChanged(self, index):
        """Slot called when the index of the combox box changes

        :param index:
        """
        mIndex = self.__cBox.rootModelIndex().child(index, 0)
        self.__tree.selectionModel().setCurrentIndex(
            mIndex, Qt.QItemSelectionModel.ClearAndSelect
        )

    def __notifySelectionChanged(self, node=None):
        """Emits the signal sigSelectionChanged

        :param node:
        """
        if node is None:
            index = self.__tree.selectionModel().currentIndex()
            node = index.data(role=ModelRoles.InternalDataRole)

        if node is None:
            # this shouldnt happen ever
            raise ValueError("Node is none")

        self.sigSelectionChanged.emit(node)

    def treeView(self):
        """Returns the TreeView

        :rtype: QTreeView
        """
        return self.__tree

    def comboBox(self):
        """Returns the QComboBox

        :rtype: QComboBox
        """
        return self.__cBox


class ShiftPlotWidget(Qt.QWidget):
    sigSelectionChanged = Qt.Signal(object)
    """Signal emitted when the current selected entry changes"""

    sigPointSelected = Qt.Signal(object, object)
    """Signal emitted when a point is selected on the plot
       Parameters are node and selected coordinates XsocsPlot2DPoint"""

    def __init__(
        self, shiftModel, rootIndex, applyRoi=False, showSelection=False, parent=None
    ):
        """A widget containing a Plot and a combobox for entry selection.

        :param shiftModel: The shiftModel to use.
        :param rootIndex: The root index for the combobox.
        :param applyRoi: True to apply the ROI to the displayed data.
        :param showSelection: True to display the selected point (crosshair).
        :param parent:
        """
        super(ShiftPlotWidget, self).__init__(parent)

        layout = Qt.QGridLayout(self)

        self.__cBox = Qt.QComboBox()
        self.__entryLocked = False

        self.__applyRoi = applyRoi
        self.__showSelection = showSelection

        self.__cBox.setModel(shiftModel)
        self.__cBox.setRootModelIndex(rootIndex)
        self.__cBox.setCurrentIndex(0)

        layout.addWidget(self.__cBox, 0, 0, Qt.Qt.AlignCenter)

        self.__plot = XsocsPlot2D()
        self.__plot.setSnapToPoint(True)
        self.__plot.setPointSelectionEnabled(True)

        layout.addWidget(self.__plot, 1, 0, Qt.Qt.AlignCenter)

        self.__cBox.currentIndexChanged[int].connect(self.__slotIndexChanged)
        self.__plot.sigPointSelected.connect(self.__slotPointSelected)

        self.__cBox.setCurrentIndex(0)
        self.__cBox.currentIndexChanged.emit(0)

    def lockEntry(self, lock):
        """Locks the entry selector to the current entry.

        :param lock:
        """
        self.__entryLocked = lock
        self.__cBox.setEnabled(not lock)

    def __slotPointSelected(self, point):
        """Slot called when a point is selected on the plot.

        :param point:
        """
        node = self.__getCurrentNode()
        self.sigPointSelected.emit(node, point)

    def plot(self):
        """Returns the plot widget.

        :rtype: PlotWidget
        """
        return self.__plot

    def setSnapToPoint(self, snap):
        """Set the snapToPoint flag of the plot.

        :param snap:
        """
        self.__plot.setSnapToPoint(snap)

    def __slotIndexChanged(self, index):
        """Slot called when the index of the combox box changes

        :param index:
        """
        mIndex = self.__cBox.rootModelIndex().child(index, 0)
        node = mIndex.data(role=ModelRoles.InternalDataRole)

        if node is None:
            # this shouldnt happen ever
            raise ValueError("Node is none")

        self.setCurrentModelIndex(mIndex)

        self.sigSelectionChanged.emit(node)

    def comboBox(self):
        """Returns the QComboBox

        :rtype: QComboBox
        """
        return self.__cBox

    def getCurrentEntry(self):
        """Returns the current selected entry."""
        node = self.__getCurrentNode()
        return node.branchName

    def setCurrentModelIndex(self, mdlIndex):
        """
        Sets the current displayed node to the one referenced by the given
        QModelIndex (shiftModel index).

        :param mdlIndex:
        """
        self.__plot.clear()

        if not mdlIndex.isValid():
            raise ValueError("Invalid index.")

        node = mdlIndex.data(ModelRoles.InternalDataRole)

        self.__cBox.setCurrentIndex(mdlIndex.row())

        self.__drawPlotData(node)
        self.__drawSelectedPoint(node)

    def __getCurrentNode(self):
        mIndex = self.__cBox.rootModelIndex().child(self.__cBox.currentIndex(), 0)
        node = mIndex.data(role=ModelRoles.InternalDataRole)

        if node is None:
            # this shouldnt happen ever
            raise ValueError("Node is none")

        return node

    def __drawPlotData(self, node=None):
        """Draws the scatter plot"""
        if node is None:
            node = self.__getCurrentNode()

        if self.__applyRoi:
            roiData = node.getRoiData(shifted=False)
        else:
            roiData = node.getFullData()

        if roiData is not None:
            self.__plot.setPlotData(
                roiData.x, roiData.y, roiData.z, dataIndices=roiData.idx
            )

    def __drawSelectedPoint(self, node=None):
        """Draws the selected point crosshair"""
        if not self.__showSelection:
            return

        if node is None:
            node = self.__getCurrentNode()

        selectedPt = node.getControlPoint()
        if selectedPt is not None:
            self.__plot.selectPoint(*selectedPt)

    def refreshPlotData(self):
        """Redraws the plot data"""
        self.__drawPlotData()

    def refreshSelectedPoint(self):
        """Redraws the selected point crosshair"""
        self.__drawSelectedPoint()


class ShiftTree(TreeView):
    sigCurrentChanged = Qt.Signal(object)

    def __init__(self, shiftSubject, **kwargs):
        super(ShiftTree, self).__init__(**kwargs)

        shiftList = ShiftListNode(subject=shiftSubject)
        model = ShiftModel()
        model.appendGroup(shiftList)
        self.setModel(model)
        self.setShowUniqueGroup(True)
        self.setRootIndex(shiftList.index())
        model.startModel()

    def currentChanged(self, current, previous):
        super(ShiftTree, self).currentChanged(current, previous)
        node = current.data(ModelRoles.InternalDataRole)
        if not node:
            return
        self.sigCurrentChanged.emit(node)


class ShiftAreaSelectorWidget(Qt.QWidget):
    """A ShiftPlotWidget + a roi widget."""

    sigRoiApplied = Qt.Signal(object, object)
    """Triggered when the ROI is applied.

    Args are : the roi, and the node on which the ROI was applied.
    """

    def __init__(self, shiftModel, rootIndex, **kwargs):
        super(ShiftAreaSelectorWidget, self).__init__(**kwargs)

        layout = Qt.QGridLayout(self)

        self.__firstShow = True

        self.__plotWid = ShiftPlotWidget(shiftModel, rootIndex)
        self.__plotWid.plot().setPointSelectionEnabled(False)
        self.__roiWidget = RectRoiWidget(plot=self.__plotWid.plot())
        self.__roiWidget.applyButton().setText("View selection")

        layout.addWidget(self.__plotWid, 0, 0)
        layout.addWidget(self.__roiWidget, 1, 0, Qt.Qt.AlignTop | Qt.Qt.AlignCenter)

        self.__plotWid.sigSelectionChanged.connect(self.__slotSelectionChanged)
        self.__roiWidget.sigRoiApplied.connect(self.__slotRoiApplied)

        self.__plotWid.comboBox().setCurrentIndex(0)
        self.__plotWid.comboBox().currentIndexChanged.emit(0)

    def shiftPlotWidget(self):
        """Returns ShiftPlotWidget used within this widget

        :rtype: ShiftPlotWidget
        """
        return self.__plotWid

    def __slotSelectionChanged(self, node):
        """
        Slot Called when the selection changes in the ShitPlotWidget combobox.

        :param node:
        """
        if not node:  # this should not happen ever
            raise ValueError("node is None")

        plotData = node.getFullData()

        self.__plotWid.plot().setPlotData(plotData.x, plotData.y, values=plotData.z)

        self.__roiWidget.roiManager().showRois(True)

    def showEvent(self, event):
        super(ShiftAreaSelectorWidget, self).showEvent(event)
        if self.__firstShow:
            self.__firstShow = False
            self.__plotWid.plot().resetZoom()

    def __slotRoiApplied(self, roi):
        """Slot called when the ROI is applied.

        Emits ShiftAreaSelectorWidget.sigRoiApplied

        :param roi:
        """
        cbox = self.__plotWid.comboBox()
        mIndex = cbox.rootModelIndex().child(cbox.currentIndex(), 0)

        if not mIndex.isValid():
            # THIS SHOULD NEVER HAPPEN
            raise ValueError("Invalid index")

        node = mIndex.data(ModelRoles.InternalDataRole)

        self.sigRoiApplied.emit(roi, node)


class ShiftPreviewPanel(Qt.QWidget):
    def __init__(self, shiftSubject, parent=None, **kwargs):
        super(ShiftPreviewPanel, self).__init__(parent, **kwargs)

        self.__subject = shiftSubject

        layout = Qt.QGridLayout(self)

        self.__snapToGrid = True

        self.__refreshBn = Qt.QPushButton("Refresh")
        app = Qt.QApplication.instance()
        style = app.style()
        icon = style.standardIcon(Qt.QStyle.SP_BrowserReload)
        self.__refreshBn.setIcon(icon)

        self.__progBar = Qt.QProgressBar()

        self.__plot = XsocsPlot2D()

        layout.addWidget(self.__refreshBn, 0, 0, Qt.Qt.AlignCenter)
        layout.addWidget(self.__progBar, 0, 1, Qt.Qt.AlignCenter)
        layout.addWidget(self.__plot, 2, 0, 1, 2)

        shiftSubject.sigShiftChanged.connect(self.__slotShiftChanged)
        self.__refreshBn.clicked.connect(self.__slotRefreshClicked)

    def setSnapToGrid(self, snap):
        """Sets the snapToGrid to True (called by ShiftView when checking
        the regular grid) checkbox.

        :param snap:
        """
        if snap != self.__snapToGrid:
            self.__snapToGrid = snap
            self.__slotShiftChanged()

    def __slotShiftChanged(self):
        """Called when a shift value changes.

        Notifies the user that a refresh is needed.
        """
        self.__plot.clear()
        self.__plot.setGraphTitle("")
        self.__progBar.setValue(0)
        self.__refreshBn.setEnabled(True)

    def __slotRefreshClicked(self):
        """Called when the refresh button is clicked"""
        intersectionPoints = self.__subject.getIntersectionIndices(
            grid=self.__snapToGrid, progressCb=self.__progBar.setValue
        )
        self.__refreshBn.setEnabled(False)

        self.__plot.clear()
        self.__plot.setGraphTitle("")

        if intersectionPoints is None or intersectionPoints.size == 0:
            return

        iGroup = self.__subject.getIntensityGroup()

        # Get positions
        scanPositions = iGroup.getIntensityItem("Total").getScatterData()[1]

        # Compute intensity with current shift
        scanShift = self.__subject.scanShift()
        intensity = np.zeros(intersectionPoints.shape, dtype=np.float64)
        for entry in self.__subject.getShiftEntries():
            item = iGroup.getIntensityItem(entry)
            entryIntensity = item.getScatterData()[0]
            indices = scanShift.get_entry_intersection_indices(entry)
            intensity += entryIntensity[indices]

        self.__plot.setPlotData(
            scanPositions.pos_0[intersectionPoints],
            scanPositions.pos_1[intersectionPoints],
            values=intensity,
        )

        title = "Intensity (Points: {0}/{1})".format(
            intersectionPoints.size, scanPositions.pos_0.size
        )
        self.__plot.setGraphTitle(title)


class ShiftWidget(Qt.QMainWindow):
    """
    Window allowing a user to display/set the shift
    (sample holder displacement).
    """

    def __init__(self, intensityGroup, shiftItem, parent=None, **kwargs):
        super(ShiftWidget, self).__init__(parent, **kwargs)

        self.setWindowTitle(
            "[XSOCS] Shift {0}:{1}".format(intensityGroup.filename, intensityGroup.path)
        )

        centralWidget = Qt.QWidget()
        centralLayout = Qt.QGridLayout(centralWidget)
        self.setCentralWidget(centralWidget)

        self.__shiftSubject = ShiftSubject(intensityGroup, shiftItem)

        # Preview panel
        self.__selector = ShiftSelectorPanel(self.__shiftSubject)
        selSubGroup = GroupBox("Preview")
        layout = Qt.QVBoxLayout(selSubGroup)
        layout.addWidget(self.__selector)

        treeView = self.__selector.treeView()

        # Point preview
        self.__previewPanel = ShiftPreviewPanel(shiftSubject=self.__shiftSubject)
        pointsSubGroup = GroupBox("Intensity")
        layout = Qt.QVBoxLayout(pointsSubGroup)
        layout.addWidget(self.__previewPanel)

        entriesDock = Qt.QDockWidget("Entries", self)
        entriesDock.setWidget(selSubGroup)
        features = entriesDock.features() ^ Qt.QDockWidget.DockWidgetClosable
        entriesDock.setFeatures(features)
        self.addDockWidget(Qt.Qt.RightDockWidgetArea, entriesDock)

        pointsDock = Qt.QDockWidget("Intensity", self)
        pointsDock.setWidget(pointsSubGroup)
        features = pointsDock.features() ^ Qt.QDockWidget.DockWidgetClosable
        pointsDock.setFeatures(features)
        self.tabifyDockWidget(entriesDock, pointsDock)
        entriesDock.setTitleBarWidget(Qt.QWidget())
        pointsDock.setTitleBarWidget(Qt.QWidget())
        entriesDock.raise_()

        self.setTabPosition(Qt.Qt.AllDockWidgetAreas, Qt.QTabWidget.North)

        # "Ref" panel
        self.__refPanel = ShiftPlotWidget(
            treeView.model(), treeView.rootIndex(), applyRoi=True, showSelection=True
        )
        self.__refPanel.setSnapToPoint(True)
        self.__refPanel.lockEntry(True)
        refSubGroup = GroupBox("Reference")
        layout = Qt.QVBoxLayout(refSubGroup)
        layout.addWidget(self.__refPanel)
        self.__refPanel.plot().setPointSelectionEnabled(True)
        self.__shiftSubject.sigDataChanged.connect(self.__refPanel.refreshPlotData)

        # "Set" panel
        self.__setPanel = ShiftPlotWidget(
            treeView.model(), treeView.rootIndex(), applyRoi=True, showSelection=True
        )
        self.__setPanel.setSnapToPoint(True)
        self.__setPanel.plot().setPointSelectionEnabled(True)
        self.__shiftSubject.sigDataChanged.connect(self.__setPanel.refreshPlotData)

        self.__linearShiftBn = Qt.QPushButton("Apply linear shift")
        self.__linearShiftWholeRangeBn = Qt.QPushButton(
            "Apply linear shift on whole range"
        )
        resetShiftBn = Qt.QPushButton("Reset entry shift")
        resetAllShiftBn = Qt.QPushButton("Reset ALL shifts")
        self.__linearShiftBn.setEnabled(False)
        self.__linearShiftWholeRangeBn.setEnabled(False)

        setSubGroup = GroupBox("Set")
        layout = Qt.QVBoxLayout(setSubGroup)
        layout.addWidget(self.__setPanel)

        bnBase = Qt.QWidget()
        bnBase.setContentsMargins(0, 0, 0, 0)
        bnLayout = Qt.QHBoxLayout(bnBase)
        bnLayout.addWidget(self.__linearShiftBn, alignment=Qt.Qt.AlignCenter)
        bnLayout.addWidget(self.__linearShiftWholeRangeBn, alignment=Qt.Qt.AlignCenter)
        bnLayout.addWidget(resetShiftBn, alignment=Qt.Qt.AlignCenter)
        bnLayout.addWidget(resetAllShiftBn, alignment=Qt.Qt.AlignCenter)
        layout.addWidget(bnBase, alignment=Qt.Qt.AlignCenter)

        # ROI panel
        self.__areaPlot = ShiftAreaSelectorWidget(
            treeView.model(), treeView.rootIndex()
        )
        self.__shiftSubject.sigDataChanged.connect(
            self.__areaPlot.shiftPlotWidget().refreshPlotData
        )
        roiSubGroup = GroupBox("Selection")
        layout = Qt.QVBoxLayout(roiSubGroup)

        # Select displayed value
        dataComboBox = Qt.QComboBox()
        dataComboBox.setToolTip("Select displayed data")
        dataComboBox.addItem("Intensity")
        for name in self.__shiftSubject.xsocsH5().normalizers():
            dataComboBox.addItem(name)
        dataComboBox.currentIndexChanged.connect(self.__dataChanged)

        dataSelectLayout = Qt.QHBoxLayout()
        dataSelectLayout.addStretch(1)
        dataSelectLayout.addWidget(Qt.QLabel("Displayed data:"))
        dataSelectLayout.addWidget(dataComboBox)
        dataSelectLayout.addStretch(1)
        layout.addLayout(dataSelectLayout)

        layout.addWidget(self.__areaPlot)

        # X and Y shift plot
        self.__xShiftPlot = XsocsPlot2D()
        self.__yShiftPlot = XsocsPlot2D()
        self.__xShiftPlot.setGraphXLabel("entry #")
        self.__xShiftPlot.setGraphYLabel("horizontal shift")
        self.__xShiftPlot.setGraphYLabel("column shift", axis="right")
        self.__yShiftPlot.setGraphXLabel("entry #")
        self.__yShiftPlot.setGraphYLabel("vertical shift")
        self.__yShiftPlot.setGraphYLabel("row shift", axis="right")
        self.__xShiftPlot.setKeepDataAspectRatio(False)
        self.__yShiftPlot.setKeepDataAspectRatio(False)
        shiftSubGroup = GroupBox("Shift/Entry")
        layout = Qt.QHBoxLayout(shiftSubGroup)
        layout.addWidget(self.__xShiftPlot)
        layout.addWidget(self.__yShiftPlot)

        buttonsLayout = Qt.QHBoxLayout()
        bottomBnGrp = Qt.QDialogButtonBox(
            Qt.QDialogButtonBox.Save | Qt.QDialogButtonBox.Cancel
        )
        self.__saveProgBar = Qt.QProgressBar()

        buttonsLayout.addWidget(bottomBnGrp)
        buttonsLayout.addWidget(self.__saveProgBar)

        centralLayout.addWidget(roiSubGroup, 0, 0, 4, 1)
        centralLayout.addWidget(refSubGroup, 0, 1)
        centralLayout.addWidget(setSubGroup, 1, 1)
        centralLayout.addWidget(shiftSubGroup, 2, 1)
        centralLayout.addLayout(buttonsLayout, 3, 1, Qt.Qt.AlignLeft)

        # signal triggered when the ROI is applied in the full plot window
        self.__areaPlot.sigRoiApplied.connect(self.__slotRoiApplied)

        # signal triggered when an entry is selected in the preview widget
        self.__selector.sigSelectionChanged.connect(self.__slotSelectorChanged)

        # signal triggered when an entry is selected in the ref panel
        # self.__refPanel.sigSelectionChanged.connect(self.__slotRefSelectionChanged)

        # signal triggered when an entry is selected in the set panel
        self.__setPanel.sigSelectionChanged.connect(self.__slotSelectorChanged)

        # signal triggered when a point is selected on the REF plot
        self.__refPanel.sigPointSelected.connect(self.__slotRefPointSelected)

        # signal triggered when a point is selected on the SET plot
        self.__setPanel.sigPointSelected.connect(self.__slotSetPointSelected)

        # signal triggered when a shift value is changed
        self.__shiftSubject.sigShiftChanged.connect(self.__updateShiftPlot)

        self.__linearShiftBn.clicked.connect(self.__slotLinearShiftClicked)
        self.__linearShiftWholeRangeBn.clicked.connect(
            self.__slotLinearShiftWholeRangeClicked
        )
        resetShiftBn.clicked.connect(self.__slotResetShiftClicked)
        resetAllShiftBn.clicked.connect(self.__slotResetAllShiftClicked)

        bottomBnGrp.rejected.connect(self.close)

        bottomBnGrp.accepted.connect(self.__slotAccepted)

        self.__updateShiftPlot()

    def model(self):
        """Returns the ShiftModel"""
        return self.__selector.treeView().model()

    def __dataChanged(self, index):
        """Handle change of data in data QComboBox

        :param int index:
        """
        if index == 0:
            name = None  # To select intensity
        else:
            comboBox = self.sender()
            name = comboBox.currentText()

        self.__shiftSubject.setDisplayedDataName(name)

    def __slotAccepted(self):
        """Slot called when the "save" button is clicked"""
        self.__shiftSubject.writeToShiftH5(
            isSnapped=True, progressCb=self.__saveProgBar.setValue
        )
        self.close()

    def __slotResetAllShiftClicked(self):
        """Slot called when the "reset all shifts" button is clicked"""
        buttons = Qt.QMessageBox.Yes | Qt.QMessageBox.Cancel
        ans = Qt.QMessageBox.question(
            self,
            "Reset all?",
            "Are you sure you want to reset all " "shifts to 0?",
            buttons=buttons,
            defaultButton=Qt.QMessageBox.Cancel,
        )

        if ans == Qt.QMessageBox.Cancel:
            return

        self.__shiftSubject.resetShifts()

    def __slotResetShiftClicked(self):
        """Slot called when the "reset enty shift" button is clicked"""
        setEntry = self.__setPanel.getCurrentEntry()

        buttons = Qt.QMessageBox.Ok | Qt.QMessageBox.Cancel
        ans = Qt.QMessageBox.question(
            self,
            "Reset shift?",
            "Reset shift to 0 for entry :\n" "{0}?" "".format(setEntry),
            buttons=buttons,
            defaultButton=Qt.QMessageBox.Cancel,
        )
        if ans == Qt.QMessageBox.Cancel:
            return

        self.__shiftSubject.setShift(setEntry, 0.0, 0.0)

    def __slotLinearShiftClicked(self, wholeRange=False):
        """Slot called when the "Apply linear shift" button is clicked"""
        refEntry = self.__refPanel.getCurrentEntry()
        setEntry = self.__setPanel.getCurrentEntry()

        if refEntry == setEntry:
            Qt.QMessageBox.warning(
                self,
                "Same entry",
                "Can't set the shift, " "ref and set entries are the same.",
            )
            return

        buttons = Qt.QMessageBox.Ok | Qt.QMessageBox.Cancel

        if wholeRange:
            msg = "Are you sure you want to set a linear " "shift on the whole range?"
        else:
            msg = (
                "Are you sure you want to set a linear "
                "shift between entries\n"
                "- {0}\n"
                "and\n"
                "- {1}?".format(refEntry, setEntry)
            )

        ans = Qt.QMessageBox.question(
            self,
            "Apply linear shift",
            msg,
            buttons=buttons,
            defaultButton=Qt.QMessageBox.Cancel,
        )
        if ans == Qt.QMessageBox.Cancel:
            return

        self.__shiftSubject.applyLinearShift(setEntry, refEntry, wholeRange)
        self.__updateShiftPlot()

    def __slotLinearShiftWholeRangeClicked(self):
        return self.__slotLinearShiftClicked(wholeRange=True)

    def __updateShiftPlot(self):
        """Updates the shift plot"""
        shifts = self.__shiftSubject.getShifts()
        nShifts = len(shifts)

        dx = np.ndarray(nShifts, dtype=np.int32)
        dy = np.ndarray(nShifts, dtype=np.int32)

        for iShift, shift in enumerate(shifts):
            grid_shift = shift.grid_shift
            if grid_shift is None:
                grid_shift = [0, 0]
            dx[iShift] = grid_shift[0]
            dy[iShift] = grid_shift[1]

        self.__xShiftPlot.addCurve(
            np.arange(dx.size),
            dx,
            color="red",
            legend="gridshift_dx",
            yaxis="right",
            linestyle=" ",
            symbol="s",
        )
        self.__yShiftPlot.addCurve(
            np.arange(dy.size),
            dy,
            color="red",
            legend="gridshift_dy",
            yaxis="right",
            linestyle=" ",
            symbol="s",
        )

        dx = np.ndarray(nShifts, dtype=np.double)
        dy = np.ndarray(nShifts, dtype=np.double)

        for iShift, shift in enumerate(shifts):
            dx[iShift] = shift.dx
            dy[iShift] = shift.dy

        self.__xShiftPlot.addCurve(
            np.arange(dx.size),
            dx,
            color="blue",
            legend="shift_dx",
            linestyle=" ",
            symbol="o",
        )
        self.__yShiftPlot.addCurve(
            np.arange(dy.size),
            dy,
            color="blue",
            legend="shift_dy",
            linestyle=" ",
            symbol="o",
        )

    def __slotRefPointSelected(self, node, point):
        """Slot called when a point is selected on the REF plot.

        Updates the model's "SelectedPoint".

        :param point:
        """
        self.__shiftSubject.setReferenceControlPoint(
            node.getEntry(), point.x, point.y, point.xIdx
        )
        self.__setPanel.refreshSelectedPoint()

    def __slotSetPointSelected(self, node, point):
        """Slot called when a point is selected on the REF plot.

        Updates the model's "SelectedPoint".

        :param point:
        """
        setEntry = node.getEntry()

        try:
            self.__shiftSubject.setControlPoint(setEntry, point.x, point.y, point.xIdx)
        except ValueError as ex:
            Qt.QMessageBox.warning(self, "Exception", str(ex))
            return

    def __slotSelectorChanged(self, node):
        """Slot called when the "set" selection changes.

        Called from the preview panel or the "set" combobox.

        :param node:
        """
        self.__setPanel.setCurrentModelIndex(node.index())

    def __slotRoiApplied(self, roi, node):
        """Slot called when the ROI in the ShiftAreaSelectorWidget is applied.

        :param node: the node that was selected in the Roi selection widget
            when the roi was applied.
        :param roi: the roi values
        """
        mdlIndex = node.index()
        self.__shiftSubject.setRoi(roi)
        self.__refPanel.setCurrentModelIndex(mdlIndex)
        self.__setPanel.setCurrentModelIndex(mdlIndex)
        self.__linearShiftBn.setEnabled(True)
        self.__linearShiftWholeRangeBn.setEnabled(True)
