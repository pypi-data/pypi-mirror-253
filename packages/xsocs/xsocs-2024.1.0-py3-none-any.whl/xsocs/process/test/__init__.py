import unittest

from .test_parser import suite as test_parser_suite
from .test_merger import suite as test_merger_suite
from .test_qspace import suite as test_qspace_suite
from .test_fitter import suite as test_peakfit_suite


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_parser_suite())
    test_suite.addTest(test_merger_suite())
    test_suite.addTest(test_qspace_suite())
    test_suite.addTest(test_peakfit_suite())

    return test_suite
