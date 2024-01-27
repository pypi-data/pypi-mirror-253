import logging
import functools
import multiprocessing

import numpy
from scipy.optimize import leastsq

from silx.math.fit import snip1d

from ... import config
from ...io import QSpaceH5
from ...io.FitH5 import BackgroundTypes, FitH5, FitH5Writer
from ...util import gaussian, project


_logger = logging.getLogger(__name__)


class FitTypes(object):
    """Kind of fit available"""

    GAUSSIAN = 0
    """1 gaussian fit"""

    CENTROID = 1
    """Center of mass and max"""

    ALLOWED = GAUSSIAN, CENTROID


class FitStatus(object):
    """Enum for the fit status

    Starting at 1 for compatibility reasons.
    """

    UNKNOWN, OK, FAILED = range(0, 3)


class FitResult(object):
    """Object storing fit/com results

    It also allows to save as hdf5 with :meth:`to_fit_h5`.

    :param numpy.ndarray sample_x: N X sample position of the results
    :param numpy.ndarray sample_y: N Y sample position of the results
    :param List[numpy.ndarray] q_dim_values:
        Values along each axis of the QSpace
    :param List[str] q_dim_names:
        Name of axes for each dimension of the QSpace
    :param Union[List[List[int]],None] roi_indices: QSpace ROI to process
    :param FitTypes fit_mode: Kind of fit
    :param BackgroundTypes background_mode: Kind of background subtraction
    :param numpy.ndarray fit_results:
        The fit/com results as a N (points) x 3 (axes) array of struct
        containing the results.

        Warning: This array is used as is and not copied.
    """

    def __init__(
        self,
        sample_x,
        sample_y,
        q_dim_values,
        q_dim_names,
        roi_indices,
        fit_mode,
        background_mode,
        fit_results,
    ):
        super(FitResult, self).__init__()

        self.sample_x = sample_x
        """X position on the sample of each fit result (numpy.ndarray)"""

        self.sample_y = sample_y
        """Y position on the sample of each fit result (numpy.ndarray)"""

        self.qspace_dimension_values = q_dim_values
        """QSpace axis values (List[numpy.ndarray])"""

        self.qspace_dimension_names = q_dim_names
        """QSpace axis names (List[str])"""

        self.roi_indices = roi_indices
        """Roi indices (List[List[int]])"""

        self.fit_mode = fit_mode
        """Fit type (FitTypes)"""

        self.background_mode = background_mode
        """Background type (BackgroundTypes)"""

        # transpose from N (points) x 3 (axes) to 3 (axes) x N (points)
        self._fit_results = numpy.transpose(fit_results)

    @property
    def available_result_names(self, dimension=None):
        """Returns the available result names

        :param Union[int,None] dimension:
        :rtype: List[str]
        """
        if dimension is None:
            dimension = 0
        return self._fit_results[dimension].dtype.names

    def get_results(self, dimension, parameter, copy=True):
        """Returns a given parameter of the result

        :param int dimension: QSpace dimension from which to return result
        :param str parameter: Name of the result to return
        :param bool copy: True to return a copy, False to return internal data
        :return: A 1D array
        :rtype: numpy.ndarray
        """
        return numpy.array(self._fit_results[dimension][parameter], copy=copy)

    _FIT_ENTRY_NAMES = {FitTypes.GAUSSIAN: "Gaussian", FitTypes.CENTROID: "Centroid"}

    _FIT_PROCESS_NAMES = {FitTypes.GAUSSIAN: "gauss_0", FitTypes.CENTROID: "centroid"}

    def to_fit_h5(self, fit_h5, mode="a"):
        """Write fit results to an HDF5 file

        :param str fit_h5: Filename where to save fit results
        :param Union[None,str] mode: HDF5 file opening mode
        """
        fit_name = self._FIT_ENTRY_NAMES[self.fit_mode]
        result_name = self._FIT_PROCESS_NAMES[self.fit_mode]

        with FitH5Writer(
            fit_h5,
            entry=fit_name,
            axis_names=self.qspace_dimension_names,
            background_mode=self.background_mode,
            mode=mode,
        ) as fitH5:
            fitH5.create_process(result_name)
            fitH5.set_sample_positions(self.sample_x, self.sample_y)
            fitH5.set_qspace_dimension_values(*self.qspace_dimension_values)
            if self.roi_indices is not None:
                fitH5.set_roi_indices(*self.roi_indices)

            for dimension, array in enumerate(self._fit_results):
                for name in self.available_result_names:
                    results = self.get_results(dimension, name, copy=False)
                    if name == "Status":
                        fitH5.set_status(dimension, results)
                    else:
                        fitH5.set_result(result_name, dimension, name, results)

    @classmethod
    def from_fit_h5(cls, filename):
        """Create a FitResult from content of a HDF5 fit file

        :param str filename: HDF% fit results file name
        :rtype: FitResult
        """
        with FitH5(filename) as fith5:
            # Retrieve entry
            entries = fith5.entries()
            if len(entries) != 1:
                raise RuntimeError("Only one entry in fit result is supported")
            entry = fith5.entries()[0]

            # Get fit mode corresponding to entry name
            for key, value in cls._FIT_ENTRY_NAMES.items():
                if value == entry:
                    fit_mode = key
                    break
            else:
                raise RuntimeError("Unsupported fit entry name: %s" % entry)

            # Get corresponding NXProcess name
            process = cls._FIT_PROCESS_NAMES[fit_mode]
            if process not in fith5.processes(entry):
                raise RuntimeError("Cannot find relevant NXProcess group in file")

            # Retrieve fit results
            parameters = list(fith5.get_result_names(entry, process))
            parameters.append("Status")

            fit_results = []
            for axis in range(len(fith5.get_qspace_dimension_names(entry))):
                result = [
                    fith5.get_axis_result(entry, process, param, axis)
                    for param in parameters[:-1]
                ]  # All but Status
                result.append(fith5.get_status(entry, axis))
                fit_results.append(result)

            # Get dtype from result arrays
            result_dtype = [
                (name, array.dtype) for name, array in zip(parameters, fit_results[0])
            ]

            # Convert from list by axis of list by param of list by sample point
            # To list by sample point of list by axis of list by param
            nb_axes = len(fit_results)
            nb_params = len(fit_results[0])
            nb_points = len(fit_results[0][0])

            fit_results = [
                [
                    tuple(
                        [fit_results[axis][param][point] for param in range(nb_params)]
                    )
                    for axis in range(nb_axes)
                ]
                for point in range(nb_points)
            ]

            # Convert to record array
            fit_results = numpy.array(fit_results, dtype=result_dtype)

            # Return FitResult object
            sample_x, sample_y = fith5.sample_positions(entry)
            return FitResult(
                sample_x=sample_x,
                sample_y=sample_y,
                q_dim_values=fith5.get_qspace_dimension_values(entry),
                q_dim_names=fith5.get_qspace_dimension_names(entry),
                roi_indices=fith5.get_roi_indices(entry),
                fit_mode=fit_mode,
                background_mode=fith5.get_background_mode(entry),
                fit_results=fit_results,
            )

    def __eq__(self, other):
        """Implement equality, useful for tests"""
        return self.almost_equal(other, rtol=0.0, atol=0.0)

    def almost_equal(self, other, rtol=1e-5, atol=1e-8):
        """Implement almost equal comparison, useful for tests

        :param FitResult other: The other FitResult to compare to
        :param float rtol: The relative tolerance.
            See :func:`numpy.allclose` for details.
        :param float atol: The absolute tolerance.
            See :func:`numpy.allclose` for details.
        """
        return (
            isinstance(other, FitResult)
            and numpy.array_equal(self.sample_x, other.sample_x)
            and numpy.array_equal(self.sample_y, other.sample_y)
            and numpy.all(
                [
                    numpy.array_equal(a1, a2)
                    for a1, a2 in zip(
                        self.qspace_dimension_values, other.qspace_dimension_values
                    )
                ]
            )
            and (
                tuple(self.qspace_dimension_names)
                == tuple(other.qspace_dimension_names)
            )
            and numpy.array_equal(self.roi_indices, other.roi_indices)
            and self.fit_mode == other.fit_mode
            and self.background_mode == other.background_mode
            and (set(self.available_result_names) == set(other.available_result_names))
            and numpy.all(
                [
                    numpy.allclose(ary1[param], ary2[param], rtol=rtol, atol=atol)
                    for param in self.available_result_names
                    for ary1, ary2 in zip(self._fit_results, other._fit_results)
                ]
            )
        )


class PeakFitter(object):
    """Class performing fit/com processing

    :param str qspace_f: path to the HDF5 file containing the qspace cubes
    :param FitTypes fit_type:
    :param Union[numpy.ndarray,None] indices:
        indices of the cubes (in the input HDF5 dataset) for which
        the dim0/dim1/dim2 peaks coordinates will be computed. E.g : if the array
        [1, 2, 3] is provided, only those cubes will be fitted.
    :param Union[int,None] n_proc:
        Number of process to use. If None, the config value is used.
    :param Union[List[List[int]],None] roi_indices: QSpace ROI to process
    :param BackgroundTypes background: The background subtraction to perform
    """

    # Different status values
    READY, RUNNING, DONE, ERROR, CANCELED = __STATUSES = range(5)

    def __init__(
        self,
        qspace_f,
        fit_type=FitTypes.GAUSSIAN,
        indices=None,
        n_proc=None,
        roi_indices=None,
        background=BackgroundTypes.NONE,
    ):
        super(PeakFitter, self).__init__()

        self.__results = None
        self.__status = self.READY

        self.__qspace_f = qspace_f
        self.__fit_type = fit_type
        self.__background = background

        self.__n_proc = n_proc if n_proc else config.DEFAULT_PROCESS_NUMBER

        if roi_indices is not None:
            self.__roi_indices = numpy.array(roi_indices[:])
        else:
            self.__roi_indices = None

        if fit_type not in FitTypes.ALLOWED:
            self.__set_status(self.ERROR)
            raise ValueError("Unknown fit type: {0}".format(fit_type))

        if background not in BackgroundTypes.ALLOWED:
            self.__set_status(self.ERROR)
            raise ValueError("Unknown background type: {}".format(background))

        try:
            with QSpaceH5.QSpaceH5(qspace_f) as qspace_h5:
                with qspace_h5.qspace_dset_ctx() as dset:
                    qdata_shape = dset.shape
        except IOError:
            self.__set_status(self.ERROR)
            raise

        if indices is None:
            n_points = qdata_shape[0]
            self.__indices = numpy.arange(n_points)
        else:
            self.__indices = numpy.array(indices, copy=True)

    def __set_status(self, status):
        """Set the status of the processing

        :param int status:
        """
        assert status in self.__STATUSES
        self.__status = status

    status = property(
        lambda self: self.__status, doc="Status of the fit/COM process (int)"
    )

    results = property(
        lambda self: self.__results, doc="The result of the fit/COM (FitResult or None)"
    )

    def peak_fit(self):
        """Blocking execution of fit/com processing.

        It returns the fit/com result

        :rtype: FitResult
        """
        for _ in self.__peak_fit():
            pass
        return self.results

    def peak_fit_iterator(self):
        """Run fit/com processing as a generator.

        It yields a progress indicator in [0, 1].
        """
        for progress, _ in enumerate(self.__peak_fit()):
            yield progress / len(self.__indices)

    def __peak_fit(self):
        """Run the fit/COM processing and set result and status"""
        self.__results = None
        self.__set_status(self.RUNNING)

        pool = multiprocessing.Pool(self.__n_proc)

        fit_results = []
        for result in pool.imap(
            functools.partial(
                _fit_process,
                qspace_f=self.__qspace_f,
                fit_type=self.__fit_type,
                background_type=self.__background,
                roi_indices=self.__roi_indices,
            ),
            self.__indices,
        ):
            fit_results.append(result)
            yield result
        pool.close()
        pool.join()

        # Prepare FitResult object
        with QSpaceH5.QSpaceH5(self.__qspace_f) as qspace_h5:
            x_pos = qspace_h5.sample_x[self.__indices]
            y_pos = qspace_h5.sample_y[self.__indices]
            q_dim0, q_dim1, q_dim2 = qspace_h5.qspace_dimension_values
            q_dim_names = qspace_h5.qspace_dimension_names

        if self.__roi_indices is not None:
            q_dim0 = q_dim0[self.__roi_indices[0][0] : self.__roi_indices[0][1]]
            q_dim1 = q_dim1[self.__roi_indices[1][0] : self.__roi_indices[1][1]]
            q_dim2 = q_dim2[self.__roi_indices[2][0] : self.__roi_indices[2][1]]

        if self.__fit_type == FitTypes.GAUSSIAN:
            result_dtype = [
                ("Area", numpy.float64),
                ("Center", numpy.float64),
                ("Sigma", numpy.float64),
                ("Status", numpy.bool_),
            ]

        elif self.__fit_type == FitTypes.CENTROID:
            result_dtype = [
                ("COM", numpy.float64),
                ("I_sum", numpy.float64),
                ("I_max", numpy.float64),
                ("Pos_max", numpy.float64),
                ("Status", numpy.bool_),
            ]

        else:
            raise RuntimeError("Unknown Fit Type")

        self.__results = FitResult(
            sample_x=x_pos,
            sample_y=y_pos,
            q_dim_values=(q_dim0, q_dim1, q_dim2),
            q_dim_names=q_dim_names,
            roi_indices=self.__roi_indices,
            fit_mode=self.__fit_type,
            background_mode=self.__background,
            fit_results=numpy.array(fit_results, dtype=result_dtype),
        )

        self.__set_status(self.DONE)


# Fit/COM function run through multiprocessing

# Per process cache for fit process
_per_process_cache = None


def _fit_process(
    index,
    qspace_f,
    fit_type=FitTypes.GAUSSIAN,
    background_type=BackgroundTypes.NONE,
    roi_indices=None,
):
    """Run fit processing.

    It loads a QSpace, extracts a ROI from it, project to axes,
    and then for each axis, it subtracts a background and performs a fit/COM.

    This function is run through a multiprocessing.Pool

    :param int index: The index of the QSpace to process
    :param str qspace_f: Filename of the hdf5 file containing QSpace
    :param FitTypes fit_type: The kind of fit to perform
    :param BackgroundTypes background_type:
        The kind of background subtraction to perform
    :param Union[List[List[int]],None] roi_indices:
        Optional QSpace ROI start:end in the 3 dimensions
    :return: Fit results as a list of results for dim0, dim1 and dim2
    :rtype: List[List[Union[float,bool]]]
    """
    global _per_process_cache
    if _per_process_cache is None:  # Initialize per process cache
        qspace_h5 = QSpaceH5.QSpaceH5(qspace_f)
        _per_process_cache = (
            qspace_h5,
            qspace_h5.qspace_dimension_values,
            qspace_h5.histo,
        )

    # Retrieve data/file from cache
    qspace_h5, axes, hits = _per_process_cache

    # Load qspace
    if roi_indices is not None:
        qslice = numpy.s_[
            roi_indices[0][0] : roi_indices[0][1],
            roi_indices[1][0] : roi_indices[1][1],
            roi_indices[2][0] : roi_indices[2][1],
        ]

        axes = [axis[roi] for axis, roi in zip(axes, qslice)]
        qspace = qspace_h5.qspace_slice((index,) + qslice)
        hits = hits[qslice]

    else:
        qspace = qspace_h5.qspace_slice(index)

    # Normalize with hits and project to axes
    projections = project(qspace, hits)

    # Background subtraction
    if background_type != BackgroundTypes.NONE:
        for array in projections:
            array -= background_estimation(background_type, array)

    # Select Fit/COM function
    if fit_type == FitTypes.CENTROID:
        fit_func = centroid
    elif fit_type == FitTypes.GAUSSIAN:
        fit_func = gaussian_fit
    else:
        raise RuntimeError("Unsupported fit type: %s" % fit_type)

    # Fit/COM for projections on each axes
    return [fit_func(axis, signal) for axis, signal in zip(axes, projections)]


# Center of mass


def centroid(axis, signal):
    """Returns Center of mass and maximum information

    :param numpy.ndarray axis: 1D x data
    :param numpy.ndarray signal: 1D y data
    :return: Center of mass, sum of signal, max of signal, position of max and status
        ('COM', 'I_sum', 'I_max', 'Pos_max', 'status')
    :rtype: List[Union[float,bool]]
    """
    signal_sum = signal.sum()
    if signal_sum == 0:
        return float("nan"), float("nan"), float("nan"), float("nan"), False

    else:
        max_idx = signal.argmax()
        return (
            float(numpy.dot(axis, signal) / signal_sum),
            float(signal_sum),
            float(signal[max_idx]),
            float(axis[max_idx]),
            True,
        )


# Gaussian fit


def _gaussian_err(parameters, axis, signal):
    """Returns difference between signal and given gaussian

    :param List[float] parameters: area, center, sigma
    :param numpy.ndarray axis: 1D x data
    :param numpy.ndarray signal: 1D y data
    :return:
    """
    area, center, sigma = parameters
    return gaussian(axis, area, center, sigma) - signal


_SQRT_2_PI = numpy.sqrt(2 * numpy.pi)


def gaussian_fit(axis, signal):
    """Returns gaussian fitting information

    parameters: (a, c, s)
    and f(x) = (a / (sqrt(2 * pi) * s)) * exp(- 0.5 * ((x - c) / s)^2)

    :param axis: 1D x data
    :param signal: 1D y data
    :return: Area, center, sigma, status
        ('Area', 'Center', 'Sigma', 'status)
    :rtype: List[Union[float,bool]]
    """
    # compute guess
    area = signal.sum() * (axis[-1] - axis[0]) / len(axis)
    center = axis[signal.argmax()]
    sigma = area / (signal.max() * _SQRT_2_PI)

    # Fit a gaussian
    result = leastsq(
        _gaussian_err,
        x0=(area, center, sigma),
        args=(axis, signal),
        maxfev=100000,
        full_output=True,
    )

    if result[4] not in [1, 2, 3, 4]:
        return float("nan"), float("nan"), float("nan"), False

    else:
        area, center, sigma = result[0]
        return float(area), float(center), float(sigma), True


# background


def background_estimation(mode, data):
    """Estimates a background of mode kind for data

    :param BackgroundTypes mode: The kind of background to compute
    :param numpy.ndarray data: The data array to process
    :return: The estimated background as an array with same shape as input
    :rtype: numpy.ndarray
    :raises ValueError: In case mode is not known
    """
    # Background subtraction
    if mode == BackgroundTypes.CONSTANT:
        # Shift data so that smallest value is 0
        return numpy.ones_like(data) * numpy.nanmin(data)

    elif mode == BackgroundTypes.SNIP:
        # Using snip background
        return snip1d(data, snip_width=len(data))

    elif mode == BackgroundTypes.NONE:
        return numpy.zeros_like(data)

    else:
        raise ValueError("Unsupported background mode")
