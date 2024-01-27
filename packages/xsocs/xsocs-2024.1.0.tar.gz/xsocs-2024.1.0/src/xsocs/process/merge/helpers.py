import os

from ... import config
from . import KmapMerger
from . import KmapSpecParser


def merge_scan_data(
    output_dir,
    spec_fname,
    beam_energy=None,
    chan_per_deg=None,
    center_chan=None,
    scan_ids=None,
    img_dir=None,
    n_proc=None,
    version=1,
    nr_padding=None,
    nr_offset=None,
    compression="DEFAULT",
    overwrite=False,
    image_roi=None,
):
    """
    Creates a "master" HDF5 file and one HDF5 per scan. Those scan HDF5 files
    contain spec data (from *spec_fname*) as well as the associated
    image data. This file will either contain all valid scans or the one
    selected using the scan_ids parameter. A valid scan is a scan associated
    with an (existing) image file. Existing output files will be
    overwritten.

    :param str output_dir: folder name into which output data
        (as well as temporary files) will be written.

    :param str spec_fname: path to the spec file.

    :param float beam_energy: beam energy in ....

    :param chan_per_deg: 2 elements array containing the number of channels
        per degree (v, h) (as defined by xrayutilitied, used when converting to
        reciprocal space coordinates).
    :type chan_per_deg: array_like

    :param center_chan: 2 elements array containing the coordinates (v, h) of
        the direct beam position in the detector coordinates.
    :type center_chan: *optional* array_like

    :param scan_ids: array of scan numbers to add to the merged file.
        If None, all valid scans will be merged.
    :type scan_ids: *optional* array of int

    :param str img_dir: directory path. If provided the image files will be
        looked for into that folder instead of the one found in the scan
        headers.

    :param Union[int,None] n_proc:
        Number of threads to use when merging files.
        If None, the number of processes used will be the
        default config value (usually the number of cores).

    :param int version: version of the spec file.
        It is currently used to get the offset and padding to apply to
        the nextNr value found in the spec scan headers.
        This nextNr is then used to generate the image file name.
        Set it to 0 if you are merging data generated before April 2016 (TBC).

    :param int nr_padding: zero padding to apply to the nextNr number found
        in the SPEC file.

    :param int nr_offset:
        Offset to apply to the nextNr number found in the SPEC file.

    :param Union[str,int] compression: The HDF5 compression to use.

    :param bool overwrite: True to allow overwriting already existing output file

    :param Union[List[int],None] image_roi:
        Detector image ROI (origin_row, origin_column, height, width) to save,
        or None (default) to save the whole image

    :returns: a list of scan IDs that were merged
    :rtype: List
    """

    base_spec = os.path.basename(spec_fname)

    spec_h5 = os.path.join(output_dir, "{}.h5".format(base_spec))

    if os.path.exists(spec_h5) and not overwrite:
        raise ValueError("The temporary file {0} already exists." "".format(spec_h5))

    parser = KmapSpecParser(
        spec_fname,
        spec_h5,
        img_dir=img_dir,
        version=version,
        nr_padding=nr_padding,
        nr_offset=nr_offset,
    )

    parser.parse()

    if parser.status != KmapSpecParser.DONE:
        raise ValueError(
            "Parsing failed with error code {0}:{1}"
            "".format(parser.status, parser.statusMsg)
        )

    p_results = parser.results

    merger = KmapMerger(p_results.spec_h5, p_results, output_dir)

    merger.beam_energy = beam_energy
    merger.center_chan = center_chan
    merger.chan_per_deg = chan_per_deg
    merger.n_proc = n_proc
    if compression == "DEFAULT":
        compression = config.DEFAULT_HDF5_COMPRESSION
    merger.compression = compression
    merger.image_roi = image_roi

    merger.select(scan_ids, clear=True)

    merger.output_dir = output_dir

    merger.merge(overwrite=overwrite)

    if merger.status != KmapMerger.DONE:
        raise ValueError("Merging failed with error code {0}" "".format(parser.status))

    m_results = merger.results

    return m_results
