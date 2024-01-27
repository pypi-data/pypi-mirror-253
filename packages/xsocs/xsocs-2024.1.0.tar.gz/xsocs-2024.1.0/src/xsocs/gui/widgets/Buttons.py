from silx.gui import qt as Qt


class FixedSizePushButon(Qt.QPushButton):
    """
    It seems that by default QPushButtons minimum width is 75.
    This is a workaround.
    """

    _emptyWidth = 4
    _padding = 1

    def __init__(self, *args, **kwargs):
        super(FixedSizePushButon, self).__init__(*args, **kwargs)
        self.__nChar = None
        self._updateSize()

    def setText(self, text):
        """
        Reimplemented from QPushButton::setText.
        Calls _updateStyleSheet
        :param text:
        :return:
        """
        super(FixedSizePushButon, self).setText(text)
        self._updateSize()

    def _updateSize(self):
        """
        Sets the widget's size
        :return:
        """

        style = Qt.QApplication.style()
        border = 2 * (
            self._padding + style.pixelMetric(Qt.QStyle.PM_ButtonMargin, widget=self)
        )

        fm = self.fontMetrics()
        width = fm.width(self.text()) + border
        self.setFixedWidth(width)
