from silx.gui import qt as Qt

from .Input import StyledLineEdit

_MU_LOWER = "\u03BC"
_PHI_LOWER = "\u03C6"
_ETA_LOWER = "\u03B7"


class _DblValidator(Qt.QDoubleValidator):
    """QDoubleValidator accepting empty text"""

    def validate(self, text, pos):
        if len(text) == 0:
            return Qt.QValidator.Acceptable, text, pos
        return super(_DblValidator, self).validate(text, pos)


def _dblLineEditWidget(width, read_only):
    """Returns a LineEdit of given width

    :param int width: Widget's width in pixels
    :param bool read_only: Set read only or read/write widget
    :rtype: StyledLineEdit
    """
    wid = StyledLineEdit(nChar=width, readOnly=read_only)
    wid.setValidator(_DblValidator())
    return wid


class AcqParamsWidget(Qt.QWidget):
    def __init__(self, read_only=False, **kwargs):
        super(AcqParamsWidget, self).__init__(**kwargs)
        layout = Qt.QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # ===========
        # beam energy
        # ===========
        row = 0
        self.__energyWidget = Qt.QWidget(self)
        h_layout = Qt.QHBoxLayout(self.__energyWidget)
        self.__beam_nrg_edit = _dblLineEditWidget(12, read_only)
        h_layout.addWidget(self.__beam_nrg_edit)
        h_layout.addWidget(Qt.QLabel("<b>eV</b>"))

        label = Qt.QLabel("Beam energy:")

        layout.addWidget(label, row, 0)
        layout.addWidget(
            self.__energyWidget, row, 1, alignment=Qt.Qt.AlignLeft | Qt.Qt.AlignTop
        )

        tooltip = "Incoming beam energy"
        label.setToolTip(tooltip)
        self.__energyWidget.setToolTip(tooltip)

        # ===

        row += 1
        h_line = Qt.QFrame()
        h_line.setFrameShape(Qt.QFrame.HLine)
        h_line.setFrameShadow(Qt.QFrame.Sunken)
        layout.addWidget(h_line, row, 0, 1, 2)

        # ===========
        # direct beam
        # ===========

        row += 1
        widget = Qt.QWidget(self)
        h_layout = Qt.QHBoxLayout(widget)
        layout.addWidget(widget, row, 1, alignment=Qt.Qt.AlignLeft | Qt.Qt.AlignTop)
        self.__dir_beam_v_edit = _dblLineEditWidget(6, read_only)
        h_layout.addWidget(Qt.QLabel("v="))
        h_layout.addWidget(self.__dir_beam_v_edit)
        self.__dir_beam_h_edit = _dblLineEditWidget(6, read_only)
        h_layout.addWidget(Qt.QLabel(" h="))
        h_layout.addWidget(self.__dir_beam_h_edit)
        h_layout.addWidget(Qt.QLabel("<b>px</b>"))
        label = Qt.QLabel("Direct beam:")
        layout.addWidget(label, row, 0)

        tooltip = (
            "Set direct beam <b>V</b>ertical and <b>H</b>orizontal "
            "calibration position on the detector"
        )
        widget.setToolTip(tooltip)
        label.setToolTip(tooltip)

        # ===

        row += 1
        h_line = Qt.QFrame()
        h_line.setFrameShape(Qt.QFrame.HLine)
        h_line.setFrameShadow(Qt.QFrame.Sunken)
        layout.addWidget(h_line, row, 0, 1, 3)

        # ===========
        # chan per degree
        # ===========

        row += 1
        widget = Qt.QWidget(self)
        h_layout = Qt.QHBoxLayout(widget)
        layout.addWidget(widget, row, 1, alignment=Qt.Qt.AlignLeft | Qt.Qt.AlignTop)
        self.__chpdeg_v_edit = _dblLineEditWidget(6, read_only)
        h_layout.addWidget(Qt.QLabel("v="))
        h_layout.addWidget(self.__chpdeg_v_edit)
        self.__chpdeg_h_edit = _dblLineEditWidget(6, read_only)
        h_layout.addWidget(Qt.QLabel(" h="))
        h_layout.addWidget(self.__chpdeg_h_edit)
        h_layout.addWidget(Qt.QLabel("<b>px</b>"))
        label = Qt.QLabel("Chan. per deg.:")

        layout.addWidget(label, row, 0)

        tooltip = (
            "Set <b>V</b>ertical and <b>H</b>orizontal detector "
            "pixels per degree calibration information"
        )
        widget.setToolTip(tooltip)
        label.setToolTip(tooltip)

        # ===

        row += 1
        h_line = Qt.QFrame()
        h_line.setFrameShape(Qt.QFrame.HLine)
        h_line.setFrameShadow(Qt.QFrame.Sunken)
        layout.addWidget(h_line, row, 0, 1, 3)

        # ===========
        # size constraints
        # ===========
        self.setSizePolicy(Qt.QSizePolicy(Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Fixed))

    def clear(self):
        self.__beam_nrg_edit.clear()
        self.__dir_beam_h_edit.clear()
        self.__dir_beam_v_edit.clear()
        self.__chpdeg_h_edit.clear()
        self.__chpdeg_v_edit.clear()

    def isBeamEnergyEnabled(self):
        """Returns whether beam energy is enabled on not.

        :rtype: bool
        """
        return self.__energyWidget.isEnabled()

    def setBeamEnergyEnabled(self, enabled):
        """Enable/disable beam energy widget

        :param bool enabled:
        """
        self.__energyWidget.setEnabled(enabled)

    @property
    def beam_energy(self):
        text = self.__beam_nrg_edit.text()
        if len(text) == 0:
            return None
        return float(text)

    @beam_energy.setter
    def beam_energy(self, beam_energy):
        self.__beam_nrg_edit.setText(str(beam_energy))

    def setBeamEnergyFromList(self, energies):
        """Set the beam energy from a list of energies

        :param List[float] energies:
        """
        nbEnergies = len(set(energies))
        if nbEnergies == 0:
            text = ""
        elif nbEnergies == 1:  # All energies are the same
            text = "%g" % energies[0]
        else:
            text = "[%g;%g]" % (min(energies), max(energies))
        self.__beam_nrg_edit.setText(text)

    @property
    def direct_beam_h(self):
        text = self.__dir_beam_h_edit.text()
        if len(text) == 0:
            return None
        return float(text)

    @direct_beam_h.setter
    def direct_beam_h(self, direct_beam_h):
        self.__dir_beam_h_edit.setText(str(direct_beam_h))

    @property
    def direct_beam_v(self):
        text = self.__dir_beam_v_edit.text()
        if len(text) == 0:
            return None
        return float(text)

    @direct_beam_v.setter
    def direct_beam_v(self, direct_beam_v):
        self.__dir_beam_v_edit.setText(str(direct_beam_v))

    @property
    def chperdeg_h(self):
        text = self.__chpdeg_h_edit.text()
        if len(text) == 0:
            return None
        return float(text)

    @chperdeg_h.setter
    def chperdeg_h(self, chperdeg_h):
        self.__chpdeg_h_edit.setText(str(chperdeg_h))

    @property
    def chperdeg_v(self):
        text = self.__chpdeg_v_edit.text()
        if len(text) == 0:
            return None
        return float(text)

    @chperdeg_v.setter
    def chperdeg_v(self, chperdeg_v):
        self.__chpdeg_v_edit.setText(str(chperdeg_v))
