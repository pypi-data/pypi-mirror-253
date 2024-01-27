import os as _os
import logging as _logging
from ._config import Config as _Config

config = _Config()
"""Global configuration shared with the whole library"""

# Attach a do nothing logging handler for xsocs
_logging.getLogger(__name__).addHandler(_logging.NullHandler())


project = _os.path.basename(_os.path.dirname(_os.path.abspath(__file__)))

from ._version import version, version_info, hexversion, strictversion  # noqa

# Set OpenMP to use a single thread (for median filter)
_os.environ["OMP_NUM_THREADS"] = "1"
