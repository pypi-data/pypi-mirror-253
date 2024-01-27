from silx.gui import qt as Qt


class StyledLineEdit(Qt.QLineEdit):
    """
    Styled QLineEdit. Background color is set depending on the following
    states : read only, enabled.
    """

    _padding = 2

    def __init__(self, parent=None, nChar=None, readOnly=False):
        super(StyledLineEdit, self).__init__(parent)
        self.__nChar = nChar
        self.setAlignment(Qt.Qt.AlignLeft)
        self.setReadOnly(readOnly)
        self._updateStyleSheet()

    def setReadOnly(self, ro):
        super(StyledLineEdit, self).setReadOnly(ro)
        self._updateStyleSheet()

    def setEnabled(self, enabled):
        super(StyledLineEdit, self).setEnabled(enabled)
        self._updateStyleSheet()

    def setNChar(self, nChar):
        """
        Sets the number of characters to be displayed.
        :param nChar: None to reset to default.
        :return:
        """
        self.__nChar = nChar
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        """
        Sets the style sheet according to the state of the widget :
        - read only
        - enabled
        :return:
        """
        # Qt stylesheet system allow the use of keywords like
        # [readOnly="true"] or [enabled="true"] but this won't help here
        # since stylesheets are not applied when properties change
        # so we have to manually reset them.
        ro = self.isReadOnly()
        enabled = self.isEnabled()

        if not enabled:
            sheet = ""
        else:
            if ro:
                color = "lightGray"
            else:
                color = "white"
            sheet = """StyledLineEdit{{ background-color: {0}; }}
                    """.format(
                color
            )

        if self.__nChar is not None:
            # There are two stylesheet units "em" and "xm" that I tried,
            # but the results were not satisfactory.
            fm = self.fontMetrics()
            # text = 'M' * (self.__nChar + self._padding)
            # width = fm.width(text)
            width = fm.width("M") * self.__nChar
            height = fm.height()
            sheet += """StyledLineEdit{{ max-width: {0}px;
                                         min-width: {0}px;
                                         max-height: {1}px;
                                         min-height: {1}px;}}
                     """.format(
                width, height
            )
        self.setStyleSheet(sheet)

    def event(self, ev):
        # this has to be done so that the stylesheet is reapplied when the
        # "enabled" property changes
        # https://wiki.qt.io/Dynamic_Properties_and_Stylesheets
        if ev.type() == Qt.QEvent.EnabledChange:
            self.style().unpolish(self)
            self.style().polish(self)
        return super(StyledLineEdit, self).event(ev)


class FixedSizeLabel(Qt.QLabel):
    """
    Styled QLabel.
    """

    def __init__(self, parent=None, nChar=None):
        super(FixedSizeLabel, self).__init__(parent)
        self.__nChar = nChar
        self.setAlignment(Qt.Qt.AlignLeft)
        self.setFrameStyle(Qt.QFrame.Panel | Qt.QFrame.Sunken)
        self._updateStyleSheet()

    def setNChar(self, nChar):
        """
        Sets the number of characters to be displayed.
        :param nChar: None to reset to default.
        :return:
        """
        self.__nChar = nChar
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        """
        Sets the style sheet.
        :return:
        """

        if self.__nChar is not None:
            fm = self.fontMetrics()

            # see QLabel::indent doc for the reason behind the width('x')/2
            width = fm.width("M") * self.__nChar + (fm.width("x") / 2)
            self.setFixedWidth(int(width))
