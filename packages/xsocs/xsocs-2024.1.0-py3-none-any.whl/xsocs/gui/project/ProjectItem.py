import weakref

import h5py
import numpy as np


from .ProjectDef import getItemClass
from ...io.XsocsH5Base import XsocsH5Base
from ...io.XsocsH5 import XsocsH5


def _getIInfo(h5File, h5Path):
    attrs = dict([(key, value) for key, value in h5File[h5Path].attrs.items()])
    itemClass = h5File.get(h5Path, getclass=True)
    itemLink = h5File.get(h5Path, getclass=True, getlink=True)
    return itemClass, itemLink, attrs


def setProjectItemFactory(factory):
    global _projectItemFactory
    if factory is None:
        _projectItemFactory = projectItemFactory
    else:
        _projectItemFactory = factory


def projectItemFactory(h5File, h5Path, mode=None):
    klass = None
    with h5py.File(h5File, mode="r") as h5f:
        attrs = h5f[h5Path].attrs
        if "XsocsClass" in attrs:
            xsocsClass = attrs["XsocsClass"]
            if hasattr(xsocsClass, "decode"):
                xsocsClass = xsocsClass.decode()
            klass = getItemClass(xsocsClass)
        del attrs

    if not klass:
        klass = ProjectItem
    return klass(h5File, h5Path, mode=mode)


_projectItemFactory = projectItemFactory


class ProjectItem(XsocsH5Base):
    # TODO : some consistency check when loading a file? Make sure the right

    InputPath = "/_input"
    XsocsH5FilePath = "/_input/XsocsH5File"
    PrivateDataPath = "_xsocs"
    ItemNamePath = "_xsocs/name"
    IsDeletedPath = "_xsocs/deleted"
    XsocsClass = None
    MaxNameLength = 1000

    gui = property(lambda self: self.__gui() if self.__gui is not None else None)

    def __init__(
        self, h5File, nodePath="/", mode="r", processLevel=None, data=None, gui=None
    ):
        # TODO : check if parent already has a child with the same name
        super(ProjectItem, self).__init__(h5File, mode=mode)
        self.__nodePath = nodePath
        self.__xsocsFile = None

        self.__gui = weakref.ref(gui) if gui is not None else None

        # TODO : improve (maybe check if attributes are already present
        if nodePath == "/":
            self.__setXsocsAttributes(self.XsocsClass, processLevel)

        if self._path_exists(nodePath):
            self._loadItem()
        else:
            with self._get_file() as h5f:
                if data is not None:
                    h5f[nodePath] = data
                else:
                    grp = h5f.require_group(nodePath)
                    privatePath = (
                        self.path.rstrip("/") + "/" + ProjectItem.PrivateDataPath
                    )
                    grp.require_group(ProjectItem.PrivateDataPath)
                    self.setHidden(True, privatePath)
                    # self.setItemName('')

                self.__setXsocsAttributes(self.XsocsClass, processLevel)
            self._createItem()

    @staticmethod
    def factory(h5File, h5Path):
        return _projectItemFactory(h5File, h5Path)

    def __setXsocsAttributes(self, xsocsClass, processLevel):
        if self.mode not in ("r",):
            with self._get_file() as h5f:
                item = h5f[self.path]
                if self.XsocsClass is not None and "XsocsClass" not in item.attrs:
                    # for some reason there was an error when using
                    # attrs.get(), so I had to use "not in" instead
                    item.attrs["XsocsClass"] = np.string_(xsocsClass)
                if processLevel is not None and item.attrs.get("XsocsLevel") is None:
                    item.attrs["XsocsLevel"] = processLevel
                del item

    def parent(self, classinfo=None):
        """
        Returns this Project item's parent. Or None if this is the toplevel
        item.
        :param classinfo: Only returns the first parent which is an instance
        of this class.
        :return:
        """
        parent = None
        filename = self.filename
        parentPath = self.path.rpartition("/")[0]
        if parentPath:
            parent = ProjectItem(filename, parentPath).cast()
            if classinfo is not None and not isinstance(parent, classinfo):
                parent = parent.parent(classinfo)

        return parent

    def children(self, classinfo=None):
        """
        Returns this items direct children.
        :param classinfo: Only returns children that are instances of this/those
            class, if any.
        :type classinfo: class or tuple of classes.
        :return:
        """
        children = []
        with self._get_file() as h5f:
            try:
                keys = list(h5f[self.path].keys())
            except AttributeError:
                return []
        pathTpl = self.path.rstrip("/") + "/{0}"
        for key in keys:
            child = self.factory(self.filename, pathTpl.format(key.lstrip("/")))
            if classinfo:
                if isinstance(child, classinfo):
                    children.append(child)
            else:
                children.append(child)
        return children

    def cast(self):
        return ProjectItem.factory(self.filename, self.path)

    def projectRoot(self):
        return ProjectItem(self.filename, "/", mode=self.mode).cast()

    def setHidden(self, hidden, path=None):
        if path is None:
            path = self.__nodePath
        self.set_attribute(path, "XsocsHidden", hidden)

    def isHidden(self, path=None):
        if path is None:
            path = self.__nodePath
        hidden = self.attribute(path, "XsocsHidden")
        return (hidden is not None and hidden) or False

    path = property(lambda self: self.__nodePath)
    """ The hdf5 path to this item. """

    @property
    def xsocsFile(self):
        """The name of the input data file."""
        if self.__xsocsFile is None:
            with self._get_file() as h5f:
                path = "/" + ProjectItem.XsocsH5FilePath
                group = h5f.get(path)
                if group:
                    self.__xsocsFile = group.file.filename
                del group
        return self.__xsocsFile

    @xsocsFile.setter
    def xsocsFile(self, xsocs_f):
        """Set the input data file for this Xsocs workspace. The input data
        file can only be set once. To use a different data file you have to
        create a new project."""
        # TODO : make sure file exists and is readable
        if self.xsocsFile is not None:
            raise ValueError("Xsocs input file is already set.")

        # Adding the external link to the file
        self.__xsocsFile = xsocs_f
        path = "/" + ProjectItem.XsocsH5FilePath
        self.add_file_link(path, xsocs_f, "/")
        self.setHidden(True, path=ProjectItem.InputPath)

        self._createItem()

    xsocsH5 = property(lambda self: XsocsH5(self.xsocsFile) if self.xsocsFile else None)

    @classmethod
    def load(cls, h5File, groupPath):
        with h5py.File(h5File, "r") as h5f:
            grp = h5f[groupPath]
            xsocsType = grp.attrs.get("XsocsType")
            del grp
            if xsocsType is None:
                return None
            klass = getItemClass(xsocsType)
            if klass is None:
                return None
        instance = klass(h5File, groupPath)
        return instance

    @property
    def processLevel(self):
        with self._get_file() as h5f:
            return h5f[self.__nodePath].attrs.get("XsocsLevel")

    @property
    def xsocsClass(self):
        return self.attribute(self.path, "XsocsClass")

    def setItemName(self, itemName):
        """
        Sets the item's custom name.
        :param itemName:
        :return:
        """
        itemName = np.string_(
            "{{0:<{0}}}".format(ProjectItem.MaxNameLength).format(itemName)
        )
        with self._get_file():
            self._set_scalar_data(self.path + "/" + self.ItemNamePath, itemName)

    def getItemName(self):
        """
        Returns the item's custom name.
        :return:
        """
        with self._get_file():
            itemName = self._get_scalar_data(self.path + "/" + self.ItemNamePath)
        if itemName is not None:
            if hasattr(itemName, "decode"):  # We get bytes with python3
                itemName = itemName.decode()
            return itemName.strip()
        else:
            return ""

    @property
    def customPath(self):
        """Path with custom item names if defined"""
        parent = self.parent()
        if parent is not None:
            path = parent.customPath
        else:
            path = ""

        customName = self.getItemName()
        if not customName:
            customName = self.path.split("/")[-1]

        return "/".join((path, customName))

    def _createItem(self):
        """
        Called when the xsocsh5 file is succesfuly called. This should be used
        to create the hdf5 file contents.
        :return:
        """
        pass

    def _loadItem(self):
        """
        Called when the xsocsh5 file is succesfuly called. This should be used
        to load the hdf5 file contents.
        :return:
        """
        pass
