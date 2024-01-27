import os

from ...io.FitH5 import FitH5
from .ProjectItem import ProjectItem
from .ProjectDef import ItemClassDef


@ItemClassDef("FitGroup")
class FitGroup(ProjectItem):
    """Project item containing a group of fit results."""

    def addFitFile(self, fitFile):
        """
        Adds a fit result file to this group. Creates a FitItem.
        :param fitFile:
        :return:
        """
        itemName = os.path.basename(fitFile).rsplit(".")[0]
        itemPath = self.path + "/" + itemName
        item = FitItem(self.filename, itemPath, mode="a")
        item.fitFile = fitFile
        return item

    def getFitItems(self):
        """
        Returns all fit items in this group.
        :return:
        """
        return self.children(classinfo=FitItem)


@ItemClassDef("FitItem")
class FitItem(ProjectItem):
    """Project item linked to a Fit result files."""

    FitH5FilePath = "input"

    def __init__(self, *args, **kwargs):
        self.__fitFile = None
        super(FitItem, self).__init__(*args, **kwargs)

    fitH5 = property(lambda self: FitH5(self.fitFile) if self.fitFile else None)

    @property
    def fitFile(self):
        """The name of the input data file."""
        if self.__fitFile is None:
            with self._get_file() as h5f:
                path = self.path + "/" + FitItem.FitH5FilePath
                if path in h5f:
                    group = h5f.get(path)
                    if group:
                        self.__fitFile = group.file.filename
                    del group
        return self.__fitFile

    @fitFile.setter
    def fitFile(self, fitFile):
        """Set the fit data file for this item. The fit data
        file can only be set once. To use a different data file you have to
        create a new project."""
        # TODO : make sure file exists and is readable
        if self.fitFile is not None:
            raise ValueError("Fit input file is already set.")

        # Adding the external link to the file
        self.__fitFile = fitFile
        path = self.path + "/" + FitItem.FitH5FilePath
        self.add_file_link(path, fitFile, "/")
        self.setHidden(True, path)

        self._createItem()

    def _createItem(self):
        fitFile = self.fitFile
        if fitFile is None:
            return
