"""This module provides Gaussian fit/Center-of-Mass QSpace reduction processing

It provides the :class:`PeakFitter` class to run QSpace histogram projection
on the axes and either a gaussian fit or Center-of-mass with optional
background subtraction.

- :class:`FitTypes`: QSpace reduction modes
- :class:`BackgroundTypes`: Background subtraction modes
"""

from .peak_fit import FitTypes, FitStatus, PeakFitter, FitResult  # noqa
from .peak_fit import BackgroundTypes, background_estimation  # noqa
