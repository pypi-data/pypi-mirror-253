"""This module contains library wide configuration.
"""

from multiprocessing import cpu_count
import os


class Config(object):
    """
    Class containing shared global configuration for the silx library.
    """

    DEFAULT_PROCESS_NUMBER = max(
        1,
        (
            len(os.sched_getaffinity(0))
            if hasattr(os, "sched_getaffinity")
            else cpu_count()
        ),
    )
    """Default max number of processes to use (Use number of core by default)

    This value must be strictly positive.
    """

    USE_OPENGL = True
    """True to use OpenGL widgets (default), False to disable."""

    DEFAULT_HDF5_COMPRESSION = "gzip"
    """Default HDF5 dataset compression scheme"""
