import weakref
from collections import OrderedDict
from contextlib import contextmanager

import numpy as _np

from .XsocsH5Base import XsocsH5Base
from .. import config
from ._utils import str_to_h5_utf8


class QSpaceCoordinates(object):
    """Kind of QSpace coordinate system"""

    CARTESIAN = "cartesian"
    """Cartesian coordinates: (x, y, z)"""

    SPHERICAL = "spherical"
    """Spherical coordinates (ISO): (pitch, roll, radial)"""

    ALLOWED = CARTESIAN, SPHERICAL
    """Supported coordinate systems"""

    @classmethod
    def axes_names(cls, coordinates):
        """Returns axes names for a coordinate system"""
        if coordinates == cls.CARTESIAN:
            return "qx", "qy", "qz"
        elif coordinates == cls.SPHERICAL:
            return "pitch", "roll", "radial"
        else:
            raise ValueError("Unsupported coordinates argument")


class QSpaceH5(XsocsH5Base):
    """Class accessing QSpace information in xsocs HDF5 file

    :param str h5_f: HDF5 file name
    :param str mode: Mode to use to open the file
    """

    # Path to use within hdf5 file
    _DATA_PATH = "Data"
    _QSPACE_PATH = "Data/qspace"
    _HISTO_PATH = "Data/histo"
    _SAMPLE_X_PATH = "Data/sample_x"
    _SAMPLE_Y_PATH = "Data/sample_y"
    _QSPACE_SUM_PATH = "Data/qspace_sum"
    _PARAMS_PATH = "Params/"
    _ENTRIES_PATH = "params/entries"

    def __init__(self, h5_f, mode="r"):
        super(QSpaceH5, self).__init__(h5_f, mode=mode)

    @contextmanager
    def qspace_dset_ctx(self):
        """Context manager for the image dataset.

        WARNING: only to be used as a context manager!
        WARNING: the data set must exist. see also QSpaceH5Writer.init_cube
        """
        with self._get_file() as h5_file:
            qspace_dset = h5_file[self._QSPACE_PATH]
            yield weakref.proxy(qspace_dset)
            del qspace_dset

    @contextmanager
    def qspace_sum_dset_ctx(self):
        """Context manager for the image dataset.

        WARNING: only to be used as a context manager!
        WARNING: the data set must exist. see also QSpaceH5Writer.init_cube
        """
        with self._get_file() as h5_file:
            qspace_sum_dset = h5_file[self._QSPACE_SUM_PATH]
            yield weakref.proxy(qspace_sum_dset)
            del qspace_sum_dset

    qspace = property(
        lambda self: self._get_array_data(self._QSPACE_PATH),
        doc="Stack of QSpace (4D stack)",
    )

    def qspace_slice(self, index):
        """Returns the 3D QSpace at index

        :param int index:
        :rtype: numpy.ndarray
        """
        with self.item_context(self._QSPACE_PATH) as dset:
            return dset[index]

    @property
    def qspace_dimension_names(self):
        """Returns the names of the QSpace axes for dataset dimension 1, 2, 3

        :rtype: List[str]
        """
        # Try to get NXdata axes, else use cartesian (backward compatible)
        with self._get_file() as h5f:
            axes = h5f[self._DATA_PATH].attrs.get("axes", (".", "qx", "qy", "qz"))
        return tuple(axes[1:])

    @property
    def qspace_dimension_values(self):
        """Retrieve QSpace axes values for QSpace dataset dimension 1, 2 and 3.

        :rtype: List[numpy.ndarray]
        """
        return tuple(
            [
                self._get_array_data("/".join((self._DATA_PATH, name)))
                for name in self.qspace_dimension_names
            ]
        )

    sample_x = property(lambda self: self._get_array_data(self._SAMPLE_X_PATH))

    sample_y = property(lambda self: self._get_array_data(self._SAMPLE_Y_PATH))

    histo = property(lambda self: self._get_array_data(self._HISTO_PATH))

    qspace_sum = property(lambda self: self._get_array_data(self._QSPACE_SUM_PATH))

    @property
    def selected_entries(self):
        """Returns the input entries used for the conversion."""
        path = self._ENTRIES_PATH + "/selected"
        entries = self._get_array_str(path)
        return entries if entries is not None else []

    @property
    def shifts(self):
        """
        Returns the shift that was applied to each of the selected entries,
        or None if no shift was applied to any of the selected entries.

        :return: A dictionary {entry: {'shift':[x, y], 'grid_shift':[n, m]}
            shift (grid_shift) is None if the shift (grid_shift) was not set.
        """
        with self:
            entries = self.selected_entries

            shifts = OrderedDict()

            has_shift_path = self._ENTRIES_PATH + "/has_grid_shift"
            has_shift = self._get_scalar_data(has_shift_path)
            has_grid_path = self._ENTRIES_PATH + "/has_grid_shift"
            has_grid_shift = self._get_scalar_data(has_grid_path)

            shift_path = self._ENTRIES_PATH + "/shifts/{0}/shift"
            grid_shift_path = self._ENTRIES_PATH + "/shifts/{0}/grid_shift"

            if not has_shift and not has_grid_shift:
                return None

            for entry in entries:
                if not has_grid_shift:
                    grid_shift = None
                else:
                    grid_shift = self._get_array_data(grid_shift_path.format(entry))

                if not has_shift:
                    shift = None
                else:
                    shift = self._get_array_data(shift_path.format(entry))
                shifts[entry] = {"shift": shift, "grid_shift": grid_shift}

            return shifts

    @property
    def discarded_entries(self):
        """
        Returns the input entries that were not used for the conversion.
        """
        path = self._ENTRIES_PATH + "/discarded"
        entries = self._get_array_str(path)
        return entries if entries is not None else []

    @property
    def image_mask(self):
        """Returns the mask selecting pixels in images.

        Non-zero value means that the pixel is masked.

        :rtype: Union[numpy.ndarray,None]
        """
        return self._get_array_data(self._PARAMS_PATH + "/image_mask")

    @property
    def image_normalizer(self):
        """Returns the image normalizer used when converting to q space.

        :rtype: Union[str,None]
        """
        return self._get_array_data(self._PARAMS_PATH + "/image_normalizer")

    @property
    def maxipix_correction(self):
        """Returns whether maxipix correction was enabled or not.

        :rtype: Union[int,None]
        """
        return self._get_scalar_data(self._PARAMS_PATH + "/maxipix_correction")

    @property
    def image_binning(self):
        """Returns the image binning used when converting to q space.

        This is deprecated as no more created during conversion.
        It is kept for displaying the information for files
        produced with older version of xsocs.
        """
        path = self._PARAMS_PATH + "/image_binning"
        return self._get_array_data(path)

    @property
    def medfilt_dims(self):
        """
        Returns the dimensions of the median filter applied when
        converting to q space.
        """
        path = self._PARAMS_PATH + "/medfilt_dims"
        return self._get_array_data(path)

    @property
    def sample_roi(self):
        """
        Returns the sample area selected for conversion (sample coordinates).

        :return: 4 elements array : xMin, xMax, yMin, yMax
        """
        path = self._PARAMS_PATH + "/sample_roi"
        sample_roi = self._get_array_data(path)
        if sample_roi is None:
            return [_np.nan, _np.nan, _np.nan, _np.nan]
        return sample_roi

    @property
    def qspace_dimensions(self):
        """Returns the dimensions of the qspace cubes"""
        with self.qspace_dset_ctx() as dset:
            return dset.shape[1:]

    @property
    def beam_energy(self):
        """Returns the beam energy in eV.

        It might be None if not stored.
        """
        return self._get_scalar_data(self._PARAMS_PATH + "/beam_energy")

    @property
    def direct_beam(self):
        """Returns direct beam calibration position.

        It might be None if not stored.
        """
        return self._get_array_data(self._PARAMS_PATH + "/direct_beam")

    @property
    def channels_per_degree(self):
        """Returns channels per degree calibration.

        It might be None if not stored.
        """
        return self._get_array_data(self._PARAMS_PATH + "/channels_per_degree")


class QSpaceH5Writer(QSpaceH5):
    """Class writing QSpace information in xsocs HDF5 file

    :param str h5_f: HDF5 file name
    :param str mode: Mode to use to open the file
    """

    def __init__(self, h5_f, mode="a"):
        self.mode = mode
        super(QSpaceH5Writer, self).__init__(h5_f, mode=mode)
        self.__cube_init = False

    def init_file(
        self,
        n_positions,
        qspace_shape,
        qspace_chunks=None,
        qspace_sum_chunks=None,
        compression="DEFAULT",
        coordinates=QSpaceCoordinates.CARTESIAN,
    ):
        """Creates empty datasets in the file if not yet created

        :param int n_positions: Number of positions on the sample
        :param List[int] qspace_shape: shape of the QSpace to store as 3 int
        :param qspace_chunks: Chunking to use for QSpace dataset
        :param qspace_sum_chunks: Chunking to use for integrated intensity dataset
        :param Union[str,None] compression:
            Compression of QSpace and integrated intensity dataset
        :param QSpaceCoordinates coordinates: Coordinate system to use
        """
        if compression == "DEFAULT":
            compression = config.DEFAULT_HDF5_COMPRESSION

        # TODO : mode this to XsocsH5Base ('init_dataset')
        if not self.__cube_init:
            cube_dtype = _np.float32
            histo_dtype = _np.int32
            position_dtype = _np.float64
            q_bins_dtype = _np.float64

            axis_names = QSpaceCoordinates.axes_names(coordinates)

            dataset_info = [  # path, shape, dtype, chunks for each dataset
                (
                    self._QSPACE_PATH,
                    (n_positions,) + qspace_shape,
                    cube_dtype,
                    qspace_chunks,
                ),
                (
                    self._DATA_PATH + "/" + axis_names[0],
                    qspace_shape[0:1],
                    q_bins_dtype,
                    None,
                ),
                (
                    self._DATA_PATH + "/" + axis_names[1],
                    qspace_shape[1:2],
                    q_bins_dtype,
                    None,
                ),
                (
                    self._DATA_PATH + "/" + axis_names[2],
                    qspace_shape[2:3],
                    q_bins_dtype,
                    None,
                ),
                (self._HISTO_PATH, qspace_shape, histo_dtype, None),
                (self._SAMPLE_X_PATH, (n_positions,), position_dtype, None),
                (self._SAMPLE_Y_PATH, (n_positions,), position_dtype, None),
                (self._QSPACE_SUM_PATH, (n_positions,), cube_dtype, qspace_sum_chunks),
            ]

            with self._get_file() as h5f:
                # Create empty datasets
                for path, shape, dtype, chunks in dataset_info:
                    h5f.require_dataset(
                        path,
                        shape=shape,
                        dtype=dtype,
                        compression=compression,
                        chunks=chunks,
                    )

                # Create NXdata structure
                group = h5f[self._DATA_PATH]
                group.attrs["NX_class"] = str_to_h5_utf8("NXdata")
                group.attrs["signal"] = str_to_h5_utf8(self._QSPACE_PATH.split("/")[-1])
                group.attrs["axes"] = str_to_h5_utf8((".",) + axis_names)

    def set_qspace_dimension_values(self, dim0, dim1, dim2):
        """Set the axes values of the QSpace dataset for dimension 1, 2, 3.

        :param numpy.ndarray dim0:
        :param numpy.ndarray dim1:
        :param numpy.ndarray dim2:
        """
        for name, array in zip(self.qspace_dimension_names, (dim0, dim1, dim2)):
            self._set_array_data(self._DATA_PATH + "/" + name, array)

    def set_sample_x(self, sample_x):
        """Set X coordinates on the sample for each QSpace

        :param numpy.ndarray sample_x:
        """
        self._set_array_data(self._SAMPLE_X_PATH, sample_x)

    def set_sample_y(self, sample_y):
        """Set Y coordinates on the sample for each QSpace

        :param numpy.ndarray sample_y:
        """
        self._set_array_data(self._SAMPLE_Y_PATH, sample_y)

    def set_histo(self, histo):
        """Set the count for each bin of the QSpace

        :param numpy.ndarray histo:
        """
        self._set_array_data(self._HISTO_PATH, histo)

    def set_qspace_sum(self, qspace_sum):
        """Set the integrated intensity of each QSpace

        :param numpy.ndarray qspace_sum:
        """
        self._set_array_data(self._QSPACE_SUM_PATH, qspace_sum)

    def set_position_data(self, pos_idx, qspace, qspace_sum):
        """Set the QSpace and integrated intensity for a given point

        :param int pos_idx: Sample position index
        :param numpy.ndarray qspace: 3D qspace dataset
        :param float qspace_sum: Corresponding integrated intensity
        """
        with self._get_file() as h5f:
            h5f[self._QSPACE_PATH][pos_idx] = qspace
            h5f[self._QSPACE_SUM_PATH][pos_idx] = qspace_sum

    def set_entries(
        self, selected, discarded=None, sample_shifts=None, grid_shifts=None
    ):
        """Sets the input entries that were converted to qspace.

        :param selected: Selected entry names
        :param discarded: List of input entries that were discarded, or None.
        :param sample_shifts: x and y shift that was applied to each selected
            entry. It must be a numpy array of dimension [n, 2] where n is the
            number of selected entries. The shift is in sample positions
            (microns?).
        :param grid_shifts: regular grid_shift that was applied to each selected
            entry. It must be a numpy array of dimension [n, 2] where n is the
            number of selected entries. The shift is in grid coordinates.
        """
        path = self._ENTRIES_PATH + "/selected"
        selected = str_to_h5_utf8(selected)
        self._set_array_data(path, selected)
        path = self._ENTRIES_PATH + "/discarded"
        discarded = str_to_h5_utf8(discarded if discarded is not None else [])
        self._set_array_data(path, discarded)

        if sample_shifts is not None:
            sample_shifts = _np.array(sample_shifts, ndmin=2, dtype=_np.float64)
            if sample_shifts.shape != (len(selected), 2):
                raise ValueError(
                    "Expected sample_shift of shape {0}, "
                    "received {1} instead."
                    "".format((len(selected), 2), sample_shifts.shape)
                )
            path = self._ENTRIES_PATH + "/shifts/{0}/shift"
            for e_idx, entry in enumerate(selected):
                entry_path = path.format(entry)
                self._set_array_data(entry_path, sample_shifts[e_idx])
            has_shift = True
        else:
            has_shift = False

        if grid_shifts is not None:
            grid_shifts = _np.array(grid_shifts, ndmin=2, dtype=_np.int64)
            if grid_shifts.shape != (len(selected), 2):
                raise ValueError(
                    "Expected grid_shift of shape {0}, "
                    "received {1} instead."
                    "".format((len(selected), 2), grid_shifts.shape)
                )
            path = self._ENTRIES_PATH + "/shifts/{0}/grid_shift"
            for e_idx, entry in enumerate(selected):
                entry_path = path.format(entry)
                self._set_array_data(entry_path, grid_shifts[e_idx])

            has_grid_shift = True
        else:
            has_grid_shift = False

        # this is set just in case the set_entries is called twice on the same
        # file with a different list of entries (and the number of entries
        # is the same for each calls, in which case no exception will
        # be raised)
        path = self._ENTRIES_PATH + "/has_grid_shift"
        self._set_scalar_data(path, has_grid_shift)
        path = self._ENTRIES_PATH + "/has_shift"
        self._set_scalar_data(path, has_shift)

    def set_image_mask(self, mask):
        """Stores the image mask used when converting to q space

        :param numpy.ndarray mask: Mask as a 2D image
        """
        if mask is not None:
            path = self._PARAMS_PATH + "/image_mask"
            self._create_dataset(path, data=mask)

    def set_image_normalizer(self, normalizer):
        """Stores the image normalizer used when converting to q space

        :param str normalizer:
            Name of measurement group dataset to use
        """
        path = self._PARAMS_PATH + "/image_normalizer"
        self._create_dataset(path, data=str(normalizer))

    def set_medfilt_dims(self, medfilt_dims):
        """
        Stores the dimensions of the median filter applied when
        converting to q space.

        :param medfilt_dims: a 2 elements array.
        """
        path = self._PARAMS_PATH + "/medfilt_dims"
        if medfilt_dims is None or len(medfilt_dims) != 2:
            raise ValueError(
                "medfilt_dims must be a 2 elements array : " "{0}.".format(medfilt_dims)
            )
        self._set_array_data(path, _np.array(medfilt_dims))

    def set_sample_roi(self, sample_roi):
        """
        Stores the sample area selected for conversion (sample coordinates).

        :param sample_roi: 4 elements array : xMin, xMax, yMin, yMax
        """
        path = self._PARAMS_PATH + "/sample_roi"
        if sample_roi is None:
            sample_roi = [_np.nan, _np.nan, _np.nan, _np.nan]
        elif len(sample_roi) != 4:
            raise ValueError(
                "sample_roi must be a 4 elements array (or None):"
                " {0}.".format(sample_roi)
            )
        self._set_array_data(path, _np.array(sample_roi))

    def set_beam_energy(self, beam_energy):
        """Stores the beam_energy used when converting to q space

        :param float beam_energy:
        """
        path = self._PARAMS_PATH + "/beam_energy"
        self._set_scalar_data(path, float(beam_energy))

    def set_direct_beam(self, direct_beam):
        """Stores the direct beam calibration position.

        :param direct_beam: a 2 elements array.
        """
        path = self._PARAMS_PATH + "/direct_beam"
        if direct_beam is None or len(direct_beam) != 2:
            raise ValueError(
                "direct_beam must be a 2 elements array : " "{0}.".format(direct_beam)
            )
        self._set_array_data(path, _np.array(direct_beam))

    def set_channels_per_degree(self, channels_per_degree):
        """Stores channels per degree calibration.

        :param channels_per_degree: a 2 elements array.
        """
        path = self._PARAMS_PATH + "/channels_per_degree"
        if channels_per_degree is None or len(channels_per_degree) != 2:
            raise ValueError(
                "channels_per_degree must be a 2 elements array : "
                "{0}.".format(channels_per_degree)
            )
        self._set_array_data(path, _np.array(channels_per_degree))

    def set_maxipix_correction(self, enabled):
        """Stores whether maxipix correction was used or not

        :param bool enabled:
        """
        path = self._PARAMS_PATH + "/maxipix_correction"
        self._set_scalar_data(path, int(1 if enabled else 0))
