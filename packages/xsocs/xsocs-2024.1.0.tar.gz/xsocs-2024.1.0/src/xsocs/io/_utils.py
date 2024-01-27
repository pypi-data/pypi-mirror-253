"""Useful functions for HDF5 files"""

import numpy
import h5py


def str_to_h5_utf8(text):
    """Convert text to the appropriate unicode type

    :param Union[str,List[str]] text:
    :return: Input converted to a format appropriate for h5py
    :rtype: numpy.ndarray
    """
    return numpy.array(text, dtype=h5py.special_dtype(vlen=str))


def find_NX_class(group, nx_class):
    """Yield name of items in group of nx_class NX_class

    :param h5py.Group group:
    :param str nx_class:
    :rtype: Iterable[str]
    """
    for key, item in group.items():
        cls = item.attrs.get("NX_class", "")
        if hasattr(cls, "decode"):
            cls = cls.decode()
        if cls == nx_class:
            yield key
