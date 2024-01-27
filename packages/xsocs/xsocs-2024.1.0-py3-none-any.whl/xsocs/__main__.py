"""xsocs launcher"""

import logging
import sys

from silx.utils.launcher import Launcher
from xsocs import version

logging.basicConfig()
logging.getLogger("xsocs").setLevel(logging.INFO)


def main(argv=None):
    """Main entry point of xsocs"""
    if argv is None:
        argv = sys.argv

    launcher = Launcher(prog="xsocs", version=version)
    launcher.add_command(
        "gui",
        module_name="xsocs._app.gui",
        description="Open xsocs main Graphical User Interface",
    )
    launcher.add_command(
        "concat",
        module_name="xsocs._app.concat",
        description="Concatenate multiple scans into one HDF5 master file",
    )

    # Start the GUI by default
    argv = list(argv)
    if len(argv) <= 1:
        argv.append("gui")

    sys.exit(launcher.execute(argv))


if __name__ == "__main__":
    main()
