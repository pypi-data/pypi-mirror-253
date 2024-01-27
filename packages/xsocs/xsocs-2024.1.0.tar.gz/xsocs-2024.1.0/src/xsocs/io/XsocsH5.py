import weakref
from collections import OrderedDict, namedtuple
from contextlib import contextmanager

import h5py as _h5py
import numpy as _np

from .XsocsH5Base import XsocsH5Base
from ._utils import str_to_h5_utf8, find_NX_class

from silx.io.utils import h5py_read_dataset


class InvalidEntryError(Exception):
    pass


ScanPositions = namedtuple(
    "ScanPositions", ["motor_0", "pos_0", "motor_1", "pos_1", "shape"]
)

MOTORCOLS = {"pix": "adcY", "piy": "adcX", "piz": "adcZ"}


def _process_entry(method):
    def _method(inst, entry=None, *args, **kwargs):
        if entry is None:
            entry = inst.get_entry_name()
        elif isinstance(entry, int):
            entry = inst.get_entry_name(entry)
        return method(inst, entry, *args, **kwargs)

    return _method


class XsocsH5(XsocsH5Base):
    TOP_ENTRY = "global"
    positioners_tpl = "/{0}/instrument/positioners"
    img_data_tpl = "/{0}/measurement/image/data"
    measurement_tpl = "/{0}/measurement"
    detector_tpl = "/{0}/instrument/detector"
    scan_params_tpl = "/{0}/scan"

    def __init__(self, h5_f, mode="r"):
        super(XsocsH5, self).__init__(h5_f, mode=mode)

        self.__entries = None

    @_process_entry
    def title(self, entry):
        with self._get_file() as h5_file:
            path = entry + "/title"
            return h5py_read_dataset(h5_file[path], decode_ascii=True)

    @_process_entry
    def entry_filename(self, entry):
        with self._get_file() as h5_file:
            return h5_file[entry].file.filename

    def _update_entries(self):
        with self._get_file() as h5_file:
            self.__entries = sorted(find_NX_class(h5_file, "NXentry"))

    def entries(self):
        if self.__entries is None:
            self._update_entries()
        return self.__entries[:]

    @_process_entry
    def scan_angle(self, entry):
        # TODO : get the correct angle name
        return self.positioner(entry, "eta")

    def get_entry_name(self, entry_idx=0):
        """
        Get the entry found at position *entry_idx* (entries names sorted
        alphabeticaly).
        Raises InvalidEntryError if the entry is not found.
        """
        try:
            return self.entries()[entry_idx]
        except IndexError:
            raise InvalidEntryError(
                "Entry not found (entry_idx={0})." "".format(entry_idx)
            )

    @_process_entry
    def __detector_params(self, entry, param_names):
        with self._get_file() as h5_file:
            path = self.detector_tpl.format(entry) + "/{0}"
            if isinstance(param_names, (list, set, tuple)):
                return [
                    h5_file.get(path.format(param), _np.array(None))[()]
                    for param in param_names
                ]
            return h5_file.get(path.format(param_names), _np.array(None))[()]

    @_process_entry
    def beam_energy(self, entry):
        return self.__detector_params(entry, "beam_energy")

    @_process_entry
    def direct_beam(self, entry):
        return self.__detector_params(entry, ["center_chan_dim0", "center_chan_dim1"])

    @_process_entry
    def chan_per_deg(self, entry):
        return self.__detector_params(entry, ["chan_per_deg_dim0", "chan_per_deg_dim1"])

    @_process_entry
    def image_roi_offset(self, entry):
        """Image ROI offset that was saved in the hdf5 file

        :param str entry: Entry from which to retrieve the information
        :return: ROI offset (row_offset, column)
        :rtype: Union[List[int],None]
        """
        return self.__detector_params(entry, "image_roi_offset")

    @_process_entry
    def n_images(self, entry):
        # TODO : make sure that data.ndims = 3
        path = self.img_data_tpl.format(entry)
        return self._get_array_data(path, shape=True)[0]

    @_process_entry
    def image_size(self, entry):
        # TODO : make sure that data.ndims = 3
        path = self.img_data_tpl.format(entry)
        return self._get_array_data(path, shape=True)[1:3]

    @_process_entry
    def image_dtype(self, entry):
        path = self.img_data_tpl.format(entry)
        return self._get_array_data(path, dtype=True)

    @_process_entry
    def dset_shape(self, path):
        return self._get_array_data(path, shape=True)

    @_process_entry
    def image_cumul(self, entry, dtype=None):
        """Returns the summed intensity for each image.

        :param str entry:
        :param dtype: dtype passed to the numpy.sum function.
            Default is numpy.double.
        :type dtype: numpy.dtype
        """
        if dtype is None:
            dtype = _np.double

        with self.image_dset_ctx(entry) as ctx:
            shape = ctx.shape
            intensity = _np.zeros(shape=(shape[0],), dtype=dtype)
            img_buffer = _np.array(ctx[0], dtype=dtype)
            for idx in range(0, shape[0]):
                ctx.read_direct(img_buffer, idx)
                intensity[idx] = _np.sum(img_buffer)
        return intensity

    @_process_entry
    def scan_positions(self, entry):
        path = self.measurement_tpl.format(entry)
        params = self.scan_params(entry)

        motors = [
            m.decode() if hasattr(m, "decode") else m
            for m in (params["motor_0"], params["motor_1"])
        ]

        m0 = "/{0}".format(MOTORCOLS[motors[0]])
        m1 = "/{0}".format(MOTORCOLS[motors[1]])
        n_0 = params["motor_0_steps"]
        n_1 = params["motor_1_steps"]

        x_pos = self._get_array_data(path + m0)
        y_pos = self._get_array_data(path + m1)
        return ScanPositions(
            motor_0=motors[0],
            pos_0=x_pos,
            motor_1=motors[1],
            pos_1=y_pos,
            shape=(n_0, n_1),
        )

    @_process_entry
    def acquisition_params(self, entry):
        beam_energy = self.beam_energy(entry)
        direct_beam = self.direct_beam(entry)
        chan_per_deg = self.chan_per_deg(entry)

        result = OrderedDict()
        result["beam_energy"] = beam_energy
        result["direct_beam"] = direct_beam
        result["chan_per_deg"] = chan_per_deg

        return result

    @_process_entry
    def is_regular_grid(self, entry):
        """For now grids are always regular

        :param str entry:
        :rtype: bool
        """
        # TODO
        return True

    @_process_entry
    def scan_params(self, entry):
        # TODO : make this more generic to make it compatible
        #  with irregular grids
        param_names = [
            "motor_0",
            "motor_0_start",
            "motor_0_end",
            "motor_0_steps",
            "motor_1",
            "motor_1_start",
            "motor_1_end",
            "motor_1_steps",
            "delay",
        ]
        with self._get_file() as h5_file:
            path = self.scan_params_tpl.format(entry) + "/{0}"
            result = OrderedDict()
            for param in param_names:
                value = h5_file.get(path.format(param), _np.array(None))[()]
                if hasattr(value, "decode"):
                    value = value.decode()
                result[param] = value
            return result

    @_process_entry
    def positioner(self, entry, positioner):
        path = self.positioners_tpl.format(entry) + "/" + positioner
        return self._get_scalar_data(path)

    @_process_entry
    def positioners(self, entry):
        """Returns names of positioners.

        :return: List of dataset names in positioners
        :rtype: List[str]
        """
        positioners = []

        path = self.positioners_tpl.format(entry) + "/"
        with self._get_file() as h5_file:
            for name, node in h5_file[path].items():
                if isinstance(node, _h5py.Dataset) and node.dtype.kind in "iuf":
                    positioners.append(name)

        return positioners

    @_process_entry
    def measurement(self, entry, measurement):
        path = self.measurement_tpl.format(entry) + "/" + measurement
        return self._get_array_data(path)

    @_process_entry
    def normalizers(self, entry):
        """Returns names of dataset in measurement that can be used to normalize data

        It returns names of 1D datasets with same number of elements as images
        that are available in the measurement group.

        :return: List of dataset names in measurement that might be normalizers
        :rtype: List[str]
        """
        normalizers = []

        nb_images = self.n_images(entry)

        path = self.measurement_tpl.format(entry) + "/"
        with self._get_file() as h5_file:
            for name, node in h5_file[path].items():
                if (
                    isinstance(node, _h5py.Dataset)
                    and node.dtype.kind in "iuf"
                    and len(node.shape) == 1
                    and node.shape[0] == nb_images
                ):
                    # Only get (u)int and float datasets
                    # with same number of values as number of images
                    normalizers.append(name)

        return normalizers

    @contextmanager
    @_process_entry
    def image_dset_ctx(self, entry, create=False, **kwargs):
        """
        Context manager for the image dataset.
        WARNING: only to be used as a context manager!
        """
        dset_path = self.img_data_tpl.format(entry)
        with self._get_file() as h5_file:
            if create:
                try:
                    image_dset = h5_file.require_dataset(dset_path, **kwargs)
                except TypeError:
                    image_dset = h5_file.create_dataset(dset_path, **kwargs)
            else:
                image_dset = h5_file[dset_path]
            yield weakref.proxy(image_dset)
            del image_dset


class XsocsH5Writer(XsocsH5):
    def __init__(self, h5_f, mode="a"):
        super(XsocsH5Writer, self).__init__(h5_f, mode=mode)

    def __set_detector_params(self, entry, params):
        with self._get_file():
            path = self.detector_tpl.format(entry) + "/{0}"
            for param_name, param_value in params.items():
                self._set_scalar_data(path.format(param_name), param_value)

    def set_beam_energy(self, beam_energy, entry):
        return self.__set_detector_params(entry, {"beam_energy": beam_energy})

    def set_direct_beam(self, direct_beam, entry):
        value = {"center_chan_dim0": direct_beam[0], "center_chan_dim1": direct_beam[1]}
        return self.__set_detector_params(entry, value)

    def set_chan_per_deg(self, chan_per_deg, entry):
        value = {
            "chan_per_deg_dim0": chan_per_deg[0],
            "chan_per_deg_dim1": chan_per_deg[1],
        }
        return self.__set_detector_params(entry, value)

    def set_image_roi_offset(self, offset, entry):
        """Store image ROI offset information in the hdf5 file

        :param List[int] offset:
            Offset of the ROI in pixels (row_offset, column_offset)
        :param str entry: Entry for which to store information
        """
        return self.__set_detector_params(entry, {"image_roi_offset": offset})

    def set_scan_params(
        self,
        entry,
        motor_0,
        motor_0_start,
        motor_0_end,
        motor_0_steps,
        motor_1,
        motor_1_start,
        motor_1_end,
        motor_1_steps,
        delay,
        **kwargs
    ):
        params = OrderedDict(
            [
                ("motor_0", str_to_h5_utf8(motor_0)),
                ("motor_0_start", float(motor_0_start)),
                ("motor_0_end", float(motor_0_end)),
                ("motor_0_steps", int(motor_0_steps)),
                ("motor_1", str_to_h5_utf8(motor_1)),
                ("motor_1_start", float(motor_1_start)),
                ("motor_1_end", float(motor_1_end)),
                ("motor_1_steps", int(motor_1_steps)),
                ("delay", float(delay)),
            ]
        )
        with self._get_file():
            path = self.scan_params_tpl.format(entry) + "/{0}"
            for param_name, param_value in params.items():
                self._set_scalar_data(path.format(param_name), param_value)

    def create_entry(self, entry):
        with self._get_file() as h5_file:
            entry_grp = h5_file.require_group(entry)
            entry_grp.attrs["NX_class"] = str_to_h5_utf8("NXentry")

            # creating mandatory groups and setting their Nexus attributes
            grp = entry_grp.require_group("measurement/image")
            grp.attrs["interpretation"] = str_to_h5_utf8("image")

            # setting the nexus classes
            # entry_grp.attrs['NX_class'] = str_to_h5_utf8('NXentry')

            grp = entry_grp.require_group("instrument")
            grp.attrs["NX_class"] = str_to_h5_utf8("NXinstrument")

            grp = entry_grp.require_group("instrument/detector")
            grp.attrs["NX_class"] = str_to_h5_utf8("NXdetector")

            grp = entry_grp.require_group("instrument/positioners")
            grp.attrs["NX_class"] = str_to_h5_utf8("NXcollection")

            grp = entry_grp.require_group("measurement")
            grp.attrs["NX_class"] = str_to_h5_utf8("NXcollection")

            grp = entry_grp.require_group("measurement/image")
            grp.attrs["NX_class"] = str_to_h5_utf8("NXcollection")

            # creating some links
            grp = entry_grp.require_group("measurement/image")
            det_grp = entry_grp.require_group("instrument/detector")
            grp["info"] = det_grp
            det_grp["data"] = _h5py.SoftLink(self.img_data_tpl.format(entry))

            self._update_entries()


class XsocsH5MasterWriter(XsocsH5Writer):
    def add_entry_file(self, entry, entry_file, master_entry=None):
        """Add an external link to an entry in a sub-file

        :param str entry: Name of the entry in the sub-file
        :param str entry_file: Name of the file the entry belongs to
        :param str master_entry: Optional alternative entry name in master file
        """
        if master_entry is None:
            master_entry = entry

        with self._get_file() as h5_file:
            h5_file[master_entry] = _h5py.ExternalLink(entry_file, entry)
