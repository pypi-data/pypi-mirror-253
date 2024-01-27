import logging

from silx.gui import qt as Qt

from ...io.QSpaceH5 import QSpaceH5
from ...util import bin_centers_to_range_step, project

from ..widgets.Containers import GroupBox
from ..widgets.RoiAxisWidget import RoiAxisWidget
from ..widgets.Input import StyledLineEdit

from ...process.fit import PeakFitter, FitTypes
from ...io.FitH5 import BackgroundTypes


_logger = logging.getLogger(__name__)


class Roi3DSelectorWidget(GroupBox):
    """Widget displaying three RoiAxisWidgets, one for each axis.

    :param parent:
    """

    sigRoiChanged = Qt.Signal(object)
    """Signal emitted when one of the slider is moved.

       The new ranges are passed to the listener as
       a tuple of three SliderState instances, one for each axis.
    """

    def __init__(self, parent=None):
        super(Roi3DSelectorWidget, self).__init__("Roi", parent=parent)
        self.setCheckable(True)
        self.setChecked(False)
        layout = Qt.QVBoxLayout(self)

        self.__roiWidgets = (RoiAxisWidget(""), RoiAxisWidget(""), RoiAxisWidget(""))
        for widget in self.__roiWidgets:
            layout.addWidget(widget)
            layout.setAlignment(widget, Qt.Qt.AlignRight)
            widget.sigSliderMoved.connect(self.__slotSliderMoved)

    def __slotSliderMoved(self, _):
        """Slot called each time a slider moves."""
        self.sigRoiChanged.emit(
            [widget.getSliderState() for widget in self.roiAxisWidgets()]
        )

    def sliders(self):
        """Returns all ROI widgets sliders

        :rtype: List[RangeSlider]
        """
        return tuple(widget.slider() for widget in self.__roiWidgets)

    def roiAxisWidgets(self):
        """Returns all RoiAxisWidget

        :rtype: List[RoiAxisWidget]
        """
        return self.__roiWidgets


class FitWidget(Qt.QWidget):
    """Fit process widget.

    :param str qspaceFile:
    """

    sigFitTypeChanged = Qt.Signal(object)
    """Signal emitted when the fit type is changed"""

    sigProcessDone = Qt.Signal(object)
    """Signal emitted when a fit is done.

    Argument is the name of the file containing the results.
    """

    sigProcessStarted = Qt.Signal()
    """Signal emitted when a fit is started.

    Argument is the name of the file containing the results.
    """

    def __init__(self, qspaceFile, **kwargs):
        super(FitWidget, self).__init__(**kwargs)

        self.__qspaceH5 = QSpaceH5(qspaceFile)

        self.__outputFile = None

        layout = Qt.QFormLayout(self)

        self.__roiWidget = Roi3DSelectorWidget()

        layout.addRow(self.__roiWidget)

        self.__fileEdit = StyledLineEdit(readOnly=True)
        layout.addRow("File:", self.__fileEdit)

        self.__bgComboBox = Qt.QComboBox()
        self.__bgComboBox.setToolTip(
            "Select background subtraction mode:<br><br>"
            "<b>-</b>: No background<br>"
            "<b>Constant</b>: Shift data so that min is 0<br>"
            "<b>Snip</b>: Snip background estimation"
            "(Statistics-sensitive Non-linear Iterative Peak-clipping algorithm)"
        )
        self.__bgComboBox.addItem("-", BackgroundTypes.NONE)
        self.__bgComboBox.addItem("Constant", BackgroundTypes.CONSTANT)
        self.__bgComboBox.addItem("Snip", BackgroundTypes.SNIP)
        self.__bgComboBox.setCurrentIndex(0)
        layout.addRow("Background:", self.__bgComboBox)

        self.__fitTypeCb = Qt.QComboBox()
        self.__fitTypeCb.addItem("Gaussian", FitTypes.GAUSSIAN)
        self.__fitTypeCb.addItem("Centroid", FitTypes.CENTROID)
        self.__fitTypeCb.setCurrentIndex(0)
        self.__fitTypeCb.currentIndexChanged[str].connect(self.sigFitTypeChanged.emit)
        layout.addRow("Fit:", self.__fitTypeCb)

        self.__runButton = Qt.QPushButton("Run")
        self.__runButton.setEnabled(False)
        self.__runButton.clicked.connect(self.__slotRunClicked)
        self.__progBar = Qt.QProgressBar()
        layout.addRow(self.__runButton, self.__progBar)

        self.__statusLabel = Qt.QLabel("Ready")
        self.__statusLabel.setFrameStyle(Qt.QFrame.Panel | Qt.QFrame.Sunken)
        layout.addRow(self.__statusLabel)

        # Set sliders range and step
        with self.__qspaceH5:
            qDimensions = self.__qspaceH5.qspace_dimension_values

        for slider, binCenters in zip(self.roiWidget().sliders(), qDimensions):
            slider.setPositionCount(len(binCenters) + 1)
            min_, max_ = bin_centers_to_range_step(binCenters)[:2]
            slider.setRange(min_, max_)
            slider.setValues(min_, max_)

    def roiWidget(self):
        """Returns the Roi3DSelectorWidget instance.

        :rtype: Roi3DSelectorWidget
        """
        return self.__roiWidget

    def setQSpaceIndex(self, index):
        """Set slider backgrounds from given QSpace index.

        Selects the qspace cube at *index* in the qspace H5 file, and
        displays the corresponding profiles in the sliders.
        (profile = cube summed along the corresponding axis)

        :param int index: QSpace index
        """
        projections = project(self.__qspaceH5.qspace_slice(index))

        for profile, slider in zip(projections, self.roiWidget().sliders()):
            slider.setGroovePixmapFromProfile(profile, colormap="jet")

    def setOutputFile(self, outputFile):
        self.__outputFile = outputFile
        if outputFile is not None:
            self.__fileEdit.setText(outputFile)
        else:
            self.__fileEdit.clear()
        self.__runButton.setEnabled(outputFile is not None)

    def getFitName(self):
        """Returns the name of the selected fit, e.g., Gaussian, Centroid.

        :rtype: str
        """
        # TODO : real enum
        return self.__fitTypeCb.currentText()

    def __slotRunClicked(self):
        # TODO : put some safeguards
        self.__lock(True)

        self.__progBar.setValue(0)
        fitType = self.__fitTypeCb.itemData(self.__fitTypeCb.currentIndex())

        if self.roiWidget().isChecked():
            roiIndices = [
                slider.getPositions() for slider in self.roiWidget().sliders()
            ]

            # Check that roi ranges are not empty
            for min_, max_ in roiIndices:
                if min_ >= max_:
                    message = "QSpace ROI is void: cannot perform fit"
                    _logger.error(message)
                    Qt.QMessageBox.critical(self, "QSpace ROI Error", message)
                    self.__lock(False)
                    return
        else:
            roiIndices = None

        background = self.__bgComboBox.itemData(self.__bgComboBox.currentIndex())

        self.__fitter = PeakFitter(
            self.__qspaceH5.filename,
            fit_type=fitType,
            roi_indices=roiIndices,
            background=background,
        )
        self.__statusLabel.setText("Running...")

        self.sigProcessStarted.emit()
        try:
            for progress in self.__fitter.peak_fit_iterator():
                self.__progBar.setValue(int(100 * progress))
                Qt.QApplication.processEvents()

        except Exception as ex:
            # TODO : popup
            self.__statusLabel.setText("ERROR")
            _logger.error(ex)
            self.__lock(False)
            self.sigProcessDone.emit(None)
        else:
            self.__slotFitDone()

    def __lock(self, lock):
        enable = not lock
        self.roiWidget().setEnabled(enable)
        self.__bgComboBox.setEnabled(enable)
        self.__fitTypeCb.setEnabled(enable)
        self.__runButton.setEnabled(enable)

    def __slotFitDone(self):
        self.__lock(False)

        status = self.__fitter.status

        try:
            self.__fitter.results.to_fit_h5(self.__outputFile, mode="w")
        except Exception as ex:
            # TODO : popup
            _logger.error(ex)
            status = PeakFitter.ERROR

        if status == PeakFitter.DONE:
            self.__statusLabel.setText("Success")
            self.__progBar.setValue(100)
        elif status == PeakFitter.ERROR:
            # TODO : popup
            self.__statusLabel.setText("ERROR")
        elif status == PeakFitter.CANCELED:
            # TODO : popup
            self.__statusLabel.setText("Canceled")
        else:
            # TODO : popup
            self.__statusLabel.setText("?")

        self.__fitter = None

        self.sigProcessDone.emit(self.__outputFile)
