"""xsocs main graphical user interface"""

import argparse
from multiprocessing import cpu_count

from .. import config


def main(argv):
    """Starts main graphical user interface

    :param argv: Command line arguments
    :return: exit code
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "project_file", nargs=argparse.OPTIONAL, help="xsocs project file to open"
    )
    parser.add_argument(
        "--numcores",
        nargs="?",
        type=int,
        default=cpu_count(),
        help="Max number of processes to use (default: %d)" % cpu_count(),
    )
    parser.add_argument(
        "--no-3d", action="store_true", help="Do not use OpenGL-based 3D visualization"
    )

    options = parser.parse_args(argv[1:])

    if options.numcores <= 0:
        raise ValueError("Number of processes to use must be strictly positive")
    config.DEFAULT_PROCESS_NUMBER = options.numcores

    config.USE_OPENGL = not options.no_3d

    from ..gui import xsocs_main  # noqa

    if options.project_file:
        xsocs_main(projectH5File=options.project_file)
    else:
        xsocs_main()

    return 1
