"""Nominal tests for QSpaceConverter class."""

import os
import shutil
import tempfile
import unittest

import numpy as np

from silx.utils.testutils import ParametricTestCase

from xsocs import config
from xsocs.test.utils import test_resources

from xsocs.io.QSpaceH5 import QSpaceH5
from xsocs.io.XsocsH5 import XsocsH5
from xsocs.process.qspace.QSpaceConverter import QSpaceConverter


class TestQSpace(ParametricTestCase):
    """Unit tests of the QSpaceConverter class."""

    @classmethod
    def setUpClass(cls):
        config.DEFAULT_PROCESS_NUMBER = 2  # Limit number of processes

        cls._tmpdir = tempfile.mkdtemp()

        cls._resources = {
            "merged": test_resources.getdir("merged.zip"),
            "qspace": test_resources.getdir("qspace.zip"),
        }

    @classmethod
    def tearDownClass(cls):
        tmpdir = cls._tmpdir
        if tmpdir is not None:
            shutil.rmtree(tmpdir)
        cls._tmpdir = None

    def _get_resource(self, namespace, filename):
        """Returns the filename of a resource

        :param str namespace: Either 'merged' or 'qspace'
        :param str filename: The filename to get
        :rtype: str
        """
        for f in self._resources[namespace]:
            if f.endswith(filename):
                return f

    def setUp(self):
        self._tmpTestDir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmpTestDir)
        self._tmpTestDir = None

    def test_nominal(self):
        """Test of QSpaceConverter"""
        master_f = self._get_resource("merged", "test.h5")

        keys = ["output_f", "medfilt_dims", "mask"]
        parameters = [
            ("qspace_1.h5", None, None),
            ("qspace_3.h5", [3, 3], None),
            ("qspace_5.h5", None, "mask.npy"),
        ]
        param_dicts = [dict(zip(keys, params)) for params in parameters]

        for params in param_dicts:
            with self.subTest(**params):
                output_f = os.path.join(self._tmpTestDir, params["output_f"])

                converter = QSpaceConverter(
                    master_f,
                    qspace_dims=[28, 154, 60],
                    medfilt_dims=params["medfilt_dims"],
                    output_f=output_f,
                )
                self.assertEqual(converter.status, converter.READY)

                maskFilename = params["mask"]
                if maskFilename is not None:  # Load mask
                    filename = self._get_resource("qspace", maskFilename)
                    mask = np.load(filename)
                    converter.mask = mask

                converter.convert()

                self.assertEqual(
                    converter.status, converter.DONE, msg=converter.status_msg
                )

                q_ref = self._get_resource("qspace", params["output_f"])
                q_out = converter.results

                q_ref_h5 = QSpaceH5(q_ref)
                q_out_h5 = QSpaceH5(q_out)

                with q_ref_h5.qspace_dset_ctx() as ref_ctx:
                    with q_out_h5.qspace_dset_ctx() as out_ctx:
                        self.assertEqual(ref_ctx.shape, out_ctx.shape)
                        self.assertEqual(ref_ctx.dtype, out_ctx.dtype)
                        self.assertTrue(np.array_equal(ref_ctx, out_ctx))

    def test_normalization(self):
        """Test QSpaceConverter with normalization"""
        output_f = os.path.join(self._tmpTestDir, "qspace_normalization.h5")
        master_f = self._get_resource("merged", "test.h5")
        normalizer = "ccdint1"

        master_h5 = XsocsH5(master_f)
        entries = master_h5.entries()

        # Compute reference sum of each qspace from images
        normalization = [master_h5.measurement(e, normalizer) for e in entries]
        images_sum = np.array(
            [master_h5.image_cumul(e) for e in entries], dtype=np.float64
        )
        images_sum /= np.array(normalization, dtype=np.float64)
        ref_sum = np.sum(images_sum, axis=0)

        # Convert to QSpace
        converter = QSpaceConverter(
            master_f, output_f=output_f, qspace_dims=[20, 20, 20], entries=entries
        )
        converter.normalizer = normalizer

        converter.convert()

        self.assertEqual(converter.status, converter.DONE, msg=converter.status_msg)

        q_normalized_h5 = QSpaceH5(converter.results)
        self.assertEqual(q_normalized_h5.image_normalizer, normalizer)
        self.assertEqual(q_normalized_h5.qspace_dimensions, (20, 20, 20))

        # Compute sum of each qspace and compare to ref
        with q_normalized_h5.qspace_dset_ctx() as out_ctx:
            data = np.array(out_ctx, dtype=np.float64)
            normed_sum = [np.sum(histo) for histo in data]

        self.assertTrue(np.allclose(ref_sum, normed_sum, atol=1e-6, rtol=0.0))


def suite():
    loader = unittest.defaultTestLoader
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromTestCase(TestQSpace))
    return test_suite


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
