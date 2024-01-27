import os


from ...io.ShiftH5 import ShiftH5, ShiftH5Writer
from .ProjectItem import ProjectItem
from .ProjectDef import ItemClassDef


@ItemClassDef("ShiftGroup")
class ShiftGroup(ProjectItem):
    """Project item containing a group of fit results."""

    def addShiftFile(self, shiftFile):
        """
        Adds a shift file to this group. Creates a FitItem.
        :param shiftFile:
        :return:
        """

        childs = self.getShiftItems()
        if len(childs) > 0:
            raise NotImplementedError("Only one shift file supported " "at the moment.")

        itemName = os.path.basename(shiftFile).rsplit(".")[0]
        itemPath = self.path + "/" + itemName
        item = ShiftItem(self.filename, itemPath, mode="a")
        item.shiftFile = shiftFile
        return item

    def getShiftItems(self):
        """
        Returns all shift items in this group.
        :return:
        """
        return self.children(classinfo=ShiftItem)

    def _fixFile(self):
        """
        Temporary function for legacy compatibility
        :return:
        """
        if len(self.getShiftItems()) == 0:
            xsocsFile = os.path.basename(self.filename)
            xsocsPrefix = xsocsFile.rpartition(".")[0]
            shiftFile = "{0}_shift.h5".format(xsocsPrefix)
            shiftFile = os.path.join(self.projectRoot().workdir, shiftFile)
            writer = ShiftH5Writer(shiftFile, mode="w")
            xsocsH5 = self.xsocsH5
            entries = xsocsH5.entries()
            for entry in entries:
                n_images = xsocsH5.n_images(entry)
                writer.create_entry(entry, n_points=n_images)
            self.addShiftFile(shiftFile)
            self.setHidden(True)


@ItemClassDef("ShiftItem")
class ShiftItem(ProjectItem):
    """Project item containing shift values."""

    ShiftH5FilePath = "input"

    def __init__(self, *args, **kwargs):
        self.__shiftFile = None
        super(ShiftItem, self).__init__(*args, **kwargs)

    shiftH5 = property(lambda self: ShiftH5(self.shiftFile) if self.shiftFile else None)

    @property
    def shiftFile(self):
        """The name of the input data file."""
        if self.__shiftFile is None:
            with self._get_file() as h5f:
                path = self.path + "/" + ShiftItem.ShiftH5FilePath
                if path in h5f:
                    group = h5f.get(path)
                    if group:
                        self.__shiftFile = group.file.filename
                    del group
        return self.__shiftFile

    @shiftFile.setter
    def shiftFile(self, shiftFile):
        """Set the Shift data file for this item. The Shift data
        file can only be set once. To use a different data file you have to
        create a new project."""
        # TODO : make sure file exists and is readable
        if self.shiftFile is not None:
            raise ValueError("Shift input file is already set.")

        # Adding the external link to the file
        self.__shiftFile = shiftFile
        path = self.path + "/" + ShiftItem.ShiftH5FilePath
        self.add_file_link(path, shiftFile, "/")
        self.setHidden(True, path)

        self._createItem()

    def _createItem(self):
        shiftFile = self.shiftFile
        if shiftFile is None:
            return
