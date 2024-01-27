import logging
import numbers
import os
import time
import ctypes
from threading import Thread
import multiprocessing as mp
import multiprocessing.sharedctypes as mp_sharedctypes

import numpy as np
import xrayutilities as xu

from ... import config
from ...util import bin_centers_to_range_step
import silx
from silx.math.medianfilter import medfilt2d
from silx.math.chistogramnd_lut import histogramnd_get_lut, histogramnd_from_lut
from ...io import XsocsH5, QSpaceH5, ShiftH5
from ...io.QSpaceH5 import QSpaceCoordinates


_logger = logging.getLogger(__name__)


disp_times = False


def qspace_conversion(
    img_size,
    center_chan,
    chan_per_deg,
    beam_energy,
    phi,
    eta,
    nu,
    delta,
    coordinates=QSpaceCoordinates.CARTESIAN,
):
    """Returns array of Q vectors corresponding to each pixel

    This function is based on xrayutilities

    :param List[int] img_size:
        Size of the detector images in pixels (dim0, dim1)
    :param List[float] center_chan:
       Calibration center channel in image coordinates (dim0, dim1)
    :param List[float] chan_per_deg:
       Channel per degree calibration in image coordinates (dim0, dim1)
    :param Union[float,numpy.ndarray] beam_energy:
        Energy in eV. Either a float or a 1D array with energy for each image
    :param numpy.ndarray phi: 1D array of phi angle for each image
    :param numpy.ndarray eta: 1D array of eta angle for each image
    :param numpy.ndarray nu: 1D array of nu angle for each image
    :param numpy.ndarray delta: 1D array of delta angle for each image
    :param QSpaceCoordinates coordinates:
        Set the coordinate system of the returned array
    :return: Array Q vectors of shape:
        (nb images, image height, image width, coordinates).
        Coordinates are either (qx, qy, qz) or (pitch, roll, radial)
        depending on coordinates argument.
    :rtype: numpy.ndarray
    """
    phi = np.array(phi, copy=False, dtype=np.float64)
    eta = np.array(eta, copy=False, dtype=np.float64)
    nu = np.array(nu, copy=False, dtype=np.float64)
    delta = np.array(delta, copy=False, dtype=np.float64)

    n_images = len(eta)

    if isinstance(beam_energy, numbers.Real):  # Convert to array
        beam_energy = [beam_energy] * n_images
    beam_energy = np.array(beam_energy, copy=False, dtype=np.float64)

    qconv = xu.experiment.QConversion(["y-", "z-"], ["z-", "y-"], [1, 0, 0])

    # convention for coordinate system:
    # x downstream
    # z upwards
    # y to the "outside"
    # (righthanded)
    hxrd = xu.HXRD([1, 0, 0], [0, 0, 1], qconv=qconv)

    hxrd.Ang2Q.init_area(
        "z-",
        "y+",
        cch1=center_chan[0],
        cch2=center_chan[1],
        Nch1=img_size[0],
        Nch2=img_size[1],
        chpdeg1=chan_per_deg[0],
        chpdeg2=chan_per_deg[1],
    )

    # shape of the array that will store the q vectors for all
    # rocking angles
    q_shape = n_images, img_size[0], img_size[1], 3

    # then the array
    q_ar = np.zeros(q_shape, dtype=np.float64)

    for index in range(n_images):
        qx, qy, qz = hxrd.Ang2Q.area(
            eta[index], phi[index], nu[index], delta[index], en=beam_energy[index]
        )

        if coordinates == QSpaceCoordinates.CARTESIAN:
            q_ar[index, :, :, 0] = qx
            q_ar[index, :, :, 1] = qy
            q_ar[index, :, :, 2] = qz

        elif coordinates == QSpaceCoordinates.SPHERICAL:
            # Radius
            radius = np.sqrt(qx**2 + qy**2 + qz**2)
            q_ar[index, :, :, 2] = radius
            # Roll (Phi)
            q_ar[index, :, :, 1] = 90 - np.degrees(np.arctan2(qz, qy))
            # Pitch (Theta)
            q_ar[index, :, :, 0] = 90 - np.degrees(np.arccos(qx / radius))

        else:
            raise ValueError("Unsupported coordinate system")

    return q_ar


class QSpaceConverter(object):
    (READY, RUNNING, DONE, ERROR, CANCELED, UNKNOWN) = __STATUSES = range(6)
    """Available status codes"""

    status = property(lambda self: self.__status)
    """Current status code of this instance"""

    status_msg = property(lambda self: self.__status_msg)
    """Status message if any, or None"""

    results = property(lambda self: self.__results)
    """Parse results. KmapParseResults instance."""

    xsocsH5_f = property(lambda self: self.__xsocsH5_f)
    """Input file name."""

    output_f = property(lambda self: self.__output_f)
    """Output file name."""

    qspace_dims = property(lambda self: self.__params["qspace_dims"])
    """Dimensions of the Q Space (i.e : number of bins)."""

    medfilt_dims = property(lambda self: self.__params["medfilt_dims"])
    """Median filter applied to the images after masking and
    before conversion."""

    beam_energy = property(lambda self: self.__params["beam_energy"])
    """Beam energy or None to read it from entries"""

    direct_beam = property(lambda self: self.__params["direct_beam"])
    """Direct beam calibration position or None to read it from entries"""

    channels_per_degree = property(lambda self: self.__params["channels_per_degree"])
    """Channels per degree calibration or None to read it from entries"""

    sample_indices = property(lambda self: self.__params["sample_indices"])
    """Indices of sample positions that will be converted."""

    n_proc = property(lambda self: self.__n_proc)
    """Number of processes to use.

    Uses the default config value if set to None.
    """

    roi = property(lambda self: self.__params["roi"])
    """Selected ROI in sample coordinates : [xmin, xmax, ymin, ymax]"""

    normalizer = property(lambda self: self.__params["normalizer"])
    """Selected normalizer name in measurement group (str) or None"""

    mask = property(lambda self: self.__params["mask"])
    """Mask to apply on images (2D numpy.ndarray) or None.

    A non-zero value means that the pixel is masked.
    """

    coordinates = property(lambda self: self.__coordinates)
    """The coordinate system to use for the Q vectors (QSpaceCoordinates).

    Default: CARTESIAN.
    """

    def __init__(
        self,
        xsocsH5_f,
        qspace_dims=None,
        medfilt_dims=None,
        output_f=None,
        roi=None,
        entries=None,
        callback=None,
        shiftH5_f=None,
    ):
        """Merger for the Kmap SPEC and EDF files.

        This loads a spech5 file, converts it to HDF5 and
        then tries to match scans and edf image files.

        :param xsocsH5_f: path to the input XsocsH5 file.
        :param qspace_dims: dimensions of the qspace volume
        :param medfilt_dims: dimensions of the median filter kernel
            to apply to the images before conversion. The filter is not
            applied if this keyword is set to None (this is the default).
            The median filter is applied after the mask (if any).
        :param output_f: path to the output file that will be created.
        :param roi: Roi in sample coordinates (xMin, xMax, yMin, yMax)
        :param entries: a list of entry names to convert to qspace. If None,
            all entries found in the xsocsH5File will be used.
        :param callback: callback to call when the parsing is done.
        :param shiftH5_f: a ShiftH5 file name to use if applying shift.
        """
        super(QSpaceConverter, self).__init__()

        self.__status = None

        self.__set_status(self.UNKNOWN, "Init")

        self.__xsocsH5_f = xsocsH5_f
        self.__output_f = output_f

        if shiftH5_f:
            shiftH5 = ShiftH5.ShiftH5(shiftH5_f)
        else:
            shiftH5 = None

        self.__shiftH5 = shiftH5

        xsocsH5 = XsocsH5.XsocsH5(xsocsH5_f)
        # checking entries
        if entries is None:
            entries = xsocsH5.entries()
        else:
            diff = set(entries) - set(xsocsH5.entries())
            if len(diff) > 0:
                raise ValueError(
                    "The following entries were not found in "
                    "the input file :\n - {0}"
                    "".format("\n -".join(diff))
                )

        self.__params = {
            "qspace_dims": None,
            "mask": None,
            "normalizer": None,
            "sample_indices": None,
            "roi": None,
            "entries": sorted(entries),
            "beam_energy": None,
            "direct_beam": None,
            "channels_per_degree": None,
        }

        self.__coordinates = QSpaceCoordinates.CARTESIAN

        self.maxipix_correction = False
        """Whether or not to apply Maxipix module edges correction (bool)"""

        self.__callback = callback
        self.__n_proc = config.DEFAULT_PROCESS_NUMBER
        self.__overwrite = False

        self.__shared_progress = None
        self.__results = None
        self.__term_evt = None

        self.__thread = None

        self.medfilt_dims = medfilt_dims
        self.qspace_dims = qspace_dims
        self.roi = roi

        self.__set_status(self.READY)

    def __get_scans(self):
        """Returns the entries that will be converted."""
        return self.__params["entries"]

    scans = property(__get_scans)
    """Returns the scans found in the input file."""

    def __set_status(self, status, msg=None):
        """Sets the status of this instance.

        :param status:
        :param msg:
        """
        assert status in self.__STATUSES
        self.__status = status
        self.__status_msg = msg

    def convert(
        self, overwrite=False, blocking=True, callback=None, check_consistency=True
    ):
        """Starts the conversion.

        :param overwrite: if False raises an exception if some files already
            exist.
        :param blocking: if False, the merge will be done in a separate
            thread and this method will return immediately.
        :param callback: callback that will be called when the merging is done.
            It overwrites the one passed the constructor.
        :param check_consistency: set to False to ignore any incensitencies
            in the input entries (e.g : different counters, ...).
        """
        if self.is_running():
            raise RuntimeError("This QSpaceConverter instance is already " "parsing.")

        self.__set_status(self.RUNNING)

        errors = self.check_parameters()

        if len(errors) > 0:
            msg = "Invalid parameters.\n{0}".format("\n".join(errors))
            raise ValueError(msg)

        errors = self.check_consistency(
            beam_energy_check=self.beam_energy is None,
            direct_beam_check=self.direct_beam is None,
            channels_per_degree_check=self.channels_per_degree is None,
        )

        if len(errors) > 0:
            msg = "Inconsistent input data.\n{0}".format("\n".join(errors))

            if check_consistency:
                raise ValueError(msg)
            else:
                _logger.warning(msg)

        output_f = self.__output_f
        if output_f is None:
            self.__set_status(self.ERROR)
            raise ValueError("Output file name (output_f) has not been set.")

        output_dir = os.path.dirname(output_f)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if not overwrite:
            if len(self.check_overwrite()):
                self.__set_status(self.ERROR)
                raise RuntimeError(
                    "Some files already exist. Use the "
                    "overwrite keyword to ignore this "
                    "warning."
                )

        self.__results = None
        self.__overwrite = overwrite

        if callback is not None:
            self.__callback = callback

        if blocking:
            self.__run_convert()
        else:
            thread = self.__thread = Thread(target=self.__run_convert)
            thread.start()

    @qspace_dims.setter
    def qspace_dims(self, qspace_dims):
        """Sets the dimensions of the qspace volume (i.e. number of bins)."""
        if qspace_dims is None or None in qspace_dims:
            self.__params["qspace_dims"] = None
            return

        qspace_dims = np.array(qspace_dims, ndmin=1).astype(np.int32)

        if qspace_dims.ndim != 1 or qspace_dims.size != 3:
            raise ValueError("qspace_dims must be a three elements array.")

        if not np.all(qspace_dims > 1):
            raise ValueError(
                "<qspace_dims> values must be strictly" " greater than one."
            )
        self.__params["qspace_dims"] = qspace_dims

    @normalizer.setter
    def normalizer(self, normalizer):
        """Name of dataset in measurement to use for normalization"""
        if normalizer is not None:
            normalizer = str(normalizer)

            # Check for valid input in all entries
            with XsocsH5.XsocsH5(self.__xsocsH5_f) as xsocsH5:
                for entry in xsocsH5.entries():
                    if xsocsH5.measurement(entry=entry, measurement=normalizer) is None:
                        raise ValueError(
                            "normalizer %s is not available in %s/measurement"
                            % (normalizer, entry)
                        )

        self.__params["normalizer"] = normalizer

    @mask.setter
    def mask(self, mask):
        """Mask array or None to mask pixels in input images"""
        if mask is not None:
            mask = np.array(mask)
            if mask.ndim != 2:
                raise ValueError("Mask is not an image")

            with XsocsH5.XsocsH5(self.__xsocsH5_f) as xsocsH5:
                image_size = xsocsH5.image_size()
                image_roi_offset = xsocsH5.image_roi_offset()
            if image_roi_offset is None:
                image_roi_offset = 0, 0
            if (
                image_size[0] + image_roi_offset[0] > mask.shape[0]
                or image_size[1] + image_roi_offset[1] > mask.shape[1]
            ):
                raise ValueError("Mask is too small for image size and ROI information")

        self.__params["mask"] = mask

    @medfilt_dims.setter
    def medfilt_dims(self, medfilt_dims):
        """Median filter applied to the image after the mask (if any) and
        before converting to qspace.
        """
        err = False
        if medfilt_dims is None:
            self.__params["medfilt_dims"] = (1, 1)
            return

        medfilt_dims_int = None
        if len(medfilt_dims) != 2:
            raise ValueError("medfilt_dims must be a two elements array.")
        if None in medfilt_dims:
            err = True
        else:
            medfilt_dims_int = [int(medfilt_dims[0]), int(medfilt_dims[1])]
            if min(medfilt_dims_int) <= 0:
                err = True
        if err:
            raise ValueError(
                "<medfilt_dims> values must be strictly" " positive integers."
            )
        self.__params["medfilt_dims"] = np.array(medfilt_dims_int, dtype=np.int32)

    @beam_energy.setter
    def beam_energy(self, beam_energy):
        """Beam energy setter"""
        beam_energy = float(beam_energy) if beam_energy is not None else None
        self.__params["beam_energy"] = beam_energy

    @direct_beam.setter
    def direct_beam(self, direct_beam):
        """Direct beam calibration position"""
        if direct_beam is not None:
            direct_beam = float(direct_beam[0]), float(direct_beam[1])
        self.__params["direct_beam"] = direct_beam

    @channels_per_degree.setter
    def channels_per_degree(self, channels_per_degree):
        """Channels per degree calibration"""
        if channels_per_degree is not None:
            channels_per_degree = (
                float(channels_per_degree[0]),
                float(channels_per_degree[1]),
            )
        self.__params["channels_per_degree"] = channels_per_degree

    @coordinates.setter
    def coordinates(self, coordinates):
        """Q vector coordinates system"""
        assert coordinates in QSpaceCoordinates.ALLOWED
        self.__coordinates = coordinates

    @roi.setter
    def roi(self, roi):
        """Sets the roi. Set to None to unset it.

        To change an already set roi the previous one has to be unset first.

        :param roi: roi coordinates in sample coordinates.
            Four elements array : (xmin, xmax, ymin, ymax)
        """
        if self.roi is False:
            raise ValueError(
                "Cannot set a rectangular ROI, pos_indices are "
                "already set, remove them first."
            )
        self.__params["roi"] = roi
        self.__params["sample_indices"] = self.__indices_from_roi()

    def __indices_from_roi(self):
        # TODO : check all positions
        # at the moment using only the first scan's positions
        with XsocsH5.XsocsH5(self.__xsocsH5_f) as xsocsH5:
            entries = xsocsH5.entries()
            positions = xsocsH5.scan_positions(entries[0])
            x_pos = positions.pos_0
            y_pos = positions.pos_1

        if self.__shiftH5:
            with self.__shiftH5:
                shifted_idx = self.__shiftH5.shifted_indices(entries[0])
        else:
            shifted_idx = None

        roi = self.roi
        if self.roi is None:
            if shifted_idx is not None and shifted_idx.size != 0:
                return np.arange(shifted_idx.size)
            return np.arange(len(x_pos))

        if shifted_idx is not None and shifted_idx.size != 0:
            x_pos = x_pos[shifted_idx]
            y_pos = y_pos[shifted_idx]

        x_min = roi[0]
        x_max = roi[1]
        y_min = roi[2]
        y_max = roi[3]

        # we cant do this because the points arent perfectly aligned!
        # we could end up with non rectangular rois
        pos_indices = np.where(
            (x_pos >= x_min) & (x_pos <= x_max) & (y_pos >= y_min) & (y_pos <= y_max)
        )[0]

        # # TODO : rework this
        # n_x = scan_params['motor_0_steps']
        # n_y = scan_params['motor_1_steps']
        # steps_0 = scan_params['motor_0_steps']
        # steps_1 = scan_params['motor_1_steps']
        # x = np.linspace(scan_params['motor_0_start'],
        #                 scan_params['motor_0_end'], steps_0, endpoint=False)
        # y = np.linspace(scan_params['motor_1_start'],
        #                 scan_params['motor_1_end'], steps_1, endpoint=False)

        # x_pos = x_pos[]
        #
        # x_pos.shape = (n_y, n_x)
        # y_pos.shape = (n_y, n_x)
        # pos_indices_2d = np.where((x_pos >= x_min) & (x_pos <= x_max) &
        #                           (y_pos >= y_min) & (y_pos <= y_max))[0]
        return pos_indices  # pos_indices_2d.shape

    def check_overwrite(self):
        """Checks if the output file(s) already exist(s)."""
        output_f = self.__output_f
        if output_f is not None and os.path.exists(output_f):
            return [self.__output_f]
        return []

    def summary(self):
        """Gives an summary of what will be done."""
        # TODO : finish
        files = [self.output_f]
        return files

    def check_parameters(self):
        """Checks if the RecipSpaceConverter parameters are valid.

        :return: a list of strings describing those errors, if any,
            or an empty list.
        """
        errors = []

        qspace_dims = self.qspace_dims
        if (
            qspace_dims is None
            or None in qspace_dims
            or len(qspace_dims) != 3
            or min(qspace_dims) <= 0
        ):
            errors.append(
                '- "qspace size" must be an array of three'
                " strictly positive integers."
            )

        return errors

    def check_consistency(
        self,
        beam_energy_check=True,
        direct_beam_check=True,
        channels_per_degree_check=True,
    ):
        """Check if all entries have the same values plus some other
        MINIMAL checks.

        This does not check if the parameter values are valid.
        Returns a list of strings describing those errors, if any,
        or an empty list.

        :param bool beam_energy_check: Toggle beam_energy check
        :param bool direct_beam_check: Toggle direct_beam check
        :param bool channels_per_degree_check: Toggle channels_per_degree check
        """
        errors = []

        params = _get_all_params(self.__xsocsH5_f)

        def check_values(dic, key, description):
            values = [dic[scan][key] for scan in sorted(dic.keys())]
            if isinstance(values[0], (list, tuple)):
                values = [tuple(val) for val in values]
            values_set = set(values)
            if len(values_set) != 1:
                errors.append(
                    "Parameter inconsistency : "
                    '"{0}" : {1}.'
                    "".format(description, "; ".join(str(m) for m in values_set))
                )

        check_values(params, "n_images", "Number of images")
        check_values(params, "n_positions", "Number of X/Y positions")
        check_values(params, "img_size", "Images size")
        if beam_energy_check:
            # Check that beam_energy is defined in each scan
            if None in [scan_p["beam_energy"] for scan_p in params.values()]:
                errors.append("Beam energy not available for all scans.")
        if channels_per_degree_check:
            check_values(params, "chan_per_deg", "Chan. per deg.")
        if direct_beam_check:
            check_values(params, "center_chan", "Center channel")

        keys = list(params.keys())
        n_images = params[keys[0]]["n_images"]
        n_positions = params[keys[0]]["n_positions"]
        if n_images != n_positions:
            errors.append(
                "number of images != number of X/Y coordinates "
                "on sample : "
                "{0} != {1}".format(n_images, n_positions)
            )

        return errors

    def scan_params(self, scan):
        """Returns the scan parameters (filled during acquisition)."""
        params = _get_all_params(self.__xsocsH5_f)
        return params[scan]

    def __run_convert(self):
        """Performs the conversion."""
        self.__set_status(self.RUNNING)

        normalizer = self.normalizer
        medfilt_dims = self.medfilt_dims
        qspace_dims = self.qspace_dims
        xsocsH5_f = self.xsocsH5_f
        output_f = self.output_f
        sample_roi = self.__params["roi"]
        beam_energy = self.__params["beam_energy"]
        center_chan = self.__params["direct_beam"]
        chan_per_deg = self.__params["channels_per_degree"]

        try:
            # setting medfilt_dims to None if it is equal to [1, 1]
            if medfilt_dims is not None:
                medfilt_dims = np.array(medfilt_dims, ndmin=1)
                if medfilt_dims.ndim != 1:
                    raise ValueError("medfilt_dims must be a 1D array.")
                if medfilt_dims.size > 2:
                    raise ValueError(
                        "medfilt_dims must be a one or two elements" " array."
                    )
                if medfilt_dims.size == 1:
                    medfilt_dims = np.repeat(medfilt_dims, 2)
                if np.any(np.less(medfilt_dims, [1, 1])):
                    raise ValueError("medfilt_dims values must be >= 1.")

            ta = time.time()

            params = _get_all_params(xsocsH5_f)

            entries = self.__get_scans()
            n_entries = len(entries)

            first_param = params[entries[0]]

            if beam_energy is None:
                # Load it from entries
                beam_energy = [scan_p["beam_energy"] for scan_p in params.values()]
                if None in beam_energy:
                    raise ValueError("Missing beam energy: {0}".format(beam_energy))

            if chan_per_deg is None:  # Load it from first entry
                chan_per_deg = first_param["chan_per_deg"]
            if chan_per_deg is None or len(chan_per_deg) != 2:
                raise ValueError(
                    "Invalid/missing chan_per_deg value : {0}." "".format(chan_per_deg)
                )

            if center_chan is None:  # Load it from first entry
                center_chan = first_param["center_chan"]
            if center_chan is None or len(center_chan) != 2:
                raise ValueError(
                    "Invalid/missing center_chan value : {0}." "".format(center_chan)
                )

            # Load image ROI from first entry
            image_roi_offset = first_param["image_roi_offset"]
            if image_roi_offset is None:  # No image ROI offset
                image_roi_offset = 0, 0

            n_images = first_param["n_images"]
            if n_images is None or n_images == 0:
                raise ValueError(
                    "Data does not contain any images (n_images={0})."
                    "".format(n_images)
                )

            img_size = first_param["img_size"]
            if img_size is None or 0 in img_size:
                raise ValueError(
                    "Invalid image size (img_size={0})." "".format(img_size)
                )

            mask = self.mask
            if mask is not None:
                if np.count_nonzero(mask) == mask.size:
                    # Mask is empty, disable mask
                    mask = None
                else:
                    # Apply image ROI to mask
                    row, column = image_roi_offset
                    mask = mask[row : row + img_size[0], column : column + img_size[1]]

                    if mask.shape != img_size:
                        raise ValueError("Invalid mask size")

            if self.maxipix_correction and (
                image_roi_offset[0] + img_size[0] > 516
                or image_roi_offset[1] + img_size[1] > 516
            ):
                # Maxipix correction for something else
                raise ValueError("Invalid image size for Maxipix correction")

            shiftH5 = self.__shiftH5

            if shiftH5:
                shifted_idx = shiftH5.shifted_indices(entries[0])
                if shifted_idx is not None and shifted_idx.size > 0:
                    n_images = shifted_idx.size
                else:
                    shifted_idx = None
            else:
                shifted_idx = None

            # TODO value testing
            sample_indices = self.sample_indices
            if sample_indices is None:
                sample_indices = np.arange(n_images)
            else:
                n_images = len(sample_indices)

            n_xy = len(sample_indices)

            _logger.info("Parameters :")
            _logger.info(
                "\t- beam energy        : {0}".format(
                    self.beam_energy
                    if self.beam_energy is not None
                    else "Loaded from scans"
                )
            )
            _logger.info("\t- center channel     : {0}".format(center_chan))
            _logger.info("\t- image roi offset   : {0}".format(image_roi_offset))
            _logger.info("\t- channel per degree : {0}".format(chan_per_deg))
            _logger.info("\t- maxipix correction : {0}".format(self.maxipix_correction))
            _logger.info(
                "\t- mask               : {0}".format(
                    "Yes" if mask is not None else "No"
                )
            )
            _logger.info("\t- normalizer         : {0}".format(normalizer))
            _logger.info("\t- medfilt dims       : {0}".format(medfilt_dims))
            _logger.info("\t- qspace size        : {0}".format(qspace_dims))
            _logger.info("\t- coordinate system  : {0}".format(self.coordinates))

            # Offset center_chan with image roi offset if any
            center_chan = (
                center_chan[0] - image_roi_offset[0],
                center_chan[1] - image_roi_offset[1],
            )

            ndim0, ndim1, ndim2 = qspace_dims

            img_dtype = None
            phi = []
            eta = []
            nu = []
            delta = []

            with XsocsH5.XsocsH5(xsocsH5_f, mode="r") as master_h5:
                entry_files = []

                all_entries = set(master_h5.entries())

                positions = master_h5.scan_positions(entries[0])
                sample_x = positions.pos_0
                sample_y = positions.pos_1

                if shifted_idx is not None:
                    sample_x = sample_x[shifted_idx]
                    sample_y = sample_y[shifted_idx]

                for entry in entries:
                    entry_file = master_h5.entry_filename(entry)
                    if not os.path.isabs(entry_file):
                        base_dir = os.path.dirname(xsocsH5_f)
                        entry_file = os.path.abspath(os.path.join(base_dir, entry_file))
                    entry_files.append(entry_file)

                    phi.append(master_h5.positioner(entry, "phi"))
                    eta.append(master_h5.positioner(entry, "eta"))
                    nu.append(master_h5.positioner(entry, "nu"))
                    delta.append(master_h5.positioner(entry, "del"))

                    entry_dtype = master_h5.image_dtype(entry=entry)

                    if img_dtype is None:
                        img_dtype = entry_dtype
                    elif img_dtype != entry_dtype:
                        raise TypeError(
                            "All images in the input HDF5 files should "
                            "be of the same type. Found {0} and {1}."
                            "".format(img_dtype, entry_dtype)
                        )

            # Convert image pixel positions to Q space
            q_ar = qspace_conversion(
                img_size,
                center_chan,
                chan_per_deg,
                beam_energy,
                phi,
                eta,
                nu,
                delta,
                coordinates=self.coordinates,
            )
            # Reshape array to flatten image
            q_ar.shape = q_ar.shape[0], q_ar.shape[1] * q_ar.shape[2], q_ar.shape[3]

            if mask is not None:
                # Mark masked pixels (i.e., non zero in the mask) with NaN
                q_ar[:, mask.reshape(-1) != 0, :] = np.nan

            # custom bins range to have the same histo as
            # xrayutilities.gridder3d
            # bins centered around the qdim0, qdim1, qdim2
            # bins will be like :
            # bin_1 = [min - step/2, min + step/2[
            # bin_2 = [min - step/2, min + 3*step/2]
            # ...
            # bin_N = [max - step/2, max + step/2]
            qdim0_min = np.nanmin(q_ar[:, :, 0])
            qdim1_min = np.nanmin(q_ar[:, :, 1])
            qdim2_min = np.nanmin(q_ar[:, :, 2])
            qdim0_max = np.nanmax(q_ar[:, :, 0])
            qdim1_max = np.nanmax(q_ar[:, :, 1])
            qdim2_max = np.nanmax(q_ar[:, :, 2])

            step_dim0 = (qdim0_max - qdim0_min) / (ndim0 - 1.0)
            step_dim1 = (qdim1_max - qdim1_min) / (ndim1 - 1.0)
            step_dim2 = (qdim2_max - qdim2_min) / (ndim2 - 1.0)

            qdim0_bin_centers = qdim0_min + step_dim0 * np.arange(
                0, ndim0, dtype=np.float64
            )
            qdim1_bin_centers = qdim1_min + step_dim1 * np.arange(
                0, ndim1, dtype=np.float64
            )
            qdim2_bin_centers = qdim2_min + step_dim2 * np.arange(
                0, ndim2, dtype=np.float64
            )

            bins_rng = [
                bin_centers_to_range_step(qdim0_bin_centers)[:2],
                bin_centers_to_range_step(qdim1_bin_centers)[:2],
                bin_centers_to_range_step(qdim2_bin_centers)[:2],
            ]

            # TODO : on windows we may be forced to use shared memory
            # TODO : find why we use more memory when using shared arrays
            #        this shouldnt be the case
            #        (use the same amount as non shared mem)
            # on linux apparently we dont because when fork() is called data is
            # only copied on write.
            # shared histo used by all processes
            # histo_shared = mp_sharedctypes.RawArray(ctypes.c_int32,
            #                                         ndim0 * ndim1 * ndim2)
            # histo = np.frombuffer(histo_shared, dtype='int32')
            # histo.shape = ndim0, ndim1, ndim2
            # histo[:] = 0
            histo = np.zeros(qspace_dims, dtype=np.int32)

            # shared LUT used by all processes
            # h_lut = None
            # h_lut_shared = None
            h_lut = []
            lut = None
            for h_idx in range(n_entries):
                lut = histogramnd_get_lut(
                    q_ar[h_idx, ...],
                    bins_rng,
                    [ndim0, ndim1, ndim2],
                    last_bin_closed=True,
                )

                # if h_lut_shared is None:
                #     lut_dtype = lut[0].dtype
                #     if lut_dtype == np.int16:
                #         lut_ctype = ctypes.c_int16
                #     elif lut_dtype == np.int32:
                #         lut_ctype = ctypes.c_int32
                #     elif lut_dtype == np.int64:
                #         lut_ctype == ctypes.c_int64
                #     else:
                #         raise TypeError('Unknown type returned by '
                #                         'histogramnd_get_lut : {0}.'
                #                         ''.format(lut.dtype))
                #     h_lut_shared = mp_sharedctypes.RawArray(lut_ctype,
                #                                       n_images * lut[0].size)
                #     h_lut = np.frombuffer(h_lut_shared, dtype=lut_dtype)
                #     h_lut.shape = (n_images, -1)
                #
                # h_lut[h_idx, ...] = lut[0]
                h_lut.append(lut[0])
                histo += lut[1]

            del lut
            del q_ar

            # TODO : split the output file into several files? speedup?
            output_shape = histo.shape

            chunks = (
                1,
                max(output_shape[0] // 4, 1),
                max(output_shape[1] // 4, 1),
                max(output_shape[2] // 4, 1),
            )
            qspace_sum_chunks = (max(n_images // 10, 1),)

            discarded_entries = sorted(all_entries - set(entries))

            _create_result_file(
                output_f,
                output_shape,
                medfilt_dims,
                sample_roi,
                sample_x[sample_indices],
                sample_y[sample_indices],
                qdim0_bin_centers,
                qdim1_bin_centers,
                qdim2_bin_centers,
                histo,
                selected_entries=entries,
                discarded_entries=discarded_entries,
                compression=config.DEFAULT_HDF5_COMPRESSION,
                qspace_chunks=chunks,
                qspace_sum_chunks=qspace_sum_chunks,
                overwrite=self.__overwrite,
                shiftH5=shiftH5,
                beam_energy=self.beam_energy,
                direct_beam=center_chan,
                channels_per_degree=chan_per_deg,
                normalizer=normalizer,
                mask=mask,
                maxipix_correction=self.maxipix_correction,
                coordinates=self.coordinates,
            )

            manager = mp.Manager()
            self.__term_evt = term_evt = manager.Event()

            write_lock = manager.Lock()
            idx_queue = manager.Queue()

            self.__shared_progress = mp_sharedctypes.RawArray(
                ctypes.c_int32, self.n_proc
            )
            np.frombuffer(self.__shared_progress, dtype="int32")[:] = 0

            if shiftH5 is not None and shifted_idx is not None:
                n_shifted = n_entries * shifted_idx.size
                shared_shifted = mp_sharedctypes.RawArray(ctypes.c_int32, n_shifted)
                shifted_np = np.frombuffer(shared_shifted, dtype="int32")
                shifted_np.shape = n_entries, shifted_idx.size
                shared_shifted_shape = shifted_np.shape

                for i_entry, entry in enumerate(entries):
                    shifted_indices = shiftH5.shifted_indices(entry)
                    shifted_np[i_entry, :] = shifted_indices
            else:
                shared_shifted = None
                shared_shifted_shape = None

            pool = mp.Pool(
                self.n_proc,
                initializer=_init_thread,
                initargs=(
                    idx_queue,
                    write_lock,
                    bins_rng,
                    qspace_dims,
                    h_lut,  # _shared,
                    None,  # lut_dtype,
                    n_xy,
                    histo,  # _shared,))
                    self.__shared_progress,
                    term_evt,
                    shared_shifted,
                    shared_shifted_shape,
                ),
            )

            if disp_times:

                class MyTimes(object):
                    def __init__(self):
                        self.t_histo = 0.0
                        self.t_sum = 0.0
                        self.t_mask = 0.0
                        self.t_read = 0.0
                        self.t_context = 0.0
                        self.t_preprocess = 0.0
                        self.t_medfilt = 0.0
                        self.t_write = 0.0
                        self.t_w_lock = 0.0

                    def update(self, arg):
                        (
                            t_read_,
                            t_context_,
                            t_preprocess_,
                            t_medfilt_,
                            t_histo_,
                            t_mask_,
                            t_sum_,
                            t_write_,
                            t_w_lock_,
                        ) = arg[2]
                        self.t_histo += t_histo_
                        self.t_sum += t_sum_
                        self.t_mask += t_mask_
                        self.t_read += t_read_
                        self.t_context += t_context_
                        self.t_preprocess += t_preprocess_
                        self.t_medfilt += t_medfilt_
                        self.t_write += t_write_
                        self.t_w_lock += t_w_lock_

                res_times = MyTimes()
                callback = res_times.update
            else:
                callback = None

            # creating the processes
            results = []
            for th_idx in range(self.n_proc):
                arg_list = (
                    th_idx,
                    entry_files,
                    entries,
                    image_roi_offset,
                    img_size,
                    output_f,
                    self.maxipix_correction,
                    normalizer,
                    medfilt_dims,
                    img_dtype,
                )
                res = pool.apply_async(_to_qspace, args=arg_list, callback=callback)
                results.append(res)
            # sending the image indices
            for result_idx, pos_idx in enumerate(sample_indices):
                idx_queue.put((result_idx, pos_idx))

            # sending the None value to let the threads know that they
            # should return
            for th_idx in range(self.n_proc):
                idx_queue.put(None)

            pool.close()
            pool.join()

            tb = time.time()

            if disp_times:
                _logger.info("TOTAL {0}".format(tb - ta))
                _logger.info("Read {0}".format(res_times.t_read))
                _logger.info("Context {0}".format(res_times.t_context))
                _logger.info("Preprocess {0}".format(res_times.t_preprocess))
                _logger.info("Medfilt {0}".format(res_times.t_medfilt))
                _logger.info("Histo {0}".format(res_times.t_histo))
                _logger.info("Mask {0}".format(res_times.t_mask))
                _logger.info("Sum {0}".format(res_times.t_sum))
                _logger.info("Write {0}".format(res_times.t_write))
                _logger.info("(lock : {0})".format(res_times.t_w_lock))

            proc_results = [result.get() for result in results]
            proc_codes = np.array([proc_result[0] for proc_result in proc_results])

            rc = self.DONE
            if not np.all(proc_codes == self.DONE):
                if self.ERROR in proc_codes:
                    rc = self.ERROR
                elif self.CANCELED in proc_codes:
                    rc = self.CANCELED
                else:
                    raise ValueError("Unknown return code.")

            if rc != self.DONE:
                errMsg = "Conversion failed. Process status :"
                for th_idx, result in enumerate(proc_results):
                    errMsg += "\n- Proc {0} : rc={1}; {2}" "".format(
                        th_idx, result[0], result[1]
                    )
                self.__set_status(rc, errMsg)
            else:
                self.__set_status(rc)

        except Exception as ex:
            self.__set_status(self.ERROR, str(ex))
        else:
            self.__results = self.output_f

        # TODO : catch exception?
        if self.__callback:
            self.__callback()

        return self.__results

    def wait(self):
        """Waits until parsing is done, or returns if it is not running."""
        if self.__thread:
            self.__thread.join()

    def __running_exception(self):
        """Raises an exception if a conversion is in progress."""
        if self.is_running():
            raise RuntimeError(
                "Operation not permitted while " "a parse or merge in running."
            )

    def is_running(self):
        """Returns True if a conversion is in progress."""
        return self.status == QSpaceConverter.RUNNING
        # self.__thread and self.__thread.is_alive()

    @output_f.setter
    def output_f(self, output_f):
        """Sets the output file."""
        if not isinstance(output_f, str):
            raise TypeError(
                "output_f must be a string. Received {0}" "".format(type(output_f))
            )
        self.__output_f = output_f

    @n_proc.setter
    def n_proc(self, n_proc):
        if n_proc is None:
            n_proc = config.DEFAULT_PROCESS_NUMBER

        n_proc = int(n_proc)
        if n_proc <= 0:
            raise ValueError("n_proc must be strictly positive")
        self.__n_proc = n_proc

    def abort(self, wait=True):
        """Aborts the current conversion, if any.

        :param wait: set to False to return immediatly without waiting for the
            processes to return.
        """
        if self.is_running():
            self.__term_evt.set()
            if wait:
                self.wait()

    def progress(self):
        """Returns the progress of the conversion."""
        if self.__shared_progress:
            progress = np.frombuffer(self.__shared_progress, dtype="int32")
            return progress.max()
        return 0


def _init_thread(
    idx_queue_,
    write_lock_,
    bins_rng_,
    qspace_size_,
    h_lut_shared_,
    h_lut_dtype_,
    n_xy_,
    histo_shared_,
    shared_progress_,
    term_evt_,
    shared_shifted_,
    shared_shifted_shape_,
):
    global idx_queue, write_lock, bins_rng, qspace_size, h_lut_shared, h_lut_dtype, n_xy
    global histo_shared, shared_progress, term_evt, shared_shifted, shared_shifted_shape

    idx_queue = idx_queue_
    write_lock = write_lock_
    bins_rng = bins_rng_
    qspace_size = qspace_size_
    h_lut_shared = h_lut_shared_
    h_lut_dtype = h_lut_dtype_
    n_xy = n_xy_
    histo_shared = histo_shared_
    shared_progress = shared_progress_
    term_evt = term_evt_
    shared_shifted = shared_shifted_
    shared_shifted_shape = shared_shifted_shape_


def _create_result_file(
    h5_fn,
    qspace_dims,
    medfilt_dims,
    sample_roi,
    pos_x,
    pos_y,
    q_dim0,
    q_dim1,
    q_dim2,
    histo,
    selected_entries,
    discarded_entries=None,
    compression="DEFAULT",
    qspace_chunks=None,
    qspace_sum_chunks=None,
    overwrite=False,
    shiftH5=None,
    beam_energy=None,
    direct_beam=None,
    channels_per_degree=None,
    normalizer="",
    mask=None,
    maxipix_correction=False,
    coordinates=QSpaceCoordinates.CARTESIAN,
):
    """Initializes the output file.

    :param h5_fn: name of the file to initialize
    :param qspace_dims: dimensions of the q space
    :param medfilt_dims: dimensions of the median filter applied to the image
        after the mask (if any).
    :param pos_x: sample X positions (one for each qspace cube)
    :param pos_y: sample Y positions (one for each qspace cube)
    :param q_dim0: X coordinates of the qspace cube
    :param q_dim1: Y coordinates of the qspace cube
    :param q_dim2: Z coordinates of the qspace cube
    :param histo: histogram (number of hits per element of the qspace elements)
    :param selected_entries: list of input entries used for the conversion
    :param discarded_entries: list of input entries discarded, or None
    :param compression: datasets compression
    :param qspace_chunks: qspace chunking
    :param qspace_sum_chunks:
    :param overwrite: True to force overwriting the file if it already exists.
    :param shiftH5: file containing the shifts applied to the selected entries
    :param beam_energy: Beam energy in eV
    :param direct_beam: Direct beam calibration position
    :param channels_per_degree: Channels per degree calibration
    :param str normalizer:
        Name of measurement group dataset used for normalization
    :param Union[numpy.ndarray, None] mask:
        Mask used to discard pixels in images
    :param bool maxipix_correction:
        Whether or not to apply a correction for maxipix module edges
    :param QSpaceCoordinates coordinates:
        Coordinate system used to compute QSpace
    """

    if not overwrite:
        mode = "w-"
    else:
        mode = "w"

    dir_name = os.path.dirname(h5_fn)
    if len(dir_name) > 0 and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    if compression == "DEFAULT":
        compression = config.DEFAULT_HDF5_COMPRESSION

    qspace_h5 = QSpaceH5.QSpaceH5Writer(h5_fn, mode=mode)
    qspace_h5.init_file(
        len(pos_x),
        qspace_dims,
        qspace_chunks=qspace_chunks,
        qspace_sum_chunks=qspace_sum_chunks,
        compression=compression,
        coordinates=coordinates,
    )
    qspace_h5.set_histo(histo)
    qspace_h5.set_sample_x(pos_x)
    qspace_h5.set_sample_y(pos_y)
    qspace_h5.set_qspace_dimension_values(q_dim0, q_dim1, q_dim2)
    qspace_h5.set_medfilt_dims(medfilt_dims)
    qspace_h5.set_sample_roi(sample_roi)
    if beam_energy is not None:
        qspace_h5.set_beam_energy(beam_energy)
    qspace_h5.set_direct_beam(direct_beam)
    qspace_h5.set_channels_per_degree(channels_per_degree)
    qspace_h5.set_maxipix_correction(maxipix_correction)

    if normalizer is None:
        normalizer = ""
    qspace_h5.set_image_normalizer(normalizer)

    if mask is not None:
        qspace_h5.set_image_mask(mask)

    if shiftH5:
        sample_shifts = []
        grid_shifts = []
        with shiftH5:
            for entry in selected_entries:
                shift = shiftH5.shift(entry)

                if shift is not None:
                    sample_shifts.append([shift["shift_x"], shift["shift_y"]])
                    if shiftH5.is_snapped_to_grid():
                        grid_shifts.append(shift["grid_shift"])

        if len(grid_shifts) == 0:
            grid_shifts = None
    else:
        sample_shifts = None
        grid_shifts = None

    qspace_h5.set_entries(
        selected_entries,
        discarded=discarded_entries,
        sample_shifts=sample_shifts,
        grid_shifts=grid_shifts,
    )


def _to_qspace(
    th_idx,
    entry_files,
    entries,
    image_roi_offset,
    img_size,
    output_fn,
    maxipix_correction,
    normalizer,
    medfilt_dims,
    img_dtype,
):
    """Function running in a process. Performs the conversion.

    :param th_idx:
    :param entry_files:
    :param entries:
    :param image_roi_offset: Offset of detector image ROI (row, col)
    :param img_size:
    :param output_fn:
    :param bool maxipix_correction:
        Whether to apply maxipix correction or not
    :param str normalizer:
       Name of measurement group dataset to use for normalization
    :param medfilt_dims:
    :param img_dtype:
    """
    print("Process {0} started.".format(th_idx))

    t_histo = 0.0
    t_mask = 0.0
    t_sum = 0.0
    t_read = 0.0
    t_preprocess = 0.0
    t_medfilt = 0.0
    t_write = 0.0
    t_w_lock = 0.0
    t_context = 0.0

    write_lock.acquire()
    output_h5 = QSpaceH5.QSpaceH5Writer(output_fn, mode="r+")
    write_lock.release()

    if shared_progress is not None:
        progress_np = np.frombuffer(shared_progress, dtype="int32")
        progress_np[th_idx] = 0
    else:
        progress_np = None

    if shared_shifted is not None:
        shifted_np = np.frombuffer(shared_shifted, dtype="int32")
        shifted_np.shape = shared_shifted_shape
    else:
        shifted_np = None

    # histo = np.frombuffer(histo_shared, dtype='int32')
    # histo.shape = qspace_size
    # histo = histo_shared
    # mask = histo > 0

    # h_lut = np.frombuffer(h_lut_shared, dtype=h_lut_dtype)
    # h_lut.shape = (n_xy, -1)
    h_lut = h_lut_shared

    if (maxipix_correction or normalizer) and img_dtype.kind != "f":
        # Force the type to float64
        _logger.info("Using float64")
        img_dtype = np.float64

    img = np.ascontiguousarray(np.zeros(img_size), dtype=img_dtype)

    rc = None
    errMsg = None
    try:
        # Open all input files
        inputsH5 = []
        for entry_file in entry_files:
            h5f = XsocsH5.XsocsH5(entry_file, mode="r")
            h5f.open()
            inputsH5.append(h5f)

        while True:
            if term_evt.is_set():  # noqa
                rc = QSpaceConverter.CANCELED
                raise Exception("conversion aborted")

            next_data = idx_queue.get()
            if next_data is None:
                rc = QSpaceConverter.DONE
                break

            result_idx, image_idx = next_data
            if result_idx % 100 == 0:
                print("#{0}/{1}".format(result_idx, n_xy))

            cumul = None
            # histo = None

            if shifted_np is not None:
                image_indices = shifted_np[:, image_idx]
            else:
                image_indices = None

            for entry_idx, entry in enumerate(entries):
                xsocsH5 = inputsH5[entry_idx]

                t0 = time.time()

                if image_indices is not None:
                    image_idx = image_indices[entry_idx]

                try:
                    # TODO : there s room for improvement here maybe
                    # (recreating a XsocsH5 instance each time slows down
                    # slows down things a big, not much tho)
                    # TODO : add a lock on the files if there is no SWMR
                    # test if it slows down things much
                    with xsocsH5.image_dset_ctx() as img_data:
                        t1 = time.time()
                        img_data.read_direct(
                            img, source_sel=np.s_[image_idx], dest_sel=None
                        )
                        t_context = time.time() - t1
                        # img = img_data[image_idx].astype(np.float64)
                except Exception as ex:
                    raise RuntimeError(
                        "Error in proc {0} while reading "
                        "img {1} from entry {2} ({3}) : {4}."
                        "".format(th_idx, image_idx, entry_idx, entry, ex)
                    )

                t_read += time.time() - t0
                t0 = time.time()

                # Apply maxipix correction

                if maxipix_correction:
                    # Correction without image ROI, kept for readability
                    # img[255:258] = img[255] / 3
                    # img[258:261] = img[260] / 3
                    # img[:, 255:258] = (img[:, 255] / 3)[:, None]
                    # img[:, 258:261] = (img[:, 260] / 3)[:, None]

                    # Apply correction taking image ROI offset into account
                    # Skip correction if row/column with signal is outside ROI
                    row, column = image_roi_offset
                    if row <= 255 < row + img_size[0]:
                        img[255 - row : 258 - row] = img[255 - row] / 3
                    if row <= 260 < row + img_size[0]:
                        img[max(0, 258 - row) : 261 - row] = img[260 - row] / 3
                    if column <= 255 < column + img_size[1]:
                        img[:, 255 - column : 258 - column] = (
                            img[:, 255 - column] / 3
                        )[:, None]
                    if column <= 260 < column + img_size[1]:
                        img[:, max(0, 258 - column) : 261 - column] = (
                            img[:, 260 - column] / 3
                        )[:, None]

                # Apply normalization

                if normalizer:
                    normalization = xsocsH5.measurement(entry, normalizer)
                    # Make sure to use float to perform division
                    assert img.dtype.kind == "f"
                    img /= normalization[image_idx]

                intensity = img

                t_preprocess += time.time() - t0
                t0 = time.time()

                # intensity = medfilt2d(intensity, 3)
                if medfilt_dims[0] != 1 or medfilt_dims[1] != 1:
                    intensity = medfilt2d(
                        intensity, medfilt_dims, mode="constant", cval=0
                    )

                t_medfilt += time.time() - t0
                t0 = time.time()

                if silx.hexversion < 0x10100F0 and intensity.dtype == np.uint16:
                    # silx < 1.1.0 histogramnd_lut lacks uint16 supports
                    # see https://github.com/silx-kit/silx/pull/3670
                    intensity = intensity.astype("float64")

                try:
                    cumul = histogramnd_from_lut(
                        intensity.reshape(-1),
                        h_lut[entry_idx],
                        shape=qspace_size,
                        weighted_histo=cumul,
                        dtype=np.float64,
                    )[1]
                except Exception as ex:
                    print("EX2 {0}".format(str(ex)))
                    raise ex

                t_histo += time.time() - t0

            t0 = time.time()
            cumul_sum = cumul.sum(dtype=np.float64)
            t_sum += time.time() - t0

            t0 = time.time()
            # cumul[mask] = cumul[mask]/histo[mask]
            t_mask += time.time() - t0

            t0 = time.time()
            write_lock.acquire()
            t_w_lock += time.time() - t0
            t0 = time.time()
            try:
                output_h5.set_position_data(result_idx, cumul, cumul_sum)
            except Exception as ex:
                raise RuntimeError(
                    "Error in proc {0} while writing result "
                    "for img {1} (idx = {3}) : {2}.)"
                    "".format(th_idx, image_idx, ex, result_idx)
                )
            write_lock.release()

            if progress_np is not None:
                progress_np[th_idx] = round(100.0 * (result_idx + 1.0) / n_xy)

            t_write += time.time() - t0

        # Close input files
        for h5f in inputsH5:
            h5f.close()

    except Exception as ex:
        if rc is None:
            rc = QSpaceConverter.ERROR
        errMsg = "In thread {0} : {1}.".format(th_idx, str(ex))
        term_evt.set()

    if rc is None:
        rc = QSpaceConverter.DONE

    if disp_times:
        print(
            "Thread {0} is done. Times={1}"
            "".format(
                th_idx,
                (
                    t_read,
                    t_context,
                    t_preprocess,
                    t_medfilt,
                    t_histo,
                    t_mask,
                    t_sum,
                    t_write,
                    t_w_lock,
                ),
            )
        )
    return [
        rc,
        errMsg,
        (
            t_read,
            t_context,
            t_preprocess,
            t_medfilt,
            t_histo,
            t_mask,
            t_sum,
            t_write,
            t_w_lock,
        ),
    ]


def _get_all_params(data_h5f):
    """Read the whole data and returns the parameters for each entry.

    Returns a dictionary with the scans as keys and the following fields :
    n_images, n_positions, img_size, beam_energy, chan_per_deg,
    center_chan
    Each of those fields are N elements arrays, where N is the number of
    scans found in the file.
    """
    result = {}
    with XsocsH5.XsocsH5(data_h5f, mode="r") as master_h5:
        for entry in master_h5.entries():
            imgnr = master_h5.measurement(entry, "imgnr")

            result[entry] = dict(
                scans=entry,
                n_images=master_h5.n_images(entry=entry),
                n_positions=len(imgnr) if imgnr is not None else None,
                img_size=master_h5.image_size(entry=entry),
                beam_energy=master_h5.beam_energy(entry=entry),
                chan_per_deg=master_h5.chan_per_deg(entry=entry),
                center_chan=master_h5.direct_beam(entry=entry),
                image_roi_offset=master_h5.image_roi_offset(entry=entry),
                angle=master_h5.positioner(entry, "eta"),
            )
    return result
