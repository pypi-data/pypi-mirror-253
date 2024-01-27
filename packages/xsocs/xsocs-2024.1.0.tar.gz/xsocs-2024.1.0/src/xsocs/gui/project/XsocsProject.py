import os

from .ProjectDef import ItemClassDef
from .ProjectItem import ProjectItem
from .AcqDataGroup import AcqDataGroup
from .IntensityGroup import IntensityGroup
from .QSpaceGroup import QSpaceGroup
from .ShiftGroup import ShiftGroup
from ...io.ShiftH5 import ShiftH5Writer


@ItemClassDef("XsocsProject")
class XsocsProject(ProjectItem):
    AcquisitionGroupPath = "/Acquisition"
    # ScanPositionsPath = '/Positions'
    IntensityGroupPath = "/Intensity"
    QSpaceGroupPath = "/QSpace"
    ShiftGroupPath = "/Shift"

    XsocsNone, XsocsInput, XsocsQSpace, XsocsFit = range(4)

    def __init__(self, *args, **kwargs):
        super(XsocsProject, self).__init__(*args, **kwargs)
        self.__xsocsFile = None
        self.__xsocsH5 = None
        self.__projectModel = None

    workdir = property(lambda self: os.path.dirname(self.filename))

    def _createItem(self):
        super(XsocsProject, self)._createItem()

        AcqDataGroup(
            self.filename, self.AcquisitionGroupPath, mode=self.mode, gui=self.gui
        )
        IntensityGroup(
            self.filename, self.IntensityGroupPath, mode=self.mode, gui=self.gui
        )
        QSpaceGroup(self.filename, self.QSpaceGroupPath, mode=self.mode, gui=self.gui)

        shiftGroup = ShiftGroup(
            self.filename, self.ShiftGroupPath, mode=self.mode, gui=self.gui
        )
        shiftGroup.setHidden(True)

        # TODO : get prefix
        xsocsFile = os.path.basename(self.filename)
        xsocsPrefix = xsocsFile.rpartition(".")[0]
        shiftFile = "{0}_shift.h5".format(xsocsPrefix)
        shiftFile = os.path.join(self.workdir, shiftFile)
        writer = ShiftH5Writer(shiftFile, mode="w")
        xsocsH5 = self.xsocsH5
        entries = xsocsH5.entries()
        for entry in entries:
            n_images = xsocsH5.n_images(entry)
            writer.create_entry(entry, n_points=n_images)
        shiftGroup.addShiftFile(shiftFile)

    def positions(self, entry):
        with self.xsocsH5 as xsocsH5:
            if entry == "Total":
                entry = xsocsH5.entries()[0]
            return xsocsH5.scan_positions(entry)

    def shortName(self, entry):
        """
        Returns the angle of the given entry, or None if the entry is not
            found.
        :param entry:
        :return: str
        """
        with self.xsocsH5 as xsocsH5:
            angle = xsocsH5.scan_angle(entry)
            if angle is None:
                return None
            return str(angle)

    def qspaceGroup(self, mode=None):
        mode = mode or self.mode
        return QSpaceGroup(self.filename, self.QSpaceGroupPath, mode=mode)

    def intensityGroup(self, mode=None):
        mode = mode or self.mode
        return IntensityGroup(self.filename, self.IntensityGroupPath, mode=mode)

    def shiftGroup(self, mode=None):
        mode = mode or self.mode
        return ShiftGroup(self.filename, self.ShiftGroupPath, mode=mode)
