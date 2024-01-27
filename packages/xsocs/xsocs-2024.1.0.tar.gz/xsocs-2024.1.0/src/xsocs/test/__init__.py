"""Full xsocs test suite.
"""

import logging
import unittest

from .test_version import suite as test_version_suite
from ..process.test import suite as test_util_suite


logging.basicConfig()
logger = logging.getLogger(__name__)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_version_suite())
    test_suite.addTest(test_util_suite())
    return test_suite


def run_tests(verbosity=1):
    """Run test complete test_suite"""
    runner = unittest.TextTestRunner(verbosity=verbosity)
    if not runner.run(suite()).wasSuccessful():
        print("Test suite failed")
        return 1
    else:
        print("Test suite succeeded")
        return 0
