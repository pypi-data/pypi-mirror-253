"""This module provides the API to convert SPEC+EDF to HDF5 files.

It provides a helper function :func:`merge_scan_data` to perform the merge.
"""

from .KmapMerger import KmapMerger  # noqa
from .KmapSpecParser import KmapSpecParser  # noqa
from .helpers import merge_scan_data  # noqa
