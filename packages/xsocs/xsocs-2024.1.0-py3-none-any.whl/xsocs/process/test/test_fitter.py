"""
Nominal tests for the Fitter class.
"""

import os
import shutil
import tempfile
import unittest

import numpy

from silx.utils.testutils import ParametricTestCase

from xsocs import config
from xsocs.test.utils import test_resources
from xsocs.process.fit import PeakFitter, FitResult, FitTypes, BackgroundTypes
from xsocs.io.QSpaceH5 import QSpaceH5


class TestPeakFitter(ParametricTestCase):
    """Unit tests of the qspace converter class."""

    @classmethod
    def setUpClass(cls):
        config.DEFAULT_PROCESS_NUMBER = 2  # Limit number of processes

        cls._qspace_resources = sorted(
            f for f in test_resources.getdir("qspace.zip") if f.endswith(".h5")
        )
        cls._fit_resources = sorted(
            f for f in test_resources.getdir("fit_2018_12.zip") if f.endswith(".h5")
        )

    def setUp(self):
        self._tmpTestDir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmpTestDir)
        self._tmpTestDir = None

    def _assertResultAlmostEqual(self, ref, result):
        """Compare FitResults are equal on Linux and almost equal on Windows

        :param FitResult ref:
        :param FitResult result:
        """
        self.assertTrue(ref.almost_equal(result))

    def test_gaussian(self):
        """Test gaussian fit"""
        for fit_f, qspace_f in zip(self._fit_resources, self._qspace_resources):
            with self.subTest(fit_f=fit_f, qspace_f=qspace_f):
                # Configure fitting
                fitter = PeakFitter(
                    qspace_f=qspace_f,
                    fit_type=FitTypes.GAUSSIAN,
                    background=BackgroundTypes.NONE,
                )
                self.assertEqual(fitter.status, fitter.READY)

                # Run processing
                fitter.peak_fit()
                self.assertEqual(fitter.status, fitter.DONE)

                # Compare results
                ref = FitResult.from_fit_h5(fit_f)
                self._assertResultAlmostEqual(ref, fitter.results)

                # Save as HDF5 and compare
                fit_filename = os.path.basename(fit_f)
                fit_out = os.path.join(self._tmpTestDir, fit_filename)
                fitter.results.to_fit_h5(fit_out)
                self._assertResultAlmostEqual(ref, FitResult.from_fit_h5(fit_out))

    def test_com(self):
        """Test Center-of-mass and Max reduction"""
        for qspace_f in self._qspace_resources:
            filename = os.path.basename(qspace_f)

            # Configure reduction
            fitter = PeakFitter(
                qspace_f=qspace_f,
                fit_type=FitTypes.CENTROID,
                background=BackgroundTypes.NONE,
            )
            self.assertEqual(fitter.status, fitter.READY)

            # Run processing
            fitter.peak_fit()
            self.assertEqual(fitter.status, fitter.DONE)

            # Test results with reference implementation
            for key, ref in self._qspace_com_result(qspace_f).items():
                for dim in range(3):
                    with self.subTest(
                        qspace_file=filename, dimension=dim, parameter=key
                    ):
                        self.assertTrue(
                            numpy.array_equal(
                                ref[dim], fitter.results.get_results(dim, key)
                            )
                        )

            # Save as HDF5 and check saved result
            fit_out = os.path.join(self._tmpTestDir, "com_result_" + filename + ".h5")
            fitter.results.to_fit_h5(fit_out)
            self.assertEqual(fitter.results, FitResult.from_fit_h5(fit_out))

    @staticmethod
    def _qspace_com_result(qspace_f):
        """Test implementation of QSpace COM results

        :param str qspace_f: HDF5 file name
        :return: Dict of results for each axis for each sample point
        :rtype: Dict[List[List[float]]]
        """
        result = {
            "COM": [[], [], []],
            "I_sum": [[], [], []],
            "I_max": [[], [], []],
            "Pos_max": [[], [], []],
        }

        with QSpaceH5(qspace_f) as qspaceh5:
            axes = qspaceh5.qspace_dimension_values

            hits = qspaceh5.histo
            hits = [hits.sum(2).sum(1), hits.sum(2).sum(0), hits.sum(1).sum(0)]

            for qspace in qspaceh5.qspace:
                projs = [
                    qspace.sum(2).sum(1) / hits[0],
                    qspace.sum(2).sum(0) / hits[1],
                    qspace.sum(1).sum(0) / hits[2],
                ]
                for dim in range(3):
                    result["I_max"][dim].append(numpy.max(projs[dim]))
                    q_sum = numpy.sum(projs[dim])
                    result["I_sum"][dim].append(q_sum)
                    result["COM"][dim].append(numpy.dot(projs[dim], axes[dim]) / q_sum)
                    result["Pos_max"][dim].append(axes[dim][numpy.argmax(projs[dim])])

        return result


def suite():
    loader = unittest.defaultTestLoader
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromTestCase(TestPeakFitter))
    return test_suite


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
