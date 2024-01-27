"""Concatenate multiple (partial) scans into a single HDF5 master file"""

import argparse
import logging
import os.path

from ..io.XsocsH5 import XsocsH5, XsocsH5MasterWriter


logger = logging.getLogger(__name__)


def concat(output, input_files):
    """Concatenate scans from multiple input files into a single master.

    :param str output: The filename of the new HDF5 master file to create
    :param List[str] input_files: List of filenames to concatenate.
       Files are taken in the order they are provided.
       There should be at least to files to concatenate.
    :raise ValueError:
       If output file already exists, or there is not enough files or
       an input file does not exist.
    """
    # Check input
    if len(input_files) < 2:
        raise ValueError("Not enough input files to concatenate")

    for filename in input_files:
        if not os.path.isfile(filename):
            raise ValueError("Invalid input file {0}".format(filename))

    # check output
    if os.path.exists(output):
        raise ValueError("Output file {0} already exists.".format(output))

    # Store list of (master filename, entries, entries filenames)
    input_entries = []
    for filename in input_files:
        with XsocsH5(filename, mode="r") as input_h5:
            entries = input_h5.entries()
            filenames = [input_h5.entry_filename(e) for e in entries]
        input_entries.append((filename, entries, filenames))

    # Write new master
    with XsocsH5MasterWriter(output, mode="w-") as master:
        for index, (_, entries, filenames) in enumerate(input_entries):
            prefix = str(index) + "_"
            for entry, filename in zip(entries, filenames):
                master.add_entry_file(entry, filename, master_entry=prefix + entry)


def main(argv):
    """Concatenate scans into one HDF5 file

    :param argv: Command line arguments
    :return: exit code
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        default=["concat_master.h5"],
        nargs=1,
        help="Name of the master HDF5 file to create",
    )
    parser.add_argument(
        "files",
        nargs=argparse.ONE_OR_MORE,
        help="Name of HDF5 files to concatenate (at least 2)",
    )

    options = parser.parse_args(argv[1:])
    output = options.output[0]
    try:
        concat(output, options.files)
    except ValueError as e:
        logger.error("; ".join(map(str, e.args)))
        return 1
    else:
        print("Save concatenated files into {0}".format(output))
        return 0
