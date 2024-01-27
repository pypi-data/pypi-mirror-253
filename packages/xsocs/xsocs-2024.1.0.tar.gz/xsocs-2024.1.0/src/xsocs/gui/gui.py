import logging
import sys

from silx.gui import qt as Qt

from .XsocsGui import XsocsGui
from .process.MergeWidget import MergeWidget
from .process.QSpaceWidget import QSpaceWidget


_logger = logging.getLogger(__name__)
_logger.info("Using Qt {0}".format(Qt.qVersion()))


def merge_window(*args, **kwargs):
    app = Qt.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    mw = MergeWidget(*args, **kwargs)
    mw.show()
    app.exec_()


def conversion_window(*args, **kwargs):
    app = Qt.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    mw = QSpaceWidget(*args, **kwargs)
    mw.show()
    app.exec_()


def xsocs_main(*args, **kwargs):
    app = Qt.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    mw = XsocsGui(*args, **kwargs)
    mw.show()
    app.exec_()
