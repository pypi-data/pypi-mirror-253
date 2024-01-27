import numpy as np


from .XsocsH5Base import XsocsH5Base


class ShiftH5(XsocsH5Base):
    EntriesPath = "entries"
    CommonPath = "common"

    def __init__(self, h5_f, mode="r", **kwargs):
        super(ShiftH5, self).__init__(h5_f, mode=mode, **kwargs)

        with self._get_file() as h5_file:
            h5_file.require_group(self.EntriesPath)
            h5_file.require_group(self.CommonPath)

    def entries(self):
        """
        Returns the list of entries
        :return:
        """
        with self.item_context(self.EntriesPath) as ctx:
            return list(ctx.keys())

    def shift(self, entry):
        """
        Returns the shift for the given entry.
        :param entry:
        :return:
        """

        dsetPath = self.EntriesPath + "/{0}/shift_x".format(entry)
        shift_x = self._get_scalar_data(dsetPath)

        dsetPath = self.EntriesPath + "/{0}/shift_y".format(entry)
        shift_y = self._get_scalar_data(dsetPath)

        dsetPath = self.EntriesPath + "/{0}/grid_shift".format(entry)
        grid_shift = self._get_scalar_data(dsetPath)

        return {"shift_x": shift_x, "shift_y": shift_y, "grid_shift": grid_shift}

    def shifted_indices(self, entry):
        """
        Return the shifted indices for the given entry.
        :param entry:
        :return:
        """
        dsetPath = self.EntriesPath + "/{0}/indices".format(entry)
        return self._get_array_data(dsetPath)

    def is_snapped_to_grid(self):
        """
        Returns the "snapped to grid" flag. If True, then a regular grid
        coordinates was used to get the shifted indices, i.e : the jitter
        was not taken into account.
        :return:
        """
        dsetPath = self.CommonPath + "/snapped"
        return self._get_scalar_data(dsetPath)


class ShiftH5Writer(ShiftH5):
    ShiftValuesDType = np.float32
    """ numpy dtype of the shift values dataset """

    def __init__(self, h5_f, mode="a", **kwargs):
        super(ShiftH5Writer, self).__init__(h5_f, mode=mode, **kwargs)

    def create_entry(self, entry, n_points=None, raise_on_exists=True):
        """
        Creates a new entry.
        :param entry:
        :param n_points: the maximum number of indices to store. Setting
            this to the number of sample points for this scan
            will allow you to reuse this file with a different shift (i.e :
            with a different number of indices).
            If None, then the indice data set size for an entry will be set
            the first time the indices for that entry are set. Afterwards,
            an exception will be raised if the number of indices changes
            and is higher than the previous set.
        :param raise_on_exists: if True (default) then an exception will be
            raised if the entry already exists.
        :return:
        """
        if entry in self.entries():
            if raise_on_exists:
                raise ValueError("Entry {0} already exists.".format(entry))
            else:
                return

        with self._get_file() as h5_file:
            entryPath = self.EntriesPath + "/{0}".format(entry)
            h5_file.require_group(entryPath)

            if n_points:
                dsetPath = self.EntriesPath + "/{0}/indices".format(entry)
                self._create_dataset(
                    dsetPath, shape=(0,), dtype=np.int32, maxshape=(n_points,)
                )

            self.set_shift(entry, 0.0, 0.0)

    def set_shift(self, entry, dx, dy, grid_shift=None):
        """
        Sets the shift for the given entry.
        :param entry:
        :param dx:
        :param dy:
        :param grid_shift:
        :return:
        """
        dsetPath = self.EntriesPath + "/{0}/shift_x".format(entry)
        self._set_scalar_data(dsetPath, self.ShiftValuesDType(dx))

        dsetPath = self.EntriesPath + "/{0}/shift_y".format(entry)
        self._set_scalar_data(dsetPath, self.ShiftValuesDType(dy))

        if grid_shift is None:
            grid_shift = [0, 0]

        grid_shift = np.array(grid_shift, dtype=np.int32)

        dsetPath = self.EntriesPath + "/{0}/grid_shift".format(entry)
        self._set_scalar_data(dsetPath, grid_shift)

    def set_is_snapped_to_grid(self, snapped):
        """
        Sets the "snapped to grid" flag. If True, then a regular grid
        coordinates was used to get the shifted indices, i.e : the jitter
        was not taken into account.
        :param snapped:
        :return:
        """
        dsetPath = self.CommonPath + "/snapped"
        self._set_scalar_data(dsetPath, snapped)

    def set_shifted_indices(self, entry, indices):
        """
        Sets the shifted indices for that entry. If the indices for that
        entry were previously set, an attempt to resize the dataset will be
        made.
        :param entry:
        :param indices:
        :return:
        """
        dsetPath = self.EntriesPath + "/{0}/indices".format(entry)
        with self._get_file() as h5_f:
            if dsetPath not in h5_f:
                self._set_array_data(dsetPath, indices)
            else:
                h5_f[dsetPath].resize(indices.shape)
                self._set_array_data(dsetPath, indices)
