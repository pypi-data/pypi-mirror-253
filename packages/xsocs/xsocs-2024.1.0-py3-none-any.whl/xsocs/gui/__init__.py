"""XSocs widgets"""

import logging

_logger = logging.getLogger(__name__)

# Import PyQt5 before importing silx.gui
try:
    import PyQt5.QtCore  # noqa: Forces silx to use PyQt5
except ImportError as e:
    _logger.error("Cannot load PyQt5: PyQt5 is required to run XSocs")
    raise e

from silx import resources as _silx_resources  # noqa
from silx.gui import colors as _colors  # noqa

# Set colormaps available from silx colormap dialog
_colors.setPreferredColormaps(
    ["viridis", "magma", "inferno", "plasma", "jet", "afmhot", "gray"]
)

# Add xsocs resources to silx resource management
_silx_resources.register_resource_directory("xsocs", "xsocs.resources")

from .gui import xsocs_main, merge_window, conversion_window  # noqa
