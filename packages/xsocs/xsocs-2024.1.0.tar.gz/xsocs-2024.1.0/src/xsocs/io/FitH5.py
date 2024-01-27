"""Class handle read/write of fit/COM results in HDF5 files"""

import numpy

from .XsocsH5Base import XsocsH5Base
from .QSpaceH5 import QSpaceCoordinates
from ._utils import str_to_h5_utf8, find_NX_class


class BackgroundTypes(object):
    """Enum of background subtraction types:

    - NONE: No background
    - CONSTANT: Remove constant (= min of the data) background
    - SNIP: Statistics-sensitive Non-linear Iterative Peak-clipping algorithm
    """

    NONE = "None"
    CONSTANT = "Constant"
    SNIP = "Snip"
    ALLOWED = NONE, CONSTANT, SNIP


class FitH5(XsocsH5Base):
    """File containing fit results.

    Requirements :
    - the number of sample position is defined at entry level : all processes
    within the same entry are applied to the same sample points.
    - all results arrays within an entry (even if they don't belong to the same
    process) have the same size (equal to the number of sample points defined
    for that entry)
    - all arrays are 1D.
    """

    _QSPACE_AXIS_PATH = "{entry}/qspace_axis"
    _QSPACE_ROI_PATH = "{entry}/qspace_rois"
    _STATUS_PATH = "{entry}/status/{axis}"
    _RESULT_GRP_PATH = "{entry}/{process}/results"
    _RESULT_PATH = "{entry}/{process}/results/{result}/{axis}"
    _SCAN_X_PATH = "{entry}/sample/x_pos"
    _SCAN_Y_PATH = "{entry}/sample/y_pos"
    _BACKGROUND_MODE_PATH = "{entry}/background_mode"
    _AXIS_NAMES_PATH = "{entry}/axes"

    def entries(self):
        """Return the entry names.

        :rtype: List[str]
        """
        with self._get_file() as h5_file:
            return sorted(find_NX_class(h5_file, "NXentry"))

    def processes(self, entry):
        """Return the processes names for the given entry.

        :param str entry:
        :rtype: List[str]
        """
        with self._get_file() as h5_file:
            return sorted(find_NX_class(h5_file[entry], "NXprocess"))

    def get_result_names(self, entry, process):
        """Returns the result names for the given process.

        Names are ordered alphabetically.

        :param str entry:
        :param str process:
        :rtype: List[str]
        """
        results_path = self._RESULT_GRP_PATH.format(entry=entry, process=process)
        with self._get_file() as h5_file:
            return sorted(h5_file[results_path].keys())

    def get_status(self, entry, axis):
        """Returns the fit status for the given entry/process/axis

        :param str entry:
        :param int axis:
        :rtype: numpy.ndarray
        """
        axis_name = self.get_qspace_dimension_names(entry)[axis]
        status_path = self._STATUS_PATH.format(entry=entry, axis=axis_name)
        status = self._get_array_data(status_path)

        # 30 Jan 2017.
        # This is kept for compatibility with previous versions
        # TODO : remove this sometime...
        if status is None:
            # only one process was supported at the time
            processes = self.processes(entry)
            if len(processes) == 0:
                return None
            process = processes[0]
            status_path = "{entry}/{process}/status/{axis}"
            status = self._get_array_data(
                status_path.format(entry=entry, process=process, axis=axis_name)
            )
        return status

    def sample_positions(self, entry):
        """Return the sample points coordinates (x, y) for the given entry.

        :param str entry:
        :return: 2 arrays: x and y
        :rtype: List[numpy.ndarray]
        """
        return (
            self._get_array_data(self._SCAN_X_PATH.format(entry=entry)),
            self._get_array_data(self._SCAN_Y_PATH.format(entry=entry)),
        )

    def get_qspace_dimension_values(self, entry):
        """Returns the axis values.

        :param str entry:
        :rtype: List[numpy.ndarray]
        """
        base_path = self._QSPACE_AXIS_PATH.format(entry=entry)
        return [
            self._get_array_data("/".join((base_path, name)))
            for name in self.get_qspace_dimension_names(entry)
        ]

    def get_roi_indices(self, entry):
        """Returns the axis rois.

        :param str entry:
        :rtype: List[numpy.ndarray]
        """
        base_path = self._QSPACE_ROI_PATH.format(entry=entry)
        if not self._path_exists(base_path):
            return None
        return [
            self._get_array_data("/".join((base_path, name)))
            for name in self.get_qspace_dimension_names(entry)
        ]

    def get_axis_result(self, entry, process, result, axis):
        """Returns the results for the given entry/process/result name/axis.

        :param str entry:
        :param str process:
        :param str result:
        :param int axis:
        :rtype: numpy.ndarray
        """
        axis_name = self.get_qspace_dimension_names(entry)[axis]
        result_path = self._RESULT_PATH.format(
            entry=entry, process=process, result=result, axis=axis_name
        )
        return self._get_array_data(result_path)

    def get_background_mode(self, entry):
        """Returns the background subtraction mode used

        :param str entry: HDF5 entry name for which to retrieve information
        :rtype: str
        """
        mode = self._get_array_data(self._BACKGROUND_MODE_PATH.format(entry=entry))
        return mode if mode is not None else BackgroundTypes.NONE

    def get_qspace_dimension_names(self, entry):
        """Returns names of QSpace axes

        :param str entry: HDF5 entry name for which to retrieve information
        :rtype: List[str]
        """
        axes = self._get_array_data(self._AXIS_NAMES_PATH.format(entry=entry))
        if axes is None:  # backward compatibility
            return QSpaceCoordinates.axes_names(QSpaceCoordinates.CARTESIAN)
        else:
            return axes

    def export_csv(self, entry, filename):
        """Exports an entry results as csv.

        :param str entry:
        :param str filename:
        """
        x, y = self.sample_positions(entry)

        processes = self.processes(entry)

        if len(processes) == 0:
            raise ValueError("No process found for entry {0}.".format(entry))

        # with open(filename, 'w+') as res_f:
        with self:
            header_process = ["_", "process:"]
            header_list = ["X", "Y"]
            for process in processes:
                result_names = self.get_result_names(entry, process)
                for axis in self.get_qspace_dimension_names(entry):
                    for result_name in result_names:
                        header_process.append(process)
                        header_list.append(result_name + "_" + axis)
                    header_process.append(process)
                    header_list.append("status_" + axis)

            header = "; ".join(header_process) + "\n" + "; ".join(header_list)

            results = numpy.zeros((len(x), len(header_list)))

            results[:, 0] = x
            results[:, 1] = y

            col_idx = 2
            for process in processes:
                result_names = self.get_result_names(entry, process)
                for axis in range(len(self.get_qspace_dimension_names(entry))):
                    for result_name in result_names:
                        results[:, col_idx] = self.get_axis_result(
                            entry, process, result_name, axis
                        )
                        col_idx += 1
                    results[:, col_idx] = self.get_status(entry, axis)
                    col_idx += 1

            numpy.savetxt(
                filename,
                results,
                fmt="%.10g",
                header=header,
                comments="",
                delimiter="; ",
            )


class FitH5Writer(FitH5):
    """Class to write fit/COM results in a HDF5 file

    :param str h5_f: Filename where to write
    :param str entry:
    :param List[str] axis_names: Names of QSpace axes
    :param BackgroundTypes background_mode: Used background subtraction
    :param str mode: File opening mode
    """

    def __init__(
        self, h5_f, entry, axis_names, background_mode=BackgroundTypes.NONE, mode="w"
    ):
        assert background_mode in BackgroundTypes.ALLOWED

        super(FitH5Writer, self).__init__(h5_f, mode)

        self.__entry = entry
        self.__create_entry(self.__entry)
        self._create_dataset(
            self._AXIS_NAMES_PATH.format(entry=entry),
            data=str_to_h5_utf8([name for name in axis_names]),
        )
        self._create_dataset(
            self._BACKGROUND_MODE_PATH.format(entry=entry), data=str(background_mode)
        )

    def __axis_name(self, dimension):
        """Helper returning the names of the QSpace axis

        :param int dimension: Dimension index of the axis
        :rtype: str
        """
        return self.get_qspace_dimension_names(self.__entry)[dimension]

    def __create_entry(self, entry):
        """Create group to store result for entry

        :param str entry:
        """
        with self._get_file() as h5_file:
            entries = self.entries()
            if len(entries) > 0:
                raise ValueError(
                    "FitH5 doesnt support multiple entries "
                    "yet. ({0}, {1})"
                    "".format(self.filename, entries)
                )
            # TODO : check if it already exists
            entry_grp = h5_file.require_group(entry)
            entry_grp.attrs["NX_class"] = str_to_h5_utf8("NXentry")

    def create_process(self, process):
        """Create group to store a process in entry

        :param str process:
        """
        # TODO : check that there isn't already an existing process
        with self._get_file() as h5_file:
            if process in self.processes(self.__entry):
                raise ValueError("Process <{0}> already exists." "".format(process))

            entry_grp = h5_file[self.__entry]

            # TODO : check if it exists
            process_grp = entry_grp.require_group(process)
            process_grp.attrs["NX_class"] = str_to_h5_utf8("NXprocess")
            results_grp = process_grp.require_group("results")
            results_grp.attrs["NX_class"] = str_to_h5_utf8("NXcollection")

    def set_sample_positions(self, x, y):
        """Write sample positions (x, y) in file

        :param numpy.ndarray x:
        :param numpy.ndarray y:
        """
        self._set_array_data(self._SCAN_X_PATH.format(entry=self.__entry), x)
        self._set_array_data(self._SCAN_Y_PATH.format(entry=self.__entry), y)

    def set_status(self, dimension, data):
        """Write fit/COM status in the file

        :param int dimension:
        :param numpy.ndarray data:
        """
        status_path = self._STATUS_PATH.format(
            entry=self.__entry, axis=self.__axis_name(dimension)
        )
        self._set_array_data(status_path, data)

    def set_result(self, process, dimension, name, data):
        """Write a fit/COM result parameter to the HDF5 file

        :param str process:
        :param int dimension:
        :param str name:
        :param numpy.ndarray data:
        """
        result_path = self._RESULT_PATH.format(
            entry=self.__entry,
            process=process,
            result=name,
            axis=self.__axis_name(dimension),
        )
        self._set_array_data(result_path, data)

    def set_qspace_dimension_values(self, dim0, dim1, dim2):
        """Write qspace axes coordinates for each dimension

        :param numpy.ndarray dim0:
        :param numpy.ndarray dim1:
        :param numpy.ndarray dim2:
        """
        base_path = self._QSPACE_AXIS_PATH.format(entry=self.__entry)
        for index, values in enumerate((dim0, dim1, dim2)):
            self._set_array_data("/".join((base_path, self.__axis_name(index))), values)

    def set_roi_indices(self, roi0, roi1, roi2):
        """Write qspace axes coordinates for each dimension

        :param tuple roi0:
        :param tuple roi1:
        :param tuple roi2:
        """
        base_path = self._QSPACE_ROI_PATH.format(entry=self.__entry)
        for index, values in enumerate((roi0, roi1, roi2)):
            values = numpy.array(values)
            self._set_array_data("/".join((base_path, self.__axis_name(index))), values)
