import copy
from collections import OrderedDict, namedtuple


import numpy as np


from silx.gui import qt as Qt


from ....io.ShiftH5 import ShiftH5Writer
from ....process.shift.shift import ShiftValue, ScanShift

PlotData = namedtuple("PlotData", ["x", "y", "z", "idx"])


class ShiftSubject(Qt.QObject):
    """An entry shift is always relative to the FIRST entry in the list."""

    sigRoiChanged = Qt.Signal(object)
    """Signal emitted when the ROI changes"""

    sigReferenceControlPointChanged = Qt.Signal(object)
    """Signal emitted when the selected point changes."""

    sigShiftChanged = Qt.Signal(object)
    """Signal emitted when the shift for an entry changed.

    Value passed : an instance of ShiftValue.
    """

    sigDataChanged = Qt.Signal()
    """Signal emitted when the displayed data has changed"""

    def __init__(self, iGroup, shiftItem, **kwargs):
        super(ShiftSubject, self).__init__(**kwargs)

        self.__iGroup = iGroup
        self.__shiftItem = shiftItem
        self.__roi = None
        self.__displayedDataName = None

        self.__xsocsH5 = iGroup.xsocsH5
        entries = self.__xsocsH5.entries()

        self.__selectedPoint = {
            "x": None,
            "y": None,
            "idx": None,
            "gridIdx": None,
            "entry": entries[0],
        }

        self.__scanShift = ScanShift(self.__xsocsH5)

        self.__snap = False
        self.__shiftValues = OrderedDict()

        shiftH5 = shiftItem.shiftH5

        with shiftH5:
            for entry in entries:
                # if xsocsH5.is_regular_grid(entry):
                #     gridShift = [0, 0]
                # else:
                #     gridShift = None
                shift = shiftH5.shift(entry)
                dx = shift["shift_x"]
                dy = shift["shift_y"]
                gridShift = shift["grid_shift"]

                if dx is None:
                    dx = 0.0

                if dy is None:
                    dy = 0.0

                if gridShift is None:
                    gridShift = [0, 0]

                self.__updateShift(entry, dx, dy, gridShift)

    def displayedDataName(self):
        """Returns the name of the data to display or None for intensity

        :rtype: Union[str,None]
        """
        return self.__displayedDataName

    def setDisplayedDataName(self, name):
        """Set the data to display

        :param Union[str,None] name:
        """
        if name != self.__displayedDataName:
            self.__displayedDataName = name
            self.sigDataChanged.emit()

    def scanShift(self):
        """Returns this ShiftSubject's instance of ScanShift

        :rtype: ScanShift
        """
        return self.__scanShift

    def getIntensityGroup(self):
        """Returns the IntensityGroupItem.

        :rtype: IntensityGroupItem
        """
        return self.__iGroup

    def xsocsH5(self):
        """Returns this ShiftSubject xsocsH5 file."""
        return self.__xsocsH5

    def setControlPoint(self, entry, x, y, idx=None):
        """Sets the given entry control point.

        This control point is used to
        compute the shift by comparing it to the reference control point.
        The signal sigShiftChanged is emitted if the new shift value is
        different from the previous one.

        :param entry:
        :param x:
        :param y:
        :param idx: index of the control point in the data array. If not
            not provided then the closest data point to the given coordinates
            will be taken.
        """
        changed = False

        shift = self.__shiftValues.get(entry)
        refPt = self.getReferenceControlPoint()
        refEntry = refPt["entry"]

        if refEntry == entry:
            raise ValueError(
                "Can't set the shift, " "ref and set entries are the same."
            )

        refShift = self.__shiftValues.get(refEntry)

        if refShift is None:
            raise ValueError("Reference control point has not been set yet.")

        refX = refPt["x"]
        refY = refPt["y"]
        refDx = refShift.dx
        refDy = refShift.dy

        dx = x - refX + refDx
        dy = y - refY + refDy

        if shift is None:
            raise ValueError("Unknown entry : {0}.".format(entry))

        if shift.dx != dx:
            changed = True
        else:
            dx = shift.dx

        if shift.dy != dy:
            changed = True
        else:
            dy = shift.dy

        gridShift = self.__gridShift(entry, dx, dy, idx=idx, refPos=(refX, refY))
        if gridShift is not None:
            changed = True

        if changed:
            newShift = self.__updateShift(shift.entry, dx, dy, gridShift)
            self.sigShiftChanged.emit(newShift)

    def __gridShift(self, entry, dx, dy, idx=None, refPos=None):
        """Computes the shift on a regular grid, if applicable

        :param entry:
        :param dx:
        :param dy:
        """
        gridShift = None
        xsocsH5 = self.__xsocsH5
        with xsocsH5:
            if (dx != 0 or dy != 0) and idx is None and xsocsH5.is_regular_grid(entry):
                pos = xsocsH5.scan_positions(entry)
                if refPos is None:
                    x = pos.pos_0[self.__selectedPoint["idx"]]
                    y = pos.pos_1[self.__selectedPoint["idx"]]
                else:
                    x, y = refPos

                idx = (
                    (pos.pos_0 - (x + dx)) ** 2 + (pos.pos_1 - (y + dy)) ** 2
                ).argmin()

            if idx is not None:
                scan_params = xsocsH5.scan_params(entry)
                stepX = scan_params["motor_0_steps"]
                gridIdx = np.array([idx % stepX, idx // stepX])
                gridShift = gridIdx - self.__selectedPoint["gridIdx"]
        return gridShift

    def resetShifts(self):
        """Resets all shifts to 0."""
        for entry in self.__shiftValues:
            self.setShift(entry, 0, 0)

    def setShift(self, entry, dx, dy, gridShift=None):
        """Sets the shift for the given entry.

        :param entry:
        :param dx:
        :param dy:
        :param gridShift:
        """
        changed = False

        shift = self.__shiftValues.get(entry)

        if shift is None:
            raise ValueError("Unknown entry : {0}.".format(entry))

        if entry == list(self.__shiftValues.keys())[0] and dx != 0.0 and dy != 0:
            raise ValueError("The first entry's shift can't be set.")

        if shift.dx != dx:
            changed = True
        else:
            dx = shift.dx

        if shift.dy != dy:
            changed = True
        else:
            dy = shift.dy

        if gridShift is None:
            gridShift = self.__gridShift(entry, dx, dy)

        if not np.array_equal(gridShift, shift.grid_shift):
            changed = True
        else:
            gridShift = shift.grid_shift

        if changed:
            newShift = self.__updateShift(shift.entry, dx, dy, gridShift)
            self.sigShiftChanged.emit(newShift)

    def __updateShift(self, entry, dx, dy, gridShift):
        """Updates the shift values dictionary

        :param dx:
        :param dy:
        :param angle:
        :param entry:
        :param set:
        :param gridShift:
        :return: the newly create shift value.
        """
        newVal = ShiftValue(dx=dx, dy=dy, entry=entry, grid_shift=gridShift)
        self.__shiftValues[entry] = newVal
        self.__scanShift.set_shift(entry, dx, dy, grid_shift=gridShift)
        return newVal

    def getShift(self, entry):
        """Returns the shift applied to the given entry, relative to the first
        entry.

        :param entry:
        """
        shift = self.__shiftValues.get(entry)

        if shift is None:
            raise ValueError("Unknown entry : {0}.".format(entry))

        return shift

    def getShifts(self):
        """Return all shifts as a list."""
        return list(self.__shiftValues.values())

    def getShiftEntries(self):
        """Returns the names of all entries.

        :rtype: List[str]
        """
        return tuple(self.__shiftValues.keys())

    def getIntersectionIndices(self, grid=True, progressCb=None):
        """Returns the intersection of all entries.

        :param grid: set to True to shift all entries along a regular grid.
            Obviously only available if all points are on such a grid.
        :param progressCb: function that will be called to notify the caller
            of the progress. The callback will be passed an integer value
            between 0 and 100 (complete).
        """
        return self.__scanShift.get_intersection_indices(
            grid=grid, progress_cb=progressCb
        )

    def setReferenceControlPoint(self, refEntry, x, y, idx=None):
        """Sets the coordinates of the selected point

        (used to align images in the previews).

        Emits sigSelectedPointChanged if the new coordinates are different
        from the previous ones.

        :param x: X sample coordinates
        :param y: Y sample coordinates
        :param idx: index of the point in the sample points array
        """
        refPt = self.__selectedPoint
        if (x, y) != (refPt["x"], refPt["y"]):
            # refEntry = list(self.__shiftValues.keys())[0]
            if idx is None:
                pos = self.__xsocsH5.scan_positions(refEntry)
                idx = ((pos.pos_0 - x) ** 2 + (pos.pos_1 - y) ** 2).argmin()

            # TODO : check idx bounds

            if self.__xsocsH5.is_regular_grid(refEntry):
                scan_params = self.__xsocsH5.scan_params(refEntry)
                stepX = scan_params["motor_0_steps"]
                gridIdx = [idx % stepX, idx // stepX]
            else:
                gridIdx = None

            refPt["x"], refPt["y"] = x, y
            refPt["idx"], refPt["gridIdx"] = idx, gridIdx
            refPt["entry"] = refEntry
            self.sigReferenceControlPointChanged.emit(copy.deepcopy(refPt))

    def getReferenceControlPoint(self):
        """Returns the selected point coordinates, or None if not set yet.

        :return: numpy 2 elements array
        :rtype: Union[numpy.ndarray,None]
        """
        if self.__selectedPoint["x"] is None:
            return None
        return copy.deepcopy(self.__selectedPoint)

    def getFullData(self, entry):
        """Returns the given entry data. No ROI applied.

        :param entry:
        :return: (x, y, intensity)
        :rtype: PlotData
        """
        iItem = self.__iGroup.getIntensityItem(entry)
        data, positions = iItem.getScatterData()

        if self.displayedDataName() is not None:
            # Read data from measurements
            data = self.xsocsH5().measurement(
                entry=entry, measurement=self.displayedDataName()
            )

        return PlotData(x=positions.pos_0, y=positions.pos_1, z=data, idx=None)

    def getRoiData(self, entry, shifted=True, centered=False):
        """Returns the given entry data inside the ROI,
        or None if no ROI is defined.

        :param entry:
        :param shifted: the shift is applied to the ROI
        :param centered: the roi is centered around the selected point
        (and shifted if shifted is True)
        :return: (x, y, intensity)
        :rtype: Union[PlotData,None]
        """
        roi = self.getRoi(centered=centered)

        if roi is None:
            return None

        fullData = self.getFullData(entry)
        pos_0 = fullData.x
        pos_1 = fullData.y
        data = fullData.z

        if shifted:
            shift = self.getShift(entry)
            roi += np.array([shift.dx, shift.dx, shift.dy, shift.dy])

        dataIdx = np.where(
            (pos_0 >= roi[0])
            & (pos_0 <= roi[1])
            & (pos_1 >= roi[2])
            & (pos_1 <= roi[3])
        )

        data = data[dataIdx]
        pos_0 = pos_0[dataIdx]
        pos_1 = pos_1[dataIdx]

        return PlotData(x=pos_0, y=pos_1, z=data, idx=dataIdx[0])

    def setRoi(self, roi):
        """Sets the ROI.

        :param roi:
        """
        self.__roi = np.array([roi[0], roi[1], roi[2], roi[3]])

        if self.__selectedPoint is None:
            self.__selectedPoint = (
                roi[0] + (roi[1] - roi[0]) / 2.0,
                roi[2] + (roi[3] - roi[2]) / 2.0,
            )
        self.sigRoiChanged.emit(self.__roi)

    def getRoi(self, centered=False):
        """Returns the current ROI values, or None if no ROI has been set.

        :param centered: True to instead return a ROI with the same shape
            but centered on the selected point.
        :rtype: Union[numpy.ndarray,None]
        """
        if self.__roi is None:
            return None

        roi = np.array(self.__roi, copy=True)

        if centered:
            selectedPoint = self.__selectedPoint

            if selectedPoint["x"] is None:
                return None

            roiShape = self.getRoiSize()

            refPoint = [selectedPoint["x"], selectedPoint["y"]]
            disp = refPoint - (roiShape / 2.0) - roi[[0, 2]]
            roi[0:2] += disp[0]
            roi[2:4] += disp[1]

        return roi

    def getRoiSize(self):
        """Returns the current ROI dimensions, or None if no ROI has been set.

        :rtype: numpy.ndarray
        """
        roi = self.__roi
        if roi is None:
            return None
        return np.array([roi[1] - roi[0], roi[3] - roi[2]])

    def applyLinearShift(self, fromEntry, toEntry, wholeRange=False):
        """Applied a linear shift between two entries

        :param fromEntry:
        :param toEntry:
        :param bool wholeRange:
        """
        entries = list(self.__shiftValues.keys())

        try:
            fromIdx = entries.index(fromEntry)
        except ValueError:
            raise ValueError("Entry not found : {0}.".format(fromEntry))

        try:
            toIdx = entries.index(toEntry)
        except ValueError:
            raise ValueError("Entry not found : {0}.".format(toEntry))

        if toIdx < fromIdx:
            toIdx, fromIdx = fromIdx, toIdx
            toEntry, fromEntry = fromEntry, toEntry

        nEntries = toIdx - fromIdx
        if nEntries == 1:
            return

        fromShift = self.__shiftValues[fromEntry]
        toShift = self.__shiftValues[toEntry]

        xStep = float(toShift.dx - fromShift.dx) / nEntries
        yStep = float(toShift.dy - fromShift.dy) / nEntries

        if wholeRange:
            for stepIdx in range(1 - fromIdx, len(entries) - fromIdx):
                self.setShift(
                    entries[fromIdx + stepIdx],
                    fromShift.dx + stepIdx * xStep,
                    fromShift.dy + stepIdx * yStep,
                )
        else:
            for stepIdx in range(1, nEntries):
                self.setShift(
                    entries[fromIdx + stepIdx],
                    fromShift.dx + stepIdx * xStep,
                    fromShift.dy + stepIdx * yStep,
                )

    def writeToShiftH5(self, isSnapped=True, progressCb=None):
        """Writes the shift values to the shiftItem's ShiftH5 instance.

        :param isSnapped: set to True to inform that the user had selected
        "snap to grid" when editing the shift.
        :param progressCb: function that will be called to notify the caller
            of the progress. The callback will be passed an integer value
            between 0 and 100 (complete).
        """
        shiftH5 = ShiftH5Writer(self.__shiftItem.shiftFile, mode="w")
        scanShift = self.__scanShift

        if progressCb:
            progressCb(0)

        n_entries = len(self.__shiftValues)

        with shiftH5:
            shiftH5.set_is_snapped_to_grid(isSnapped)
            for idx, (entry, values) in enumerate(self.__shiftValues.items()):
                if progressCb:
                    progressCb(int(np.round(100 * idx / (n_entries - 1.0))))

                n_images = self.__xsocsH5.n_images(entry)
                shiftH5.create_entry(entry, n_points=n_images, raise_on_exists=False)
                shiftH5.set_shift(entry, values.dx, values.dy, values.grid_shift)
                shifted_indices = scanShift.get_entry_intersection_indices(
                    entry, grid=isSnapped
                )
                shiftH5.set_shifted_indices(entry, shifted_indices.astype(np.int32))

        if progressCb:
            progressCb(100)
