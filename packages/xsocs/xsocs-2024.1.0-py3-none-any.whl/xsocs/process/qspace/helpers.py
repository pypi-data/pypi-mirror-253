from .QSpaceConverter import QSpaceConverter


def kmap_2_qspace(
    xsocsH5_f,
    output_f,
    qspace_dims,
    medfilt_dims=None,
    maxipix_correction=False,
    normalizer=None,
    roi=None,
    mask=None,
    n_proc=None,
    overwrite=False,
):
    """
    :param xsocsH5_f: path to the HDF5 file containing the scan counters
        and images
    :type xsocsH5_f: `str`

    :param output_f: name of the file that will contain the conversion results.
    :type output_f: `str`

    :param qspace_dims: qspace dimensions along the qx, qy and qz axis.
    :type qspace_dims: `array_like`

    :param medfilt_dims: 2-tuple indicating size of median filter to be
        applied to each detector image.
    :type medfilt_dims: `array_like`

    :param maxipix_correction: if True, interpolate the maxipix4 gaps
    :type maxipix_correction: bool

    :param normalizer: spec file column containing the intensity
        of the incident beam for normalization
    :type normalizer: `str`

    :param output_f: Name of the output file the results will written to. This
        file will be created in *output_dir*. If not set, the file will be
        named 'qspace.h5'. This file will be overwritten if it already exists.
    :type output_f: *optional* str

    :param roi: rectangular region which will be converted to qspace.
        This must be a four elements array containing x_min, x_max, y_min,
        y_max.
    :type roi: *optional* `array_like` (x_min, x_max, y_min, y_max)

    :param mask: mask array indicating bad pixels of the detector.
         A non-zero value means that the pixel is masked.
    :type mask: *optional* 2D numpy.ndarray

    :param Union[int,None] n_proc:
        number of process to use.
        If None, the number of processes used will be the
        default config value (usually the number of cores).

    :param overwrite: if set to False, an exception will be raise if the output
        file already exists.
    :type overwrite: bool
    """
    converter = QSpaceConverter(
        xsocsH5_f, qspace_dims, roi=roi, medfilt_dims=medfilt_dims, output_f=output_f
    )

    converter.maxipix_correction = maxipix_correction
    converter.normalizer = normalizer
    converter.mask = mask

    converter.n_proc = n_proc

    converter.convert(overwrite=overwrite)

    rc = converter.status

    if rc != QSpaceConverter.DONE:
        raise ValueError(
            "Conversion failed with CODE={0} :\n"
            "{1}"
            ""
            "".format(converter.status, converter.status_msg)
        )
