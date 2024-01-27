"""
Nominal tests for the KmapMerger class.
"""

import os
import shutil
import tempfile
import unittest


from xsocs import config
from xsocs.test.utils import test_resources

from xsocs.process.merge.KmapMerger import KmapMerger
from xsocs.process.merge.KmapSpecParser import KmapSpecParser


# ==============================================================
# ==============================================================
# ==============================================================


class TestMerger(unittest.TestCase):
    """
    Unit tests of the merger class.
    """

    merged_files = {
        "test.h5",
        "test_340800_0000_46.1.h5",
        "test_341000_0000_48.1.h5",
        "test_341200_0000_50.1.h5",
        "test_341400_0000_52.1.h5",
        "test_341600_0000_54.1.h5",
        "test_341800_0000_56.1.h5",
        "test_342000_0000_58.1.h5",
        "test_342200_0000_60.1.h5",
        "test_342400_0000_62.1.h5",
        "test_342600_0000_64.1.h5",
        "test_342800_0000_66.1.h5",
        "test_343000_0000_68.1.h5",
        "test_343200_0000_70.1.h5",
        "test_343400_0000_72.1.h5",
        "test_343600_0000_74.1.h5",
        "test_343800_0000_76.1.h5",
        "test_344000_0000_78.1.h5",
        "test_344200_0000_80.1.h5",
    }

    matched_ids = ["{0}.1".format(idx) for idx in range(46, 82, 2)]

    @classmethod
    def setUpClass(cls):
        config.DEFAULT_PROCESS_NUMBER = 2  # Limit number of processes

        cls._tmpdir = tempfile.mkdtemp()
        cls._spec_h5 = os.path.join(cls._tmpdir, "spec_h5.h5")
        spec_resources = test_resources.getdir("spec.zip")
        spec_f = [f for f in spec_resources if f.endswith("spec/test.spec")][0]
        img_dir = os.path.dirname(
            [f for f in spec_resources if f.endswith("img/test_340800_0000.edf.gz")][0]
        )

        parser = cls._parser = KmapSpecParser(
            spec_f, cls._spec_h5, img_dir=img_dir, version=0
        )

        parser.parse()

    @classmethod
    def tearDownClass(cls):
        tmpdir = cls._tmpdir
        if tmpdir is not None:
            shutil.rmtree(tmpdir)
        cls._tmpdir = None

    def setUp(self):
        self._tmpTestDir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmpTestDir)
        self._tmpTestDir = None

    def test_nominal(self):
        """ """
        output_dir = os.path.join(self._tmpTestDir, "merged")

        if os.path.isdir(output_dir):
            shutil.rmtree(output_dir)

        merger = KmapMerger(self._spec_h5, self._parser.results, output_dir=output_dir)
        merger.center_chan = 140, 322
        merger.chan_per_deg = 318, 318
        merger.beam_energy = 8000

        self.assertEqual(merger.status, merger.READY, msg=merger.statusMsg)

        merger.merge()

        self.assertEqual(merger.status, merger.DONE, msg=merger.statusMsg)

        summary = merger.summary(fullpath=True)
        summary_set = set([merged_f for merged_f in summary.values()])
        expected_set = set(
            [os.path.join(output_dir, merged_f) for merged_f in self.merged_files]
        )

        self.assertEqual(summary_set, expected_set)

        exists = all([os.path.isfile(merged_f) for merged_f in expected_set])
        self.assertTrue(exists)

    def test_image_roi(self):
        """Run merge with image ROI"""
        output_dir = os.path.join(self._tmpTestDir, "merged")

        if os.path.isdir(output_dir):
            shutil.rmtree(output_dir)

        merger = KmapMerger(self._spec_h5, self._parser.results, output_dir=output_dir)
        merger.center_chan = 140, 322
        merger.chan_per_deg = 318, 318
        merger.beam_energy = 8000

        merger.image_roi = 10, 20, 30, 300

        self.assertEqual(merger.status, merger.READY, msg=merger.statusMsg)

        merger.merge()

        self.assertEqual(merger.status, merger.DONE, msg=merger.statusMsg)

        summary = merger.summary(fullpath=True)
        summary_set = set([merged_f for merged_f in summary.values()])
        expected_set = set(
            [os.path.join(output_dir, merged_f) for merged_f in self.merged_files]
        )

        self.assertEqual(summary_set, expected_set)

        exists = all([os.path.isfile(merged_f) for merged_f in expected_set])
        self.assertTrue(exists)


# ==============================================================
# ==============================================================
# ==============================================================


test_cases = (TestMerger,)


def suite():
    loader = unittest.defaultTestLoader
    test_suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    return test_suite


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
