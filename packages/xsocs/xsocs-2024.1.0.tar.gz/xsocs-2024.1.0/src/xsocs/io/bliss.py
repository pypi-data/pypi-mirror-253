import logging
import os
import numpy as np
import h5py
import xrayutilities as xu
import re

from xsocs.io import XsocsH5


_logger = logging.getLogger(__name__)


def get_detector_aliases(h5f, scan_no):
    groups = tuple(h5f[f"{scan_no}/measurement/"].keys())
    aliases = ("mpx1x4", "mpxgaas", "eiger2M")
    detectors = [d for d in aliases if d in groups]

    if len(detectors) > 0:
        return detectors
    else:
        msg = f"No detector group found in {h5f.name}:/{scan_no}/measurement/"
        raise Exception(msg)


def parse_scan_command(command):
    """
    Accepts an SXDM command and parses it according to the XSOCS
    file strucure. Distinguishes between commands with SPEC-like syntax
    (i.e. only spaces) and BLISS-like syntax (commas and parentheses).
    This is necessary due to an evolving HDF5 structure.
    """

    _COMMAND_LINE_PATTERN_BLISS = (
        r"^(?P<command>[^ ]*)\( "
        r"(?P<motor_0>[^ ]*), "
        r"(?P<motor_0_start>[^ ]*), "
        r"(?P<motor_0_end>[^ ]*), "
        r"(?P<motor_0_steps>[^ ]*), "
        r"(?P<motor_1>[^ ]*), "
        r"(?P<motor_1_start>[^ ]*), "
        r"(?P<motor_1_end>[^ ]*), "
        r"(?P<motor_1_steps>[^ ]*), "
        r"(?P<delay>[^ ]*)\s*"
        r".*"
        r"$"
    )

    _COMMAND_LINE_PATTERN_SPEC = (
        r"^(?P<command>[^ ]*)"
        r"(?:\s+(?P<motor_0>[^ ]*)"
        r"\s+(?P<motor_0_start>[^ ]*)"
        r"\s+(?P<motor_0_end>[^ ]*)"
        r"\s+(?P<motor_0_steps>[^ ]*)"
        r"\s+(?P<motor_1>[^ ]*)"
        r"\s+(?P<motor_1_start>[^ ]*)"
        r"\s+(?P<motor_1_end>[^ ]*)"
        r"\s+(?P<motor_1_steps>[^ ]*)"
        r"\s+(?P<delay>[^ ]*))"
        r".*"
        r"$"
    )

    cmd_rgx = re.compile(_COMMAND_LINE_PATTERN_BLISS)
    cmd_match = cmd_rgx.match(command)

    if cmd_match is None:
        cmd_rgx = re.compile(_COMMAND_LINE_PATTERN_SPEC)
        cmd_match = cmd_rgx.match(command)

        if cmd_match is None:
            raise ValueError('Failed to parse command line : "{0}".' "".format(command))

    cmd_dict = cmd_match.groupdict()
    cmd_dict.update(full=command)
    return cmd_dict


def make_xsocs_links(path_dset, path_out, scan_nums, detector=None, name_outh5=None):
    """
    Generates a set of .h5 files to be fed to XSOCS from a 3D-SXDM dataset.
    The files contain *links* to the original data, not the data itself.

    Parameters
    ----------
    path_dset : str
        Path to the .h5 dataset file, with links to individual scan .h5 files.
    path_out:
        Path to the folder where the XSOCS-compatible .h5 files will be saved.
    scan_nums : list, tuple or range of int
        Scan numbers to be processed.
    detector : str, default `None`
        The name of the detector used to collect the data.
    name_outh5 : str, default `None`
        Prefix of the XSOCS-compatible .h5 files generated. Defaults to the suffix of
        `path_dset`.

    Returns
    -------
        The path of the output master file
    """

    if not os.path.isdir(path_out):
        os.mkdir(path_out)

    pi_motor_names = {
        "pix_position": "adcY",
        "piy_position": "adcX",
        "piz_position": "adcZ",
    }

    # open the dataset file
    with h5py.File(path_dset, "r") as h5f:
        name_dset = os.path.basename(path_dset).split(".")[0]

        # using all scan numbers in file?
        if scan_nums is None:
            _logger.info(f"> Using all scan numbers in {name_dset}")
            scan_idxs = range(1, len(list(h5f.keys())) + 1)
            commands = [h5f[f"{s}.1/title"][()].decode() for s in scan_idxs]
            scan_nums = [
                f"{s}.1"
                for s, c in zip(scan_idxs, commands)
                if any([s in c for s in ("sxdm", "kmap")])
            ]
        else:
            try:
                scan_nums = [f"{int(x)}.1" for x in scan_nums]
            except ValueError:  # not a list of int
                scan_nums = scan_nums
            _logger.info(
                f"> Selecting scans {scan_nums[0]} --> {scan_nums[-1]} in {name_dset}"
            )
            commands = [h5f[f"{s}/title"][()].decode() for s in scan_nums]

        # name the output files
        if name_outh5 is None:
            name_outh5 = name_dset

        # detector?
        if detector is None:
            detector = get_detector_aliases(h5f, scan_nums[0])
            if len(detector) > 1:
                msg = f"Found multiple detector groups: {detector}, select"
                msg += "one by explicitly setting the `det` keyword argument"
                raise Exception(msg)
            else:
                detector = detector[0]
        else:
            detector = detector
        _logger.info(f"> Selecting detector {detector}")

        # generate output master file
        out_h5f_master = f"{path_out}/{name_outh5}_master.h5"
        with XsocsH5.XsocsH5MasterWriter(out_h5f_master, "w") as master:
            pass  # overwrite master file

        # load counters, positioners, and other params for each scan
        for scan_num, command in zip(scan_nums, commands):
            entry = h5f[scan_num]
            instr = entry["instrument/"]

            # get some metadata
            start_time = entry["start_time"][()].decode()
            direct_beam = [instr[f"{detector}/beam_center_{x}"] for x in ("y", "x")]
            det_distance = instr[f"{detector}/distance"]

            pix_sizes = [instr[f"{detector}/{m}_pixel_size"][()] for m in ("y", "x")]
            chan_per_deg = [
                np.tan(np.radians(1)) * det_distance / pxs for pxs in pix_sizes
            ]
            energy = xu.lam2en(instr["monochromator/WaveLength"][()] * 1e10)

            # get counters
            counters = [
                x for x in instr if instr[x].attrs.get("NX_class") == "NXdetector"
            ]

            # Why am I removing this? I forgot.
            # In the new bliss files it does not seem to be there,
            # hence the try / except
            try:
                counters.remove(f"{detector}_beam")
            except ValueError:
                pass

            # get piezo coordinates
            pi_positioners = [
                x for x in instr if instr[x].attrs.get("NX_class") == "NXpositioner"
            ]
            positioners = [x for x in instr["positioners"]]

            # more parameters
            entry_name = scan_num  # <-- ends up in output h5 fname
            command_params = parse_scan_command(command)

            out_h5f = f"{path_out}/{name_outh5}_{entry_name}.h5"

            # write links to individual XSOCS-compatible files
            with XsocsH5.XsocsH5Writer(out_h5f, "w") as xsocsh5f:  # overwrite
                """
                XsocsH5Writer methods
                --> make links to scan parameters
                """
                xsocsh5f.create_entry(entry_name)  # creates NX skeleton
                xsocsh5f.set_scan_params(
                    entry_name, **command_params
                )  # "scan" folder contents

                xsocsh5f.set_beam_energy(energy, entry_name)
                xsocsh5f.set_chan_per_deg(chan_per_deg, entry_name)
                xsocsh5f.set_direct_beam(direct_beam, entry_name)
                xsocsh5f.set_image_roi_offset([0, 0], entry_name)  # hardcoded for now

                """
                XsocsH5Base methods
                --> make links to data and counters
                """
                xsocsh5f._set_scalar_data(f"{entry_name}/title", command)
                xsocsh5f._set_scalar_data(f"{entry_name}/start_time", start_time)

                for c in counters:
                    if c == detector:
                        xsocsh5f.add_file_link(
                            f"{entry_name}/measurement/image/data",
                            path_dset,
                            f"{scan_num}/measurement/{c}",
                        )
                    else:
                        xsocsh5f.add_file_link(
                            f"{entry_name}/measurement/{c}",
                            path_dset,
                            f"{scan_num}/measurement/{c}",
                        )
                for p in positioners:
                    if p == "delta":
                        xsocsh5f.add_file_link(
                            f"{entry_name}/instrument/positioners/del",
                            path_dset,
                            f"{scan_num}/instrument/positioners/{p}",
                        )
                    else:
                        xsocsh5f.add_file_link(
                            f"{entry_name}/instrument/positioners/{p}",
                            path_dset,
                            f"{scan_num}/instrument/positioners/{p}",
                        )

                for pp in pi_positioners:
                    try:
                        new_c = pi_motor_names[pp]
                        xsocsh5f.add_file_link(
                            f"{entry_name}/measurement/{new_c}",
                            path_dset,
                            f"{scan_num}/instrument/{pp}/value",
                        )
                    except KeyError:
                        pass

                _imgnr = np.arange(entry[f"measurement/{detector}"].shape[0])
                xsocsh5f._set_array_data(f"{entry_name}/measurement/imgnr", _imgnr)

                xsocsh5f.add_file_link(
                    f"{entry_name}/technique", path_dset, f"{scan_num}/technique"
                )

            # write links to XSOCS master file
            with XsocsH5.XsocsH5MasterWriter(out_h5f_master, "a") as master:
                master.add_entry_file(entry_name, os.path.basename(out_h5f))

            # print
            _logger.info(f"> Linking # {scan_num}/{scan_nums[-1]}")

        _logger.info("> Done!")
        return out_h5f_master
