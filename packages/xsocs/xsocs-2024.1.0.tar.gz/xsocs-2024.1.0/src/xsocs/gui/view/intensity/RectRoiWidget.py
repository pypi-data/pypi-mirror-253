from collections import namedtuple

from silx.gui import qt as Qt

from ...widgets.Containers import GroupBox
from ...widgets.Input import StyledLineEdit

from ...silx_imports.ImageRois import ImageRoiManager


IntensityViewEvent = namedtuple("IntensityViewEvent", ["roi", "entries"])


# TODO : namedtuple for the roi values


class RectRoiWidget(Qt.QWidget):
    sigRoiApplied = Qt.Signal(object)

    def __init__(self, plot, parent=None):
        """Widget displaying the state of a ROI manager.

        :param PlotWidget plot: an instance of silx Plot
        :param QWidget parent:
        """
        # TODO : support multiple ROIs then batch them
        super(RectRoiWidget, self).__init__(parent)

        self.__roiManager = ImageRoiManager(plot)

        self.__roiToolBar = self.__roiManager.toolBar(
            rois=["rectangle"], options=["show"]
        )
        self.__roiToolBar.setMovable(False)

        topLayout = Qt.QVBoxLayout(self)

        grpBox = GroupBox("ROI")
        layout = Qt.QGridLayout(grpBox)

        row = 0
        layout.addWidget(self.__roiToolBar, row, 0, 1, 2, Qt.Qt.AlignTop)

        row += 1
        self._xEdit = StyledLineEdit(nChar=6)
        self._xEdit.setReadOnly(True)
        layout.addWidget(Qt.QLabel("x="), row, 0, Qt.Qt.AlignTop)
        layout.addWidget(self._xEdit, row, 1, Qt.Qt.AlignTop)

        row += 1
        self._yEdit = StyledLineEdit(nChar=6)
        self._yEdit.setReadOnly(True)
        layout.addWidget(Qt.QLabel("y="), row, 0, Qt.Qt.AlignTop)
        layout.addWidget(self._yEdit, row, 1, Qt.Qt.AlignTop)

        row += 1
        self._wEdit = StyledLineEdit(nChar=6)
        self._wEdit.setReadOnly(True)
        layout.addWidget(Qt.QLabel("w="), row, 0, Qt.Qt.AlignTop)
        layout.addWidget(self._wEdit, row, 1, Qt.Qt.AlignTop)

        row += 1
        self._hEdit = StyledLineEdit(nChar=6)
        self._hEdit.setReadOnly(True)
        layout.addWidget(Qt.QLabel("h="), row, 0, Qt.Qt.AlignTop)
        layout.addWidget(self._hEdit, row, 1, Qt.Qt.AlignTop)

        row += 1

        hLayout = Qt.QHBoxLayout()

        style = Qt.QApplication.style()

        self.__applyButtonWithoutRoi = False

        icon = style.standardIcon(Qt.QStyle.SP_DialogApplyButton)
        self.__applyBn = Qt.QToolButton()
        self.__applyBn.setToolTip("Apply ROI")
        self.__applyBn.setStatusTip("Apply ROI")
        self.__applyBn.setIcon(icon)
        self.__applyBn.setToolButtonStyle(Qt.Qt.ToolButtonTextBesideIcon)
        self.__applyBn.setText("Apply ROI")
        self.__applyBn.setEnabled(False)
        hLayout.addWidget(self.__applyBn)
        self.__applyBn.clicked.connect(self.__applyRoi)

        icon = style.standardIcon(Qt.QStyle.SP_DialogCloseButton)
        self.__discardBn = Qt.QToolButton()
        self.__discardBn.setToolTip("Discard ROI")
        self.__discardBn.setStatusTip("Discard ROI")
        self.__discardBn.setIcon(icon)
        self.__discardBn.setEnabled(False)
        hLayout.addWidget(self.__discardBn, Qt.Qt.AlignRight)
        self.__discardBn.clicked.connect(self.__discardRoi)

        layout.addLayout(hLayout, row, 0, 1, 2, Qt.Qt.AlignCenter)

        # topLayout.setSizeConstraint(Qt.QLayout.SetMinimumSize)

        topLayout.addWidget(grpBox)
        topLayout.addStretch(100)

        self.__roiManager.sigRoiDrawingFinished.connect(
            self.__roiDrawingFinished, Qt.Qt.QueuedConnection
        )
        self.__roiManager.sigRoiRemoved.connect(
            self.__roiRemoved, Qt.Qt.QueuedConnection
        )
        self.__roiManager.sigRoiMoved.connect(self.__roiMoved, Qt.Qt.QueuedConnection)

    def clearRoi(self):
        self.__roiManager.plot().setInteractiveMode("zoom", source=self)
        self.__discardRoi()

    def roiManager(self):
        """Returns the roiManager"""
        return self.__roiManager

    def applyButton(self):
        """Returns the apply button.

        It is mostly useful to customize the text displayed by this button.
        """
        return self.__applyBn

    def setApplyButtonWithoutRoi(self, enabled):
        """Set whether the apply button is disabled when there is no ROI or not

        :param bool enabled: True to always enable the ROI button
        """
        enabled = bool(enabled)
        self.__applyButtonWithoutRoi = enabled
        self.__applyBn.setEnabled(enabled or len(self.__roiManager.rois) != 0)

    def sizeHint(self):
        return Qt.QSize(self.__roiToolBar.sizeHint().width() + 10, 0)

    def __discardRoi(self):
        self.__roiManager.clear()

    def __applyRoi(self):
        # At the moment we only support one roi at a time.
        roi = self.__roiManager.rois
        if len(roi) == 0:
            self.sigRoiApplied.emit(None)
        else:
            roiItem = self.__roiManager.roiItem(roi[0])
            xMin = roiItem.pos[0]
            xMax = xMin + roiItem.width
            yMin = roiItem.pos[1]
            yMax = yMin + roiItem.height
            self.sigRoiApplied.emit([xMin, xMax, yMin, yMax])

    def __roiDrawingFinished(self, event):
        self.__display(event["xdata"], event["ydata"])
        self.__discardBn.setEnabled(True)
        self.__applyBn.setEnabled(True)

    def __clear(self):
        self._xEdit.clear()
        self._yEdit.clear()
        self._wEdit.clear()
        self._hEdit.clear()

    def __display(self, xData, yData):
        xMin, xMax = xData[0], xData[2]
        if xMax < xMin:
            xMin, xMax = xMax, xMin
        yMin, yMax = yData[0], yData[1]
        if yMax < yMin:
            yMin, yMax = yMax, yMin
        self._xEdit.setText(str(xMin))
        self._yEdit.setText(str(yMin))
        self._wEdit.setText(str(xMax - xMin))
        self._hEdit.setText(str(yMax - yMin))

    def __roiRemoved(self, name):
        self.__clear()
        self.__discardBn.setEnabled(False)
        if not self.__applyButtonWithoutRoi:
            self.__applyBn.setEnabled(False)

    def __roiMoved(self, event):
        self.__display(event["xdata"], event["ydata"])
