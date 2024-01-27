"""
This module provides the IntensityView widget displaying the intensity map.

The IntensityView widget is using:
- The EntriesTable widget to display, sort and select scan entries.
- The CurvesList widget to display names and color of curves in the profile plot.
"""

from collections import namedtuple
import functools
import logging
import weakref

import numpy as np

from silx.gui import qt as Qt
from silx.gui.plot import PlotWidget

from .RectRoiWidget import RectRoiWidget

from ..shift.ShiftView import ShiftWidget

from ...widgets.XsocsPlot2D import XsocsPlot2D
from ...widgets.ScatterPlot import ScatterPlot
from ...widgets.Buttons import FixedSizePushButon


logger = logging.getLogger(__name__)

IntensityViewEvent = namedtuple("IntensityViewEvent", ["roi", "entries", "shiftFile"])


_BEAM_ENERGY_NAME = "beam energy"
"""Name used to select beam energy as a pseudo-positioner"""


class CurvesList(Qt.QTreeWidget):
    """Widget displaying the list of curves in a plot

    Used to display the list of profile curves.

    :param QWidget parent:
    :param PlotWidget plot: The plot from which to display the curves
    """

    def __init__(self, parent=None, plot=None):
        super(CurvesList, self).__init__(parent)
        assert isinstance(plot, PlotWidget)
        self.__plotRef = weakref.ref(plot)
        plot.sigContentChanged.connect(self.__plotContentChanged)

        headerItem = self.headerItem()
        headerItem.setText(0, "Curves")

    def __plotContentChanged(self, action, kind, legend):
        """Handle update of plot content

        See PlotWidget.sigContentChanged
        """
        if kind != "curve":
            return

        if action == "remove":
            items = self.findItems(
                legend, Qt.Qt.MatchFixedString | Qt.Qt.MatchCaseSensitive
            )
            if not items:
                logger.error('Cannot remove curve "%s" from CurvesList', legend)

            for item in items:  # There should be one and only one
                index = self.indexOfTopLevelItem(item)
                self.takeTopLevelItem(index)  # remove item in the tree

        elif action == "add":
            items = self.findItems(
                legend, Qt.Qt.MatchFixedString | Qt.Qt.MatchCaseSensitive
            )
            if not items:  # Add a new item
                treeItem = Qt.QTreeWidgetItem([legend])
                self.addTopLevelItem(treeItem)

            else:  # Reuse existing item, there should be only one
                treeItem = items[0]
                if len(items) != 1:
                    logger.error("More than one curve with name %s found", legend)

            # Set the icon from the curve color if possible
            icon = Qt.QIcon()

            plot = self.__plotRef()
            if plot is not None:
                plotItem = plot.getCurve(legend)
                if plotItem is not None:
                    color = np.array(plotItem.getColor())
                    if color.ndim == 1:
                        # Single color, array of colors are not supported
                        pixmap = Qt.QPixmap(16, 16)
                        pixmap.fill(Qt.QColor.fromRgbF(*color))
                        icon = Qt.QIcon(pixmap)

            treeItem.setIcon(0, icon)


class EntriesTable(Qt.QTableWidget):
    """Table displaying scans sorted by a configurable positioner

    :param QWidget parent:
    :param IntensityGroup intensityGroup:
    """

    sigCurrentChanged = Qt.Signal(str)
    """Signal emitted when current entry has changed.

    It provides the new current entry or None for no selection or Total
    """

    sigCheckedChanged = Qt.Signal(object)
    """Signal emitted when the checked entry list has changed

    It provides the list of checked entries name
    """

    def __init__(self, parent=None, intensityGroup=None):
        super(EntriesTable, self).__init__(parent)

        self.__intensityGroup = intensityGroup
        self.__positioner = "entry"
        self.__previousCheckedEntries = None

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels([self.__positioner.capitalize(), "Shift"])

        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.Qt.AlignLeft)
        header.setSectionResizeMode(Qt.QHeaderView.ResizeToContents)

        header = self.verticalHeader()
        header.setSectionResizeMode(Qt.QHeaderView.ResizeToContents)
        header.setVisible(False)

        self.setShowGrid(False)

        self.setSelectionMode(self.SingleSelection)
        self.setSelectionBehavior(self.SelectRows)

        entries = self.__intensityGroup.xsocsH5.entries()
        self.setRowCount(len(entries) + 1)

        # Add first 'Total' item

        item = Qt.QTableWidgetItem("  Total {0}/{0}".format(len(entries)))
        item.setFlags(Qt.Qt.ItemIsSelectable | Qt.Qt.ItemIsEnabled)
        self.setItem(0, 0, item)
        self.setCurrentItem(item)  # Select Total entry

        # Fill table with entries

        for index, entry in enumerate(entries):
            item = Qt.QTableWidgetItem(entry)
            item.setData(Qt.Qt.UserRole, entry)
            item.setFlags(
                Qt.Qt.ItemIsSelectable | Qt.Qt.ItemIsEnabled | Qt.Qt.ItemIsUserCheckable
            )
            item.setCheckState(Qt.Qt.Checked)
            self.setItem(index + 1, 0, item)

            item = Qt.QTableWidgetItem()
            item.setFlags(Qt.Qt.ItemIsSelectable | Qt.Qt.ItemIsEnabled)
            self.setItem(index + 1, 1, item)

        self.itemChanged.connect(self.__itemChanged)
        self.currentItemChanged.connect(self.__currentItemChanged)

    def __itemChanged(self, item):
        """Handle update of items to manage change of checked entries"""
        column = item.column()
        row = item.row()
        if column == 0 and row >= 1:
            checkedEntries = self.getCheckedEntries()
            if self.__previousCheckedEntries != checkedEntries:
                self.__previousCheckedEntries = checkedEntries
                totalItem = self.item(0, 0)
                totalItem.setText(
                    "  Total {}/{}".format(len(checkedEntries), self.rowCount() - 1)
                )
                self.sigCheckedChanged.emit(checkedEntries)

    def __currentItemChanged(self, current, previous):
        """Handle change of selection to emit sigCurrentChanged"""
        if current is None:
            self.sigCurrentChanged.emit(None)
        elif previous is None or current.row() != previous.row():
            self.sigCurrentChanged.emit(self.getCurrentEntry())

    def __getEntry(self, row):
        """Returns the entry name corresponding to a given row.

        If row is out of bound, it returns None.

        :param int row: A table row index
        :rtype: Union[str, None]
        """
        if 1 <= row < self.rowCount():
            item = self.item(row, 0)  # Always use first column item
            return item.data(Qt.Qt.UserRole)
        else:
            return None

    def __getRowFromEntry(self, entry):
        """Returns the table row corresponding to a given entry.

        If entry is not in the table, it returns None.

        :param str entry: The entry to find
        :rtype: Union[str, None]
        """
        for row in range(1, self.rowCount()):
            if entry == self.__getEntry(row):
                return row
        return None  # Not found

    def setShiftColumnForEntry(self, entry, text):
        """Set text displayed in the Shift column of an entry

        :param str entry: Entry name
        :param str text: Text to display
        """
        row = self.__getRowFromEntry(entry)
        if row is None:
            logger.error("Cannot find entry %s", entry)
        else:
            item = self.item(row, 1)
            item.setText(text)

    def setEntriesPositionerName(self, name):
        """Set the positioner used to display and sort entries

        :param str name:
        """
        self.__positioner = name
        self.setHorizontalHeaderLabels([self.__positioner.capitalize(), "Shift"])

        with self.__intensityGroup.xsocsH5 as xsocsH5:
            for row in range(1, self.rowCount()):
                if name == _BEAM_ENERGY_NAME:
                    value = xsocsH5.beam_energy(self.__getEntry(row))
                else:
                    value = xsocsH5.positioner(self.__getEntry(row), name)
                item = self.item(row, 0)
                item.setText(str(value))

        self.sortItems(0, Qt.Qt.AscendingOrder)

    def getEntriesPositionerName(self):
        """Returns the positioner used to display and sort entries.

        If entry names are displayed (default), then 'entry' is returned.

        :rtype: str
        """
        return self.__positioner

    def getEntries(self):
        """Returns the list of entries names.

        :rtype: List[str]
        """
        return [self.__getEntry(row) for row in range(1, self.rowCount())]

    def getCurrentEntry(self):
        """Returns the currently selected entry or None for Total.

        :rtype: Union[str, None]
        """
        item = self.currentItem()
        row = item.row()
        return self.__getEntry(row)

    def getCheckedEntries(self):
        """Returns name of checked entries.

        :rtype: List[str]
        """
        entries = []
        for row in range(1, self.rowCount()):
            item = self.item(row, 0)
            if item.checkState() == Qt.Qt.Checked:
                entries.append(self.__getEntry(row))
        return entries

    def setAllEntriesChecked(self, checked=True):
        """Check/Uncheck all entries in the table

        :param bool checked: True (default) to check all, False to uncheck all
        """
        checked = Qt.Qt.Checked if checked else Qt.Qt.Unchecked

        emitSignal = False
        wasBlocked = self.blockSignals(True)

        for row in range(1, self.rowCount()):
            item = self.item(row, 0)
            if item.checkState() != checked:
                emitSignal = True
                item.setCheckState(checked)

        self.blockSignals(wasBlocked)

        if emitSignal:  # Only emit signal once if needed
            self.sigCheckedChanged.emit(self.getCheckedEntries())


class IntensityView(Qt.QMainWindow):
    sigProcessApplied = Qt.Signal(object)

    def __init__(self, intensityGroup, parent=None, **kwargs):
        """
        Widget displaying the summed intensities over the sample. It allows
        for angle selection and ROI selection.
        :param intensityGroup: IntensityGroup instance.
        :param parent: parent widget.
        :param kwargs:
        """
        super(IntensityView, self).__init__(parent, **kwargs)

        # =================================
        # TODO : this is temporary code to allow previously created projects
        # to work with the new shift
        # TODO : get prefix
        xsocsProject = intensityGroup.projectRoot()
        sGroup = xsocsProject.shiftGroup()
        sGroup._fixFile()
        # =================================

        self.setWindowTitle(
            "[XSOCS] {0}:{1}".format(intensityGroup.filename, intensityGroup.path)
        )

        self.__shiftApplied = False

        self.__scatterPlot = ScatterPlot()
        self.__scatterPlot.sigSelectedIndexChanged.connect(self.__updateProfile)

        self.__iGroup = intensityGroup

        selector = Qt.QWidget()
        layout = Qt.QVBoxLayout(selector)

        # Options as a form layout

        optionLayout = Qt.QFormLayout()
        layout.addLayout(optionLayout)

        xsocsH5 = self.__iGroup.projectRoot().xsocsH5

        # Sort by combo box

        self.__sortByComboBox = Qt.QComboBox()
        positioners = xsocsH5.positioners()
        for positioner in ("eta", "phi"):  # Add mostly used positioners first
            if positioner in positioners:
                self.__sortByComboBox.addItem(positioner)

        # Add beam energy
        self.__sortByComboBox.addItem(_BEAM_ENERGY_NAME)

        self.__sortByComboBox.insertSeparator(3)
        for name in positioners:
            self.__sortByComboBox.addItem(name)
        self.__sortByComboBox.currentTextChanged.connect(self.__sortByTextChanged)
        optionLayout.addRow("Sort by:", self.__sortByComboBox)

        # Normalization combo box

        self.__normalizationComboBox = Qt.QComboBox()
        self.__normalizationComboBox.addItem("-")
        for name in xsocsH5.normalizers():
            self.__normalizationComboBox.addItem(name)
        self.__normalizationComboBox.currentIndexChanged.connect(self.__update)
        optionLayout.addRow("Normalization:", self.__normalizationComboBox)

        # Shift option

        shiftCb = Qt.QCheckBox("Apply shift")
        shiftEditBn = Qt.QToolButton()
        shiftEditBn.setText("Edit")
        shiftEditBn.setToolTip("Edit shift values")

        shiftCb.toggled.connect(self.__slotShiftToggled)
        shiftEditBn.clicked.connect(self.__slotShiftEditClicked)

        optionLayout.addRow(shiftCb, shiftEditBn)

        # Entries table
        self.__entriesTable = EntriesTable(parent=self, intensityGroup=intensityGroup)
        self.__entriesTable.setEntriesPositionerName("eta")
        self.__entriesTable.setColumnHidden(1, True)
        self.__entriesTable.sigCheckedChanged.connect(self.__checkedEntriesChanged)
        self.__entriesTable.sigCurrentChanged.connect(self.__update)
        layout.addWidget(self.__entriesTable)

        # Select/Unselect buttons

        bnLayout = Qt.QHBoxLayout()
        layout.addLayout(bnLayout)

        selAllBn = FixedSizePushButon("Select All")
        selAllBn.clicked.connect(
            functools.partial(self.__entriesTable.setAllEntriesChecked, True)
        )
        bnLayout.addWidget(selAllBn)

        selNoneBn = FixedSizePushButon("Unselect All")
        selNoneBn.clicked.connect(
            functools.partial(self.__entriesTable.setAllEntriesChecked, False)
        )
        bnLayout.addWidget(selNoneBn)

        # ROI widget

        rectRoiWidget = RectRoiWidget(plot=self.__scatterPlot)
        rectRoiWidget.setApplyButtonWithoutRoi(True)

        applyBn = rectRoiWidget.applyButton()
        applyBn.setText("To Q Space")
        applyBn.setToolTip("To Q Space")
        rectRoiWidget.sigRoiApplied.connect(self.__slotRoiApplied)

        # Profile widget

        # Override sizeHint to avoid profile being too high
        class ProfileWidget(Qt.QWidget):
            def sizeHint(self):
                return Qt.QSize(640, 300)

        profileWid = ProfileWidget()
        profileLayout = Qt.QHBoxLayout(profileWid)

        self.__profilePlot = XsocsPlot2D()
        self.__profilePlot.setKeepDataAspectRatio(False)
        profileLayout.addWidget(self.__profilePlot, 10)

        curveList = CurvesList(plot=self.__profilePlot)
        profileLayout.addWidget(curveList)

        # Add widgets in dock widgets
        for area, widget in (
            (Qt.Qt.LeftDockWidgetArea, selector),
            (Qt.Qt.RightDockWidgetArea, rectRoiWidget),
            (Qt.Qt.BottomDockWidgetArea, profileWid),
        ):
            dock = Qt.QDockWidget(self)
            dock.setWidget(widget)
            features = dock.features() ^ Qt.QDockWidget.DockWidgetClosable
            dock.setFeatures(features)
            self.addDockWidget(area, dock)

        self.setCentralWidget(self.__scatterPlot)

        self.__update()

    def __update(self, *args, **kwargs):
        """Update plot and profile"""
        self.__updateScatterPlot()
        self.__updateProfile()

    def __sortByTextChanged(self, text):
        """Handles update of Sort By combo box"""
        self.__entriesTable.setEntriesPositionerName(text)
        self.__updateProfile()

    def __checkedEntriesChanged(self, entries):
        """Handle change of checked entries in EntriesTable"""
        if self.__entriesTable.getCurrentEntry() is None:
            # Total is selected, plot needs update
            self.__update()
        else:  # Otherwise only profile needs to be updated
            self.__updateProfile()

    def getNormalizer(self):
        """Returns currently set normalizer name or None

        :rtype: Union[str, None]"""
        text = self.__normalizationComboBox.currentText()
        return None if text == "-" else text

    def __getShiftItem(self):
        """Returns the ShiftItem

        :rtype: ShiftItem
        """
        sItems = self.__iGroup.projectRoot().shiftGroup().getShiftItems()
        if len(sItems) > 1:
            raise NotImplementedError("Only one shift item supported " "right now.")
        return sItems[0]

    def __slotShiftToggled(self, checked):
        """
        Slot called when the 'apply shift' checkbox is toggled.
        :param checked:
        :return:
        """
        self.__shiftApplied = checked

        application = Qt.QApplication.instance()
        # could not set the cursor with QWidget.setCursor for some reason
        application.setOverrideCursor(Qt.Qt.WaitCursor)

        if checked:
            self.__entriesTable.setColumnHidden(1, False)

            with self.__getShiftItem().shiftH5 as shiftH5:
                for entry in self.__entriesTable.getEntries():
                    shift = shiftH5.shift(entry)
                    shiftX = shift["shift_x"]
                    shiftY = shift["shift_y"]

                    if shiftX is None and shiftY is None:
                        text = "Not set"
                    elif shiftX is None or shiftY is None:  # error
                        text = "error"
                    else:
                        text = "x:{0:6g}, y:{1:6g}".format(shiftX, shiftY)

                        grid = shift["grid_shift"]
                        if shiftH5.is_snapped_to_grid() and grid is not None:
                            text += ", grid:{0}".format(grid)

                    self.__entriesTable.setShiftColumnForEntry(entry, text)

        else:
            self.__entriesTable.setColumnHidden(1, True)
            for entry in self.__entriesTable.getEntries():
                self.__entriesTable.setShiftColumnForEntry(entry, "")

        application.restoreOverrideCursor()

        self.__update()

    def __slotShiftEditClicked(self):
        """
        Slot called when the 'edit shift' button is clicked.
        :return:
        """
        # TODO : only one shift item supported at the moment
        shiftItem = self.__iGroup.projectRoot().shiftGroup().getShiftItems()[0]
        shiftWidget = ShiftWidget(self.__iGroup, shiftItem, parent=self)
        shiftWidget.setAttribute(Qt.Qt.WA_DeleteOnClose)
        shiftWidget.setWindowModality(Qt.Qt.WindowModal)
        shiftWidget.show()

    def __computeIntensity(self, entry, normalizer=None):
        """Returns intensity with normalization and shift applied if any

        :param str entry: The entry for which to get intensity
        :param str normalizer: Measurement dataset name used for normalization
        """
        item = self.__iGroup.getIntensityItem(entry)
        intensity = np.array(item.getScatterData()[0], dtype=np.float64)

        if normalizer is not None:
            normalization = self.__iGroup.xsocsH5.measurement(
                entry=entry, measurement=normalizer
            )
            if normalization is None:
                logger.error("Cannot normalize with %s: not found in file", normalizer)
            else:
                # Makes sure to use float for the division
                normalization = np.array(normalization, dtype=np.float64)
                if len(normalization) != len(intensity):
                    logger.error(
                        "Cannot normalize with %s: "
                        "length and number of intensities mismatch",
                        normalizer,
                    )
                else:
                    intensity /= normalization

        if self.__shiftApplied:
            with self.__getShiftItem().shiftH5 as shiftH5:
                shift = shiftH5.shift(entry)
                if shift["shift_x"] is not None and shift["shift_y"] is not None:
                    shift_idx = shiftH5.shifted_indices(entry)
                    intensity = intensity[shift_idx]

        return intensity

    def __updateScatterPlot(self):
        """Update the scatter plot to reflect current selection/normalization."""
        entry = self.__entriesTable.getCurrentEntry()
        normalizer = self.getNormalizer()

        # Get intensity values

        if entry is None:  # Get total intensity
            entries = self.__entriesTable.getCheckedEntries()
            title = "Total ({0}/{1})".format(
                len(entries), len(self.__entriesTable.getEntries())
            )
        else:  # Single selected entry
            entries = [entry]
            title = entry

        if normalizer is not None:
            title = " ".join((title, "/", normalizer))

        self.__scatterPlot.setGraphTitle(title)

        if not entries:  # Nothing to show
            self.__scatterPlot.clear()

        else:  # Use positions of first checked entry
            positions = self.__iGroup.getIntensityItem(entries[0]).getScatterData()[1]
            pos0, pos1 = positions.pos_0, positions.pos_1
            if self.__shiftApplied:
                with self.__getShiftItem().shiftH5 as shiftH5:
                    shift = shiftH5.shift(entries[0])
                    if shift["shift_x"] is not None and shift["shift_y"] is not None:
                        shift_idx = shiftH5.shifted_indices(entries[0])
                        pos0, pos1 = pos0[shift_idx], pos1[shift_idx]

            intensity = np.zeros(len(pos0), dtype=np.float64)
            for entry in entries:
                intensity += self.__computeIntensity(entry, normalizer)

            previousScatter = self.__scatterPlot.getScatter()
            self.__scatterPlot.addScatter(pos0, pos1, intensity, symbol="s")
            if previousScatter is None:
                # Only reset zoom when no scatter plot was displayed
                self.__scatterPlot.resetZoom()
            self.__scatterPlot.setGraphTitle(title)

    def __updateProfile(self):
        """Update the profile plot to reflect current status"""
        # Clear the plot
        self.__profilePlot.setGraphTitle()
        self.__profilePlot.getXAxis().setLabel("")
        self.__profilePlot.getYAxis().setLabel("")
        self.__profilePlot.clear()

        selectedIndex = self.__scatterPlot.getSelectedIndex()
        selectedPosition = self.__scatterPlot.getSelectedPosition()
        if selectedIndex is None or selectedPosition is None:
            return

        entries = self.__entriesTable.getEntries()
        selected = self.__entriesTable.getCheckedEntries()
        selectedIndices = [i for i, e in enumerate(entries) if e in selected]
        nEntries = len(entries)

        normalizerName = self.getNormalizer()
        positionerName = self.__entriesTable.getEntriesPositionerName()

        xData = np.empty((nEntries,), dtype=np.float64)
        intensities = np.empty((nEntries,), dtype=np.float64)

        for entryIdx, entry in enumerate(entries):
            item = self.__iGroup.getIntensityItem(entry)
            intensities[entryIdx] = item.getPointValue(selectedIndex)

            if positionerName == _BEAM_ENERGY_NAME:
                xValue = self.__iGroup.xsocsH5.beam_energy(entry)
            else:
                xValue = self.__iGroup.xsocsH5.positioner(entry, positionerName)
            xData[entryIdx] = xValue if xValue is not None else entryIdx

            if normalizerName:
                norm = self.__iGroup.xsocsH5.measurement(entry, normalizerName)
                if norm is None:
                    logger.error(
                        "Cannot get normalization for entry %s, set to 1" % entry
                    )
                else:
                    intensities[entryIdx] /= norm[selectedIndex]

        # Set the plot

        self.__profilePlot.setGraphTitle(
            "Profile @ ({0:.7g}, {1:.7g})".format(*selectedPosition)
        )

        self.__profilePlot.getXAxis().setLabel(positionerName)

        yLabel = "Intensity"
        if normalizerName:
            yLabel = " / ".join((yLabel, normalizerName))
        self.__profilePlot.getYAxis().setLabel(yLabel)

        self.__profilePlot.addCurve(
            xData, intensities, legend="All", symbol="o", color="blue"
        )

        if selectedIndices:
            self.__profilePlot.addCurve(
                xData[selectedIndices],
                intensities[selectedIndices],
                legend="Selected ({0}/{1})".format(len(selectedIndices), len(entries)),
                symbol="o",
                color="red",
            )

    def __slotRoiApplied(self, roi):
        """
        Slot called when the ROI is applied.
        :param roi:
        :return:
        """
        selEntries = self.__entriesTable.getCheckedEntries()

        if self.__shiftApplied:
            shiftGroup = self.__iGroup.projectRoot().shiftGroup()
            # TODO : only one shift file supported right now
            shiftFile = shiftGroup.getShiftItems()[0].shiftFile
        else:
            shiftFile = None
        event = IntensityViewEvent(roi=roi, entries=selEntries, shiftFile=shiftFile)

        self.sigProcessApplied.emit(event)
