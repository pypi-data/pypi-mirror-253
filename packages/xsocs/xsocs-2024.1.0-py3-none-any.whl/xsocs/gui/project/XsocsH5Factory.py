import logging

from .Hdf5Nodes import H5Base, H5NodeFactory
from .ProjectItem import ProjectItem


_logger = logging.getLogger(__name__)


def h5NodeToProjectItem(h5Node, mode="r", cast=True):
    if not isinstance(h5Node, H5Base):
        return None
    try:
        item = ProjectItem(h5Node.h5File, nodePath=h5Node.h5Path, mode=mode)
    except Exception as ex:
        _logger.error(ex)
        raise

    if cast:
        item = item.cast()
    return item


def XsocsH5Factory(h5File, h5Path):
    node = H5NodeFactory(h5File, h5Path)
    if node.isValid():
        item = h5NodeToProjectItem(node, cast=False)
        if item and item.isHidden():
            node.hidden = True
    return node
