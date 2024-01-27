from silx.gui import qt as Qt
from .Input import FixedSizeLabel, StyledLineEdit


class PointWidget(Qt.QFrame):
    """
    Widget displaying 2 values (x, y).
    """

    def __init__(self, **kwargs):
        super(PointWidget, self).__init__(**kwargs)

        layout = Qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.__xEdit = xEdit = StyledLineEdit(nChar=6)
        xEdit.setReadOnly(True)
        self.__yEdit = yEdit = StyledLineEdit(nChar=6)
        yEdit.setReadOnly(True)

        xLabel = "x"
        yLabel = "y"

        layout.addWidget(FixedSizeLabel(xLabel, nChar=len(xLabel)))
        layout.addWidget(xEdit)
        layout.addWidget(FixedSizeLabel(yLabel, nChar=len(yLabel)))
        layout.addWidget(yEdit)

    def setPoint(self, x, y):
        """Sets the values to display.

        :param Union[float,None] x:
        :param Union[float,None] y:
        """
        self.__xEdit.setText("" if x is None else "{0:6g}".format(x))
        self.__yEdit.setText("" if y is None else "{0:6g}".format(y))
