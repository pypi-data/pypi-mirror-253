import numpy as np

from silx.gui import qt as Qt
from silx.gui.dialog.ImageFileDialog import ImageFileDialog

from ...io.XsocsH5 import XsocsH5

from ..widgets.AcqParamsWidget import AcqParamsWidget
from ..widgets.Containers import GroupBox, SubGroupBox
from ..widgets.Input import StyledLineEdit
from ...process.qspace import QSpaceConverter, qspace_conversion
from ...process.qspace import QSpaceCoordinates


_ETA_LOWER = "\u03B7"

_DEFAULT_IMG_BIN = [1, 1]

_DEFAULT_MEDFILT = [3, 3]


class ConversionParamsWidget(Qt.QWidget):
    """Widget for conversion parameters input

    - normalization counter
    - median filter
    - qspace dimensions
    """

    def __init__(
        self,
        medfiltDims=None,
        normalizers=None,
        beamEnergies=None,
        directBeam=None,
        channelsPerDegree=None,
        **kwargs
    ):
        super(ConversionParamsWidget, self).__init__(**kwargs)
        layout = Qt.QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # medfiltDims = np.array(medfiltDims, ndmin=1)

        self.__mask = None  # Currently selected mask array

        # ################
        # parameters
        # ################

        acqParamsGbx = SubGroupBox("Acq. Parameters")
        grpLayout = Qt.QVBoxLayout(acqParamsGbx)

        self.__acqParamWid = AcqParamsWidget()
        # Set default values with provided info
        self.__acqParamWid.setBeamEnergyFromList(beamEnergies)
        self.__acqParamWid.setBeamEnergyEnabled(len(set(beamEnergies)) == 1)
        self.__acqParamWid.direct_beam_v = directBeam[0]
        self.__acqParamWid.direct_beam_h = directBeam[1]
        self.__acqParamWid.chperdeg_v = channelsPerDegree[0]
        self.__acqParamWid.chperdeg_h = channelsPerDegree[1]
        grpLayout.addWidget(self.__acqParamWid)

        self.layout().addWidget(acqParamsGbx)

        # ===========
        # Image pre processing
        # ===========

        imageGbox = SubGroupBox("Image processing.")
        imgGboxLayout = Qt.QFormLayout(imageGbox)

        # Maxipix correction
        self.__maxipixCorrection = self.__createCheckBox("1. Maxipix correction")
        self.__maxipixCorrection.setToolTip(
            "Enable/Disable Maxipix detector module edges correction " "on input images"
        )

        imgGboxLayout.addRow(self.__maxipixCorrection)

        # Mask
        self.__imgMaskCBox = self.__createCheckBox("2. Mask")

        self.__maskFileLineEdit = StyledLineEdit()
        self.__maskFileLineEdit.setAlignment(Qt.Qt.AlignLeft)
        self.__maskFileLineEdit.setReadOnly(True)
        self.__imgMaskCBox.toggled.connect(self.__maskFileLineEdit.setEnabled)

        maskButton = Qt.QToolButton()
        style = Qt.QApplication.style()
        icon = style.standardIcon(Qt.QStyle.SP_DialogOpenButton)
        maskButton.setIcon(icon)
        maskButton.setEnabled(False)
        maskButton.clicked.connect(self.__maskButtonClicked)
        self.__imgMaskCBox.toggled.connect(maskButton.setEnabled)

        maskLayout = Qt.QHBoxLayout()
        maskLayout.addWidget(self.__maskFileLineEdit, 1)
        maskLayout.addWidget(maskButton)

        tooltip = (
            "Enable/Disable input images masking "
            "and select the mask image.<br>"
            "A value different from 0 in the mask image "
            "masks the corresponding pixel in input images."
        )
        self.__imgMaskCBox.setToolTip(tooltip)
        self.__maskFileLineEdit.setToolTip(tooltip)
        maskButton.setToolTip(tooltip)

        imgGboxLayout.addRow(self.__imgMaskCBox, maskLayout)

        # Normalization
        self.__imgNormCBox = self.__createCheckBox("3. Normalization")

        self.__normalizationComboBox = Qt.QComboBox()
        self.__normalizationComboBox.setEnabled(False)

        self.__imgNormCBox.toggled.connect(self.__normalizationComboBox.setEnabled)

        if normalizers is not None:
            self.__normalizationComboBox.addItems(normalizers)

        tooltip = (
            "Enable/Disable input images normalization<br>"
            "and select the data to use as normalizer"
        )
        self.__imgNormCBox.setToolTip(tooltip)
        self.__normalizationComboBox.setToolTip(tooltip)

        imgGboxLayout.addRow(self.__imgNormCBox, self.__normalizationComboBox)

        # Median filter
        self.__medfiltCBox = self.__createCheckBox("4. Median filter")

        inputBase = Qt.QWidget()
        inputBase.setEnabled(False)
        inputBase.setContentsMargins(0, 0, 0, 0)

        self.__medfiltCBox.toggled.connect(inputBase.setEnabled)

        self.__medfiltHEdit = StyledLineEdit(nChar=5)
        self.__medfiltHEdit.setValidator(Qt.QIntValidator(self.__medfiltHEdit))
        self.__medfiltHEdit.setAlignment(Qt.Qt.AlignRight)
        # self.__medfiltHEdit.setText(str(medfiltDims[0]))

        self.__medfiltVEdit = StyledLineEdit(nChar=5)
        self.__medfiltVEdit.setValidator(Qt.QIntValidator(self.__medfiltVEdit))
        self.__medfiltVEdit.setAlignment(Qt.Qt.AlignRight)
        # self.__medfiltVEdit.setText(str(medfiltDims[1]))

        medfiltLayout = Qt.QHBoxLayout(inputBase)
        medfiltLayout.setContentsMargins(0, 0, 0, 0)
        medfiltLayout.addWidget(Qt.QLabel("w="))
        medfiltLayout.addWidget(self.__medfiltHEdit)
        medfiltLayout.addWidget(Qt.QLabel("h="))
        medfiltLayout.addWidget(self.__medfiltVEdit)

        tooltip = (
            "Enable/Disable median filter on input images "
            "and set the window size: <b>W</b>idth and <b>H</b>eight"
        )
        self.__medfiltCBox.setToolTip(tooltip)
        inputBase.setToolTip(tooltip)

        imgGboxLayout.addRow(self.__medfiltCBox, inputBase)

        layout.addWidget(imageGbox)

        # ===========
        # QSpace histogram settings
        # ===========

        qspaceGbox = SubGroupBox("QSpace")
        qspaceLayout = Qt.QFormLayout(qspaceGbox)
        qspaceLayout.addRow(Qt.QLabel("Grid dimensions:"))

        self.__qDimEdits = {}  # Store line edits for each coordinate system
        self.__qDimWidgets = {}  # Store widget containing labels and line edit

        qDimLayout = Qt.QVBoxLayout()
        qDimLayout.setContentsMargins(0, 0, 0, 0)
        qDimLayout.setSpacing(0)
        qspaceLayout.addRow(qDimLayout)

        for coordinates in QSpaceCoordinates.ALLOWED:
            self.__qDimWidgets[coordinates] = Qt.QWidget()
            qspaceDimLayout = Qt.QHBoxLayout(self.__qDimWidgets[coordinates])

            self.__qDimEdits[coordinates] = (
                StyledLineEdit(nChar=5),
                StyledLineEdit(nChar=5),
                StyledLineEdit(nChar=5),
            )

            for axis, edit in zip(
                QSpaceCoordinates.axes_names(coordinates), self.__qDimEdits[coordinates]
            ):
                qspaceDimLayout.addWidget(Qt.QLabel(axis + ":"))
                qspaceDimLayout.addWidget(edit)
                qspaceDimLayout.addStretch(1)

            qDimLayout.addWidget(self.__qDimWidgets[coordinates])

        self.__coordinatesComboBox = Qt.QComboBox()
        self.__coordinatesComboBox.currentIndexChanged[int].connect(
            self.__coordinatesChanged
        )

        tooltip = ["Select the QSpace histogram coordinate system:<br>"]
        for coordinates in QSpaceCoordinates.ALLOWED:
            self.__coordinatesComboBox.addItem(coordinates.capitalize())
            tooltip.append(
                "- <b>%s</b>: %s, %s and %s axes"
                % (
                    (coordinates.capitalize(),)
                    + QSpaceCoordinates.axes_names(coordinates)
                )
            )
        self.__coordinatesComboBox.setToolTip("<br>".join(tooltip))

        qspaceLayout.addRow("Coordinates:", self.__coordinatesComboBox)

        layout.addWidget(qspaceGbox)

        self.setMedfiltDims(medfiltDims)

        # ===========
        # size constraints
        # ===========
        # self.setSizePolicy(Qt.QSizePolicy(Qt.QSizePolicy.Fixed,
        #                                   Qt.QSizePolicy.Fixed))

    def __createCheckBox(self, title):
        """Create and init a QCheckBox

        :param str title:
        :rtype: QCheckBox
        """
        qapp = Qt.QApplication.instance()
        style = qapp.style()
        size = style.pixelMetric(Qt.QStyle.PM_SmallIconSize)

        checkBox = Qt.QCheckBox(title)
        checkBox.toggled.connect(self.__checkboxToggled)
        checkBox.setIconSize(Qt.QSize(size, size))
        checkBox.setIcon(style.standardIcon(Qt.QStyle.SP_DialogCancelButton))
        checkBox.setChecked(False)
        return checkBox

    def __coordinatesChanged(self, index=None):
        """Handle change of QSpace coordinate change"""
        coordinates = self.getCoordinates()
        for coord, widget in self.__qDimWidgets.items():
            widget.setVisible(coordinates == coord)

    def __checkboxToggled(self, checked):
        """Update image processing check box icons"""
        style = Qt.QApplication.instance().style()
        if checked:
            icon = style.standardIcon(Qt.QStyle.SP_DialogApplyButton)
        else:
            icon = style.standardIcon(Qt.QStyle.SP_DialogCancelButton)

        checkBox = self.sender()
        checkBox.setIcon(icon)

    def __maskButtonClicked(self, checked):
        """On mask file dialog"""
        dialog = ImageFileDialog()
        if dialog.exec_():
            self.__maskFileLineEdit.setText(dialog.selectedUrl())
            self.__mask = dialog.selectedImage()

    def isMaxipixCorrectionEnabled(self):
        """Returns whether Maxipix correction is enabled or not.

        :rtype: bool
        """
        return self.__maxipixCorrection.isChecked()

    def getMask(self):
        """Returns the selected mask image or None if not set

        :rtype: Union[numpy.ndarray, None]
        """
        if not self.__imgMaskCBox.isChecked():
            return None
        else:
            return self.__mask

    def getNormalizer(self):
        """Returns the counter name to use for normalization if any.

        It returns None if normalization is disabled.

        :rtype: Union[str, None]
        """
        if not self.__imgNormCBox.isChecked():
            return None
        else:
            return self.__normalizationComboBox.currentText()

    def setNormalizer(self, normalizer):
        """Set the selected normalizer

        :param str normalizer:
        """
        hasNormalizer = normalizer is not None
        if hasNormalizer:
            index = self.__normalizationComboBox.findText(normalizer)
            if index >= 0:
                self.__normalizationComboBox.setCurrentIndex(index)
            else:
                raise ValueError("%s is not a valid normalizer" % normalizer)
        self.__imgNormCBox.setChecked(hasNormalizer)
        self.__normalizationComboBox.setEnabled(hasNormalizer)

    def getMedfiltDims(self):
        """Returns the median filter dimensions.

        :return:
            a 2 integers array, or None if the median filter is not enabled.
        """

        if not self.__medfiltCBox.isChecked():
            return None

        hMedfilt = self.__medfiltHEdit.text()
        if len(hMedfilt) == 0:
            hMedfilt = None
        else:
            hMedfilt = int(hMedfilt)

        vMedfilt = self.__medfiltVEdit.text()
        if len(vMedfilt) == 0:
            vMedfilt = None
        else:
            vMedfilt = int(vMedfilt)
        return [hMedfilt, vMedfilt]

    def setMedfiltDims(self, medfiltDims):
        """Sets the median filter dimensions.

        :param medfiltDims: a 2 integers array.
        """
        if medfiltDims is None:
            medfiltDims = (1, 1)
            medfiltDims = np.array(medfiltDims, ndmin=1)
        equal = np.array_equal(medfiltDims, [1, 1])
        self.__medfiltHEdit.setText(str(medfiltDims[0]))
        self.__medfiltVEdit.setText(str(medfiltDims[1]))
        self.__medfiltCBox.setChecked(not equal)

    def getQspaceDims(self, coordinates=None):
        """Returns the qspace dimensions, a 3 integers (> 1) array if set,
            or [None, None, None].

        :param Union[None,QSpaceCoordinates] coordinates:
            Either the coordinates system for which to get the value or None
            to get information for the current coordinates system
        :rtype: List[Union[int,None]]
        """
        if coordinates is None:
            coordinates = self.getCoordinates()

        sizes = []
        for edit in self.__qDimEdits[coordinates]:
            qsize = edit.text()
            qsize = None if len(qsize) == 0 else int(qsize)
            sizes.append(qsize)
        return sizes

    def setQSpaceDims(self, coordinates, qspaceDims):
        """Sets the qspace dimensions.

        :param QSpaceCoordinates coordinates:
        :param qspaceDims: A three integers array.
        """
        for edit, size in zip(self.__qDimEdits[coordinates], qspaceDims):
            edit.setText(str(int(size)))

    def setQSpaceRecommendedMaxDims(self, coordinates, qspaceDims):
        """Sets the recommended max qspace dimensions.

        :param QSpaceCoordinates coordinates:
        :param qspaceDims: A three integers array.
        """
        self.__qDimWidgets[coordinates].setToolTip(
            "Set the number of bins of the histogram for each dimension.\n"
            "Recommended maximum values are: [%d, %d, %d]" % tuple(qspaceDims)
        )

    def getBeamEnergy(self):
        """Returns beam energy in eV or None if no input"""
        if self.__acqParamWid.isBeamEnergyEnabled():
            return self.__acqParamWid.beam_energy
        else:
            return None

    def getDirectBeam(self):
        """Returns direct beam calibration position None if no input

        If one input is missing, it returns None.
        """
        directBeam = (
            self.__acqParamWid.direct_beam_v,
            self.__acqParamWid.direct_beam_h,
        )
        return None if None in directBeam else directBeam

    def getChannelsPerDegree(self):
        """Returns channels per degree calibration position None if no input

        If one input is missing, it returns None.
        """
        channelsPerDegree = (
            self.__acqParamWid.chperdeg_v,
            self.__acqParamWid.chperdeg_h,
        )
        return None if None in channelsPerDegree else channelsPerDegree

    def getCoordinates(self):
        """Returns the coordinates system to use.

        :rtype: QSpaceCoordinates
        """
        return self.__coordinatesComboBox.currentText().lower()


class QSpaceWidget(Qt.QDialog):
    sigProcessDone = Qt.Signal()
    """Signal emitted when the processing is done,
    but before closing the progress dialog.
    """

    (
        StatusUnknown,
        StatusInit,
        StatusRunning,
        StatusCompleted,
        StatusAborted,
        StatusCanceled,
    ) = StatusList = range(6)

    def __init__(
        self,
        xsocH5File,
        outQSpaceH5,
        qspaceDims=None,
        medfiltDims=None,
        roi=None,
        entries=None,
        shiftH5File=None,
        normalizer=None,
        **kwargs
    ):
        """
        Widgets displaying informations about data to be converted to QSpace,
            and allowing the user to input some parameters.

        :param xsocH5File: name of the input XsocsH5 file.
        :param outQSpaceH5: name of the output hdf5 file
        :param qspaceDims: dimensions of the qspace volume
        :param medfiltDims: dimensions of the kernel used when applying a
            a median filter to the images (after the mask, if any).
            Set to None or (1, 1) to disable the median filter.
        :param roi: Roi in sample coordinates (xMin, xMax, yMin, yMax)
        :param entries: a list of entry names to convert to qspace. If None,
            all entries found in the xsocsH5File will be used.
        :param shiftH5File: name of a ShiftH5 file to use.
        :param Union[str, None] normalizer:
            Name of the dataset in measurement to use for normalization.
        :param kwargs:
        """
        super(QSpaceWidget, self).__init__(**kwargs)

        self.__status = QSpaceWidget.StatusInit

        xsocsH5 = XsocsH5(xsocH5File)

        # checking entries
        if entries is None:
            entries = xsocsH5.entries()
        elif len(entries) == 0:
            raise ValueError("At least one entry must be selected.")
        else:
            diff = set(entries) - set(xsocsH5.entries())
            if len(diff) > 0:
                raise ValueError(
                    "The following entries were not found in "
                    "the input file :\n - {0}"
                    "".format("\n -".join(diff))
                )

        self.__converter = QSpaceConverter(
            xsocH5File,
            output_f=outQSpaceH5,
            qspace_dims=qspaceDims,
            medfilt_dims=medfiltDims,
            roi=roi,
            entries=entries,
            shiftH5_f=shiftH5File,
        )
        self.__converter.normalizer = normalizer

        self.__params = {"roi": roi, "xsocsH5_f": xsocH5File, "qspaceH5_f": outQSpaceH5}

        topLayout = Qt.QGridLayout(self)

        # ATTENTION : this is done to allow the stretch
        # of the QTableWidget containing the scans info
        topLayout.setColumnStretch(1, 1)

        # ################
        # input QGroupBox
        # ################

        inputGbx = GroupBox("Input")
        inputGbx.setToolTip("HDF5 'master' data file to process")
        layout = Qt.QHBoxLayout(inputGbx)
        topLayout.addWidget(inputGbx, 0, 0, 1, 2)

        # data HDF5 file input
        lab = Qt.QLabel("XsocsH5 file :")
        xsocsFileEdit = StyledLineEdit(nChar=50, readOnly=True)
        xsocsFileEdit.setText(xsocH5File)
        layout.addWidget(lab, stretch=0, alignment=Qt.Qt.AlignLeft)
        layout.addWidget(xsocsFileEdit, stretch=0, alignment=Qt.Qt.AlignLeft)
        layout.addStretch()

        # ################
        # Scans
        # ################
        scansGbx = GroupBox("Scans")
        topLayout.addWidget(scansGbx, 1, 1, 2, 1)
        topLayout.setRowStretch(2, 1000)

        grpLayout = Qt.QVBoxLayout(scansGbx)
        infoLayout = Qt.QGridLayout()
        grpLayout.addLayout(infoLayout)
        #

        line = 0

        style = Qt.QApplication.instance().style()
        shiftLayout = Qt.QHBoxLayout()
        if shiftH5File is not None:
            shiftText = "Shift applied."
            icon = Qt.QStyle.SP_MessageBoxWarning
        else:
            shiftText = "No shift applied."
            icon = Qt.QStyle.SP_MessageBoxInformation
        shiftLabel = Qt.QLabel(shiftText)
        size = style.pixelMetric(Qt.QStyle.PM_ButtonIconSize)
        shiftIcon = Qt.QLabel()
        icon = style.standardIcon(icon)
        shiftIcon.setPixmap(icon.pixmap(size))
        shiftLayout.addWidget(shiftIcon)
        shiftLayout.addWidget(shiftLabel)
        infoLayout.addLayout(shiftLayout, line, 0)

        line = 1
        label = Qt.QLabel("# Roi :")
        self.__roiXMinEdit = StyledLineEdit(nChar=5, readOnly=True)
        self.__roiXMaxEdit = StyledLineEdit(nChar=5, readOnly=True)
        self.__roiYMinEdit = StyledLineEdit(nChar=5, readOnly=True)
        self.__roiYMaxEdit = StyledLineEdit(nChar=5, readOnly=True)
        roiLayout = Qt.QHBoxLayout()
        roiLayout.addWidget(self.__roiXMinEdit)
        roiLayout.addWidget(self.__roiXMaxEdit)
        roiLayout.addWidget(self.__roiYMinEdit)
        roiLayout.addWidget(self.__roiYMaxEdit)
        infoLayout.addWidget(label, line, 0)
        infoLayout.addLayout(roiLayout, line, 1, alignment=Qt.Qt.AlignLeft)

        line += 1
        label = Qt.QLabel("# points :")
        self.__nImgLabel = StyledLineEdit(nChar=16, readOnly=True)
        nImgLayout = Qt.QHBoxLayout()
        infoLayout.addWidget(label, line, 0)
        infoLayout.addLayout(nImgLayout, line, 1, alignment=Qt.Qt.AlignLeft)
        nImgLayout.addWidget(self.__nImgLabel)
        nImgLayout.addWidget(Qt.QLabel(" (roi / total)"))

        line += 1
        label = Qt.QLabel("# {0} :".format(_ETA_LOWER))
        self.__nAnglesLabel = StyledLineEdit(nChar=5, readOnly=True)
        infoLayout.addWidget(label, line, 0)
        infoLayout.addWidget(self.__nAnglesLabel, line, 1, alignment=Qt.Qt.AlignLeft)
        infoLayout.setColumnStretch(2, 1)

        self.__scansTable = Qt.QTableWidget(0, 4)
        grpLayout.addWidget(self.__scansTable, alignment=Qt.Qt.AlignLeft)

        # ################
        # conversion params
        # ################

        convGbx = GroupBox("Conversion parameters")
        grpLayout = Qt.QVBoxLayout(convGbx)
        topLayout.addWidget(convGbx, 1, 0, alignment=Qt.Qt.AlignTop)

        if entries:  # Get default config from first entry
            directBeam = xsocsH5.direct_beam(entries[0])
            channelsPerDegree = xsocsH5.chan_per_deg(entries[0])
        else:  # This should not happen
            directBeam = "", ""
            channelsPerDegree = "", ""

        beamEnergies = [xsocsH5.beam_energy(entry) for entry in entries]

        self.__paramsWid = ConversionParamsWidget(
            medfiltDims=self.__converter.medfilt_dims,
            normalizers=xsocsH5.normalizers(),
            beamEnergies=beamEnergies,
            directBeam=directBeam,
            channelsPerDegree=channelsPerDegree,
        )
        self.__paramsWid.setNormalizer(normalizer)
        grpLayout.addWidget(self.__paramsWid)

        # ################
        # output
        # ################

        outputGbx = GroupBox("Output")
        outputGbx.setToolTip("HDF5 file where QSpace will be saved")
        layout = Qt.QHBoxLayout(outputGbx)
        topLayout.addWidget(outputGbx, 3, 0, 1, 2)
        lab = Qt.QLabel("Output :")
        outputFileEdit = StyledLineEdit(nChar=50, readOnly=True)
        outputFileEdit.setText(outQSpaceH5)
        layout.addWidget(lab, stretch=0, alignment=Qt.Qt.AlignLeft)
        layout.addWidget(outputFileEdit, stretch=0, alignment=Qt.Qt.AlignLeft)
        layout.addStretch()

        # ################
        # buttons
        # ################

        self.__convertBn = Qt.QPushButton("Convert")
        cancelBn = Qt.QPushButton("Cancel")
        hLayout = Qt.QHBoxLayout()
        topLayout.addLayout(hLayout, 4, 0, 1, 2, Qt.Qt.AlignHCenter | Qt.Qt.AlignTop)
        hLayout.addWidget(self.__convertBn)
        hLayout.addWidget(cancelBn)

        # #################
        # setting initial state
        # #################

        cancelBn.clicked.connect(self.close)
        self.__convertBn.clicked.connect(self.__slotConvertBnClicked)

        self.__fillScansInfo()

        # Set default qspace bin size
        if entries:
            # Get angles from all entries
            phi = []
            eta = []
            nu = []
            delta = []
            for entry in entries:
                phi.append(xsocsH5.positioner(entry, "phi"))
                eta.append(xsocsH5.positioner(entry, "eta"))
                nu.append(xsocsH5.positioner(entry, "nu"))
                delta.append(xsocsH5.positioner(entry, "del"))

            entry = entries[0]  # Get default config from first entry

            for coordinates in QSpaceCoordinates.ALLOWED:
                # Compute Qspace conversion
                q_array = qspace_conversion(
                    img_size=xsocsH5.image_size(entry),
                    center_chan=xsocsH5.direct_beam(entry),
                    chan_per_deg=xsocsH5.chan_per_deg(entry),
                    beam_energy=beamEnergies,
                    phi=phi,
                    eta=eta,
                    nu=nu,
                    delta=delta,
                    coordinates=coordinates,
                )

                # Estimate bin numbers based on smallest distance between q vectors
                maxbins = []
                for dim in (q_array[..., 0], q_array[..., 1], q_array[..., 2]):
                    maxbin = np.inf
                    for j in range(dim.ndim):
                        step = abs(np.diff(dim, axis=j)).max()
                        bins = (abs(dim).max() - abs(dim).min()) / step
                        maxbin = min(maxbin, bins)
                    maxbins.append(int(maxbin) + 1)

                # Set default number of bins to at most 100
                self.__paramsWid.setQSpaceDims(
                    coordinates, [min(maxbin, 100) for maxbin in maxbins]
                )
                self.__paramsWid.setQSpaceRecommendedMaxDims(coordinates, maxbins)

        else:  # Set to 0 by default
            for coordinates in QSpaceCoordinates.ALLOWED:
                self.__paramsWid.setQSpaceDims(coordinates, [0, 0, 0])

    def __slotConvertBnClicked(self):
        """Slot called when the convert button is clicked.

        Does some checks then starts the conversion if all is OK.
        """
        converter = self.__converter
        if converter is None:
            # shouldn't be here
            raise RuntimeError("Converter not found.")
        elif converter.is_running():
            # this part shouldn't even be called, just putting this
            # in case someone decides to modify the code to enable the
            # convert_bn even tho conditions are not met.
            Qt.QMessageBox.critical(
                self, "Error", "A conversion is already in progress!"
            )
            return

        output_file = converter.output_f

        if len(output_file) == 0:
            Qt.QMessageBox.critical(self, "Error", "Output file field is mandatory.")
            return

        normalizer = self.__paramsWid.getNormalizer()
        medfiltDims = self.__paramsWid.getMedfiltDims()
        qspaceDims = self.__paramsWid.getQspaceDims()
        beamEnergy = self.__paramsWid.getBeamEnergy()
        directBeam = self.__paramsWid.getDirectBeam()
        channelsPerDegree = self.__paramsWid.getChannelsPerDegree()
        mask = self.__paramsWid.getMask()
        maxipixCorrection = self.__paramsWid.isMaxipixCorrectionEnabled()
        coordinates = self.__paramsWid.getCoordinates()

        try:
            converter.normalizer = normalizer
            converter.medfilt_dims = medfiltDims
            converter.qspace_dims = qspaceDims
            converter.beam_energy = beamEnergy
            converter.direct_beam = directBeam
            converter.channels_per_degree = channelsPerDegree
            converter.mask = mask
            converter.maxipix_correction = maxipixCorrection
            converter.coordinates = coordinates
        except ValueError as ex:
            Qt.QMessageBox.critical(self, "Error", str(ex))
            return

        errors = converter.check_parameters()
        if errors:
            msg = "Invalid parameters.\n{0}".format("\n".join(errors))
            Qt.QMessageBox.critical(self, "Error", msg)
            return

        if len(converter.check_overwrite()):
            ans = Qt.QMessageBox.warning(
                self,
                "Overwrite?",
                ("The output file already exists." "\nDo you want to overwrite it?"),
                buttons=Qt.QMessageBox.Yes | Qt.QMessageBox.No,
            )
            if ans == Qt.QMessageBox.No:
                return

        self.__converter = converter
        procDialog = _ConversionProcessDialog(converter, parent=self)
        procDialog.sigProcessDone.connect(self.sigProcessDone.emit)
        procDialog.accepted.connect(self.__slotConvertDone)
        procDialog.rejected.connect(self.__slotConvertDone)
        self._setStatus(self.StatusRunning)
        rc = procDialog.exec_()

        if rc == Qt.QDialog.Accepted:
            self.__slotConvertDone()
        procDialog.deleteLater()

    def __slotConvertDone(self):
        """Method called when the conversion has been completed successfully."""
        converter = self.__converter
        if not converter:
            return

        self.__qspaceH5 = None
        status = converter.status

        if status == QSpaceConverter.DONE:
            self.__qspaceH5 = converter.results
            self._setStatus(self.StatusCompleted)
            self.hide()
        elif status == QSpaceConverter.CANCELED:
            self._setStatus(self.StatusAborted)
        else:
            self._setStatus(self.StatusUnknown)

    qspaceH5 = property(lambda self: self.__qspaceH5)
    """Written file (set when the conversion was successful, None otherwise."""

    status = property(lambda self: self.__status)
    """Status of the widget."""

    def _setStatus(self, status):
        """Sets the status of the widget.

        :param status:
        """
        if status not in QSpaceWidget.StatusList:
            raise ValueError("Unknown status value : {0}." "".format(status))
        self.__status = status

    def __fillScansInfo(self):
        """Fills the QTableWidget with info found in the input file"""
        if self.__converter is None:
            return

        scans = self.__converter.scans

        self.__scansTable.verticalHeader().hide()
        self.__scansTable.setHorizontalHeaderLabels(
            ["scan", "eta (°)", "phi (°)", "energy (eV)"]
        )

        self.__scansTable.setSelectionMode(self.__scansTable.NoSelection)

        self.__scansTable.setRowCount(len(scans))

        with XsocsH5(self.__converter.xsocsH5_f, mode="r") as h5f:
            for row, scan in enumerate(scans):
                eta = h5f.positioner(scan, "eta")
                phi = h5f.positioner(scan, "phi")
                beam_energy = h5f.beam_energy(entry=scan)

                for column, value in enumerate(
                    (scan, "%g" % eta, "%g" % phi, "%g" % beam_energy)
                ):
                    item = Qt.QTableWidgetItem(value)
                    self.__scansTable.setItem(row, column, item)

        self.__scansTable.resizeColumnsToContents()
        width = (
            sum(
                [
                    self.__scansTable.columnWidth(i)
                    for i in range(self.__scansTable.columnCount())
                ]
            )
            + self.__scansTable.verticalHeader().width()
            + 20
        )

        # TODO : the size is wrong when the
        # verticalScrollBar is not displayed yet
        # scans_table.verticalScrollBar().width())
        size = self.__scansTable.minimumSize()
        size.setWidth(width)
        self.__scansTable.setMinimumSize(size)

        # TODO : warning if the ROI is empty (too small to contain images)
        params = self.__converter.scan_params(scans[0])
        roi = self.__converter.roi
        if roi is None:
            xMin = xMax = yMin = yMax = "ns"
        else:
            xMin, xMax, yMin, yMax = roi

        self.__roiXMinEdit.setText(str(xMin))
        self.__roiXMaxEdit.setText(str(xMax))
        self.__roiYMinEdit.setText(str(yMin))
        self.__roiYMaxEdit.setText(str(yMax))

        indices = self.__converter.sample_indices
        nImgTxt = "{0} / {1}".format(len(indices), params["n_images"])
        self.__nImgLabel.setText(nImgTxt)

        nEntries = len(XsocsH5(self.__params["xsocsH5_f"]).entries())
        self.__nAnglesLabel.setText("{0} / {1}".format(len(scans), nEntries))


class _ConversionProcessDialog(Qt.QDialog):
    # Used internally for executing code in main thread
    __sigConvertDone = Qt.Signal()

    sigProcessDone = Qt.Signal()
    """Signal emitted once the processing is done"""

    def __init__(self, converter, parent=None, **kwargs):
        """
        Simple widget displaying a progress bar and a info label during the
            conversion process.

        :param converter:
        :param parent:
        :param kwargs:
        """
        super(_ConversionProcessDialog, self).__init__(parent)
        layout = Qt.QVBoxLayout(self)

        progress_bar = Qt.QProgressBar()
        layout.addWidget(progress_bar)
        status_lab = Qt.QLabel('<font color="blue">Conversion ' "in progress</font>")
        status_lab.setFrameStyle(Qt.QFrame.Panel | Qt.QFrame.Sunken)
        layout.addWidget(status_lab)

        bn_box = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Abort)
        layout.addWidget(bn_box)
        bn_box.accepted.connect(self.accept)
        bn_box.rejected.connect(self.__onAbort)

        self.__sigConvertDone.connect(self.__convertDone)

        self.__bn_box = bn_box
        self.__progress_bar = progress_bar
        self.__status_lab = status_lab
        self.__converter = converter
        self.__aborted = False

        self.__qtimer = Qt.QTimer()
        self.__qtimer.timeout.connect(self.__onProgress)

        converter.convert(
            blocking=False,
            overwrite=True,
            callback=self.__sigConvertDone.emit,
            **kwargs
        )

        self.__qtimer.start(1000)

    def __onAbort(self):
        """Slot called when the abort button is clicked."""
        self.__status_lab.setText('<font color="orange">Cancelling...</font>')
        self.__bn_box.button(Qt.QDialogButtonBox.Abort).setEnabled(False)
        self.__converter.abort(wait=False)
        self.__aborted = True

    def __onProgress(self):
        """Slot called when the progress timer timeouts."""
        progress = self.__converter.progress()
        self.__progress_bar.setValue(progress)

    def __convertDone(self):
        """
        Callback called when the conversion is done (whether its successful or
        not).
        """
        self.__qtimer.stop()
        self.__qtimer = None
        self.__onProgress()

        abortBn = self.__bn_box.button(Qt.QDialogButtonBox.Abort)

        converter = self.__converter

        if converter.status == QSpaceConverter.CANCELED:
            self.__bn_box.rejected.disconnect(self.__onAbort)
            self.__status_lab.setText(
                '<font color="red">Conversion ' "cancelled.</font>"
            )
            abortBn.setText("Close")
            self.__bn_box.rejected.connect(self.reject)
            abortBn.setEnabled(True)
        elif converter.status == QSpaceConverter.ERROR:
            self.__bn_box.removeButton(abortBn)
            okBn = self.__bn_box.addButton(Qt.QDialogButtonBox.Ok)
            self.__status_lab.setText(
                '<font color="red">Error : {0}.</font>' "".format(converter.status_msg)
            )
            okBn.setText("Close")
        else:
            self.__bn_box.removeButton(abortBn)
            okBn = self.__bn_box.addButton(Qt.QDialogButtonBox.Ok)
            self.__status_lab.setText('<font color="green">Conversion ' "done.</font>")
            okBn.setText("Close")

            self.sigProcessDone.emit()

    status = property(lambda self: 0 if self.__aborted else 1)
    """Status of the process."""
