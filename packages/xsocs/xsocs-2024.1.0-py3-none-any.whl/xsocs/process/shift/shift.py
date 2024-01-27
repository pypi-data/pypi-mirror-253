import os
import tempfile
from collections import OrderedDict, namedtuple

import numpy as np

import h5py

from ... import config


ShiftValue = namedtuple("ShiftValue", ["dx", "dy", "entry", "grid_shift"])


class ScanShift(object):
    def __init__(self, xsocs_h5, tmp_file=None):
        super(ScanShift, self).__init__()

        self.__xsocs_h5 = xsocs_h5
        self.__shifts = OrderedDict()

        if tmp_file is None:
            self.__tmp_dir = tempfile.mkdtemp()
            tmp_file = os.path.join(self.__tmp_dir, "tmp_shift.h5")

        self.__tmp_file = tmp_file

        self.__shifts = OrderedDict()
        self.__dirtyGrids = OrderedDict()
        self.__dirtyFrees = OrderedDict()
        self.__dirty = True

        self.__init_tmp()

    def __init_tmp(self):
        with h5py.File(self.__tmp_file, mode="a") as tmp_h5:
            ref_p0, ref_p1 = _get_ref_positions(self.__xsocs_h5)
            tmp_h5["ref_p0"] = ref_p0
            tmp_h5["ref_p1"] = ref_p1

    def set_shift(self, entry, dx, dy, grid_shift=None):
        self.__shifts[entry] = ShiftValue(
            dx=dx, dy=dy, entry=entry, grid_shift=grid_shift
        )
        self.__dirty = True
        self.__dirtyGrids[entry] = True
        self.__dirtyFrees[entry] = True

    def get_entry_intersection_indices(self, entry, grid=True):
        """
        Return the indices that intersect all other entries for the given
        entry.
        :param entry:
        :return:
        """
        full_intersection = self.get_intersection_indices(grid=grid)
        entry_indices = self.get_shifted_indices(entry, grid=grid, full=True)
        # intersec = np.where(np.in1d(entry_indices, full_intersection))

        filtered = np.where(entry_indices >= 0)[0]
        in1d = np.in1d(filtered, full_intersection)
        idx = np.where(in1d)[0]
        return entry_indices[filtered[idx]]

    def get_shifted_indices(self, entry, grid=True, full=True):
        """
        Returns the shifted indices for the given entry.
        :param grid:
        :return:
        """
        if grid is False:
            return self.free_shifted_indices(entry, full=full)
        else:
            return self.regular_grid_indices(entry, full=full)

    def get_intersection_indices(self, grid=True, progress_cb=None):
        """
        Returns the intersection of all entries.
        :param grid: set to True to shift all entries along a regular grid.
            Obviously only available if all points are on such a grid.
        :param progress_cb: function that will be called to notify the caller
            of the progress. The callback will be passed an integer value
            between 0 and 100 (complete).
        :return:
        """

        entries = list(self.__shifts.keys())
        n_entries = len(entries)

        if progress_cb:
            progress_cb(0)

        shifted_idx = self.get_shifted_indices(entries[0], grid=grid)

        idx_count = np.zeros(shifted_idx.shape)

        valid_idx = np.where(shifted_idx >= 0)
        idx_count[valid_idx] += 1

        for entry_idx, entry in enumerate(entries[1:]):
            if progress_cb:
                progress_cb(round(100 * (entry_idx + 1.0) / n_entries - 1))

            shifted_idx = self.get_shifted_indices(entry, grid=grid)
            valid_idx = np.where(shifted_idx >= 0)
            idx_count[valid_idx] += 1

        intersection_indices = np.arange(shifted_idx.size, dtype=np.int32)
        intersection_indices = intersection_indices[np.where(idx_count == len(entries))]

        if progress_cb:
            progress_cb(100)

        return intersection_indices

    def regular_grid_indices(self, entry, full=True):
        """
        Returns the shifted indices. Shift is forced on a regular grid.
        :param entry:
        :return:
        """

        xsocs_h5 = self.__xsocs_h5

        if not xsocs_h5.is_regular_grid(entry):
            raise ValueError("Scan is not a ragular grid.")

        shift = self.__shifts.get(entry)

        if shift is None:
            raise ValueError("Unknown entry.")

        if shift.grid_shift is None:
            grid_shift = [0, 0]
        else:
            grid_shift = shift.grid_shift

        if not self.__dirtyGrids[entry]:
            dsetPath = "/entries/{0}/grid_indices".format(entry)
            with h5py.File(self.__tmp_file, mode="r") as tmp_h5:
                shifted_idx = tmp_h5.get(dsetPath)[:]
        else:
            with xsocs_h5:
                scan_params = xsocs_h5.scan_params(entry)
                steps_0 = scan_params["motor_0_steps"]
                steps_1 = scan_params["motor_1_steps"]

                shift_col = grid_shift[0]
                shift_row = grid_shift[1]

                if shift_col == 0 and shift_row == 0:
                    shifted_idx = np.arange(steps_0 * steps_1, dtype=np.int32)
                else:
                    col_idx = np.tile(np.arange(steps_0), steps_1)
                    col_idx += shift_col

                    row_idx = np.repeat(np.arange(steps_1), steps_0)
                    row_idx += shift_row

                    if shift_col > 0:
                        valid_col = col_idx < scan_params["motor_0_steps"]
                    elif shift_col < 0:
                        valid_col = col_idx >= 0
                    else:
                        valid_col = np.full((steps_0 * steps_1,), True, dtype=bool)

                    if shift_row > 0:
                        valid_row = row_idx < scan_params["motor_1_steps"]
                    elif shift_row < 0:
                        valid_row = row_idx >= 0
                    else:
                        valid_row = np.full((steps_0 * steps_1,), True, dtype=bool)

                    valid_idx = np.where(np.logical_and(valid_row, valid_col))

                    shifted_idx = np.full((steps_0 * steps_1,), -1, dtype=np.int32)

                    shifted_idx[valid_idx] = (
                        row_idx[valid_idx] * steps_0 + col_idx[valid_idx]
                    )

            dsetPath = "/entries/{0}/grid_indices".format(entry)
            with h5py.File(self.__tmp_file, mode="a") as tmp_h5:
                if dsetPath not in tmp_h5:
                    tmp_h5.create_dataset(dsetPath, data=shifted_idx)
                else:
                    tmp_h5[dsetPath][:] = shifted_idx

                self.__dirtyGrids[entry] = False

        if not full:
            shifted_idx = shifted_idx[np.where(shifted_idx >= 0)]

        return shifted_idx

    def free_shifted_indices(self, entry, full=True):
        entry_shift = self.__shifts.get(entry)

        if entry_shift is None:
            raise ValueError("Unknown entry.")

        dx, dy = entry_shift.dx, entry_shift.dy
        if None in (dx, dy):
            raise ValueError("Shift not set for entry {0}.".format(entry))

        dsetPath = "/entries/{0}/free_indices".format(entry)
        if not self.__dirtyFrees[entry]:
            with h5py.File(self.__tmp_file, mode="r") as tmp_h5:
                shifted_idx = tmp_h5.get(dsetPath)[:]
        else:
            shifted_idx = _get_free_shifted_indices(
                entry, self.__xsocs_h5, self.__shifts, self.__tmp_file
            )
            with h5py.File(self.__tmp_file, mode="a") as tmp_h5:
                if dsetPath not in tmp_h5:
                    tmp_h5.create_dataset(dsetPath, data=shifted_idx)
                else:
                    tmp_h5[dsetPath][:] = shifted_idx

                self.__dirtyFrees[entry] = False

        if not full:
            shifted_idx = shifted_idx[np.where(shifted_idx >= 0)]

        return shifted_idx

    # def compute_indices(self):
    #     if self.__computed:
    #         return
    #
    #     xsocs_h5 = self.__xsocs_h5
    #
    #     entries = self.__shifts.keys()
    #
    #     ref_p0, ref_p1 = _get_ref_positions(xsocs_h5)
    #
    #     _get_distance(xsocs_h5, self.__shifts, ref_p0, ref_p1, self.__tmp_file)


def _get_distance(xsocs_h5, shifts, ref_p0, ref_p1, tmp_file):
    entries = xsocs_h5.entries()
    n_images = xsocs_h5.n_images(entries[0])

    refmat0 = np.zeros(shape=(n_images, n_images + 1), dtype=np.float32)
    refmat1 = np.zeros(shape=(n_images, n_images + 1), dtype=np.float32)
    refmat0[:] = np.matrix(ref_p0).transpose()
    refmat1[:] = np.matrix(ref_p1).transpose()
    refmat0[:, -1] = -1
    refmat1[:, -1] = -1

    curMat0 = np.zeros(shape=(n_images + 1, n_images), dtype=refmat0.dtype)
    np.fill_diagonal(curMat0, 1)
    curMat1 = np.zeros(shape=(n_images + 1, n_images), dtype=refmat1.dtype)
    np.fill_diagonal(curMat1, 1)

    diff0 = np.zeros(shape=(n_images, n_images), dtype=refmat0.dtype)
    diff1 = np.zeros(shape=(n_images, n_images), dtype=refmat1.dtype)

    with h5py.File(tmp_file, "w") as outh5:
        grp = outh5.require_group("entries/ref")
        grp["p0"] = ref_p0
        grp["p1"] = ref_p1

        idx_dset = outh5.require_dataset(
            "data/indices",
            (len(entries), n_images),
            dtype=np.int32,
            shuffle=True,
            compression=config.DEFAULT_HDF5_COMPRESSION,
            chunks=(1, n_images),
        )

        idx_counts = np.zeros(n_images, dtype=np.int32)

        for iEntry, entry in enumerate(entries):
            entryGrp = outh5.require_group("entries/{0}".format(entry))

            pos = xsocs_h5.scan_positions(entry)

            p0 = pos.pos_0 + shifts[entry][0]
            p1 = pos.pos_1 + shifts[entry][1]

            entryGrp["p0"] = p0
            entryGrp["p1"] = p1

            curMat0[-1, :] = p0
            curMat1[-1, :] = p1

            np.dot(refmat0, curMat0, out=diff0)
            np.dot(refmat1, curMat1, out=diff1)

            np.square(diff0, out=diff0)
            np.square(diff1, out=diff1)
            np.add(diff0, diff1, out=diff0)
            np.sqrt(diff0, out=diff0)

            entryGrp["dist"] = diff0

            idx = np.argmin(diff0, axis=0)

            entryGrp["idx"] = idx

            idx_dset[iEntry, :] = idx

            np.add.at(idx_counts, idx, 1)

        outh5["data/idxcount"] = idx_counts


def _get_free_shifted_indices(
    entry, xsocs_h5, shifts, tmp_file, ref_p0=None, ref_p1=None
):
    if ref_p0 is None or ref_p1 is None:
        with h5py.File(tmp_file, mode="r") as tmp_h5:
            if ref_p0 is None:
                ref_p0 = tmp_h5["ref_p0"][:]
            if ref_p1 is None:
                ref_p1 = tmp_h5["ref_p1"][:]

    n_images = xsocs_h5.n_images(entry)

    if n_images != ref_p0.size or n_images != ref_p1.size:
        raise ValueError("Invalid size for ref positions.")

    if n_images < 1000:
        ref_mtx_0 = np.zeros(shape=(n_images, n_images + 1), dtype=np.float32)
        ref_mtx_1 = np.zeros(shape=(n_images, n_images + 1), dtype=np.float32)
        ref_mtx_0[:] = np.matrix(ref_p0).transpose()
        ref_mtx_1[:] = np.matrix(ref_p1).transpose()
        ref_mtx_0[:, -1] = -1
        ref_mtx_1[:, -1] = -1

        to_mtx_0 = np.zeros(shape=(n_images + 1, n_images), dtype=ref_mtx_0.dtype)
        np.fill_diagonal(to_mtx_0, 1)
        to_mtx_1 = np.zeros(shape=(n_images + 1, n_images), dtype=ref_mtx_1.dtype)
        np.fill_diagonal(to_mtx_1, 1)

        diff_0 = np.zeros(shape=(n_images, n_images), dtype=ref_mtx_0.dtype)
        diff_1 = np.zeros(shape=(n_images, n_images), dtype=ref_mtx_1.dtype)

        idx_counts = np.zeros(n_images, dtype=np.int32)

        pos = xsocs_h5.scan_positions(entry)

        p0 = pos.pos_0 + shifts[entry].dx
        p1 = pos.pos_1 + shifts[entry].dy

        to_mtx_0[-1, :] = p0
        to_mtx_1[-1, :] = p1

        np.dot(ref_mtx_0, to_mtx_0, out=diff_0)

        np.dot(ref_mtx_1, to_mtx_1, out=diff_1)

        np.square(diff_0, out=diff_0)
        np.square(diff_1, out=diff_1)

        np.add(diff_0, diff_1, out=diff_0)
        np.sqrt(diff_0, out=diff_0)

    idx = np.argmin(diff_0, axis=1)

    np.add.at(idx_counts, idx, 1)

    invalid_idx = np.where(idx_counts != 1)

    shifted_idx = np.arange(n_images)
    shifted_idx[invalid_idx] = -1

    return shifted_idx


def _get_ref_positions(xsocs_h5):
    """
    Returns the "reference" position. All distances for each entry will
    be measure from this reference position.
    :param xsocs_h5:
    :return:
    """
    entries = xsocs_h5.entries()
    ref_pos = xsocs_h5.scan_positions(entries[0])
    ref_p0 = ref_pos.pos_0

    n_scans = len(entries)
    n_images = xsocs_h5.n_images(entries[0])

    refmtx0 = np.zeros((n_scans, n_images), dtype=ref_p0.dtype)
    refmtx1 = np.zeros((n_scans, n_images), dtype=ref_p0.dtype)

    for iEntry, entry in enumerate(entries):
        ref_pos = xsocs_h5.scan_positions(entry)
        refmtx0[iEntry] = ref_pos.pos_0
        refmtx1[iEntry] = ref_pos.pos_1

    ref_p0 = np.median(refmtx0, axis=0)
    ref_p1 = np.median(refmtx1, axis=0)

    return ref_p0, ref_p1
