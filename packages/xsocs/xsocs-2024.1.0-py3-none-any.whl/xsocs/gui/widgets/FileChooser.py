from silx.gui import qt as Qt

from .Input import StyledLineEdit


class FileChooser(Qt.QWidget):
    sigSelectionChanged = Qt.Signal(object)

    label = property(lambda self: self.findChild(Qt.QLabel))
    lineEdit = property(lambda self: self.findChild(Qt.QLineEdit))
    fileDialog = property(lambda self: self.__fileDialog)
    selectedPath = property(lambda self: self.__selectedPath)

    appendPath = property(lambda self: self.__appendPath)

    @appendPath.setter
    def appendPath(self, append):
        self.__appendPath = append

    def __init__(
        self,
        parent=None,
        fileMode=None,
        options=None,
        appendPath=None,
        noLabel=False,
        **kwargs
    ):
        """
        Extra arguments are passed to the QFileDialog constructor
        :param parent Qt.QWidget:
        :param fileMode Qt.QFileDialog.FileMode:
        :param options Qt.QFileDialog.Options:
        :param noLabel bool: Set to True to remove the label in front of the
            line edit.
        :param kwargs: Keyword arguments passed to the QFileDialog constructor.
        """
        super(FileChooser, self).__init__(parent)

        self.__selectedPath = None
        self.__appendPath = appendPath

        layout = Qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        lineEdit = StyledLineEdit()
        lineEdit.setAlignment(Qt.Qt.AlignLeft)
        lineEdit.setReadOnly(True)

        pickButton = Qt.QToolButton()
        style = Qt.QApplication.style()
        icon = style.standardIcon(Qt.QStyle.SP_DialogOpenButton)
        pickButton.setIcon(icon)

        if not noLabel:
            label = Qt.QLabel("Path :")
            layout.addWidget(label)

        layout.addWidget(lineEdit)
        layout.addWidget(pickButton)

        pickButton.clicked.connect(self.__pickFile)

        self.__fileDialog = dialog = Qt.QFileDialog(**kwargs)

        if fileMode is not None:
            dialog.setFileMode(fileMode)

        if options is not None:
            dialog.setOptions(options)

    def __pickFile(self):
        dialog = self.__fileDialog
        if dialog.exec_():
            newPath = dialog.selectedFiles()[0]
            if self.__appendPath is not None:
                newPath = newPath + self.__appendPath
            self.lineEdit.setText(newPath)
            if newPath != self.__selectedPath:
                self.__selectedPath = newPath
                self.sigSelectionChanged.emit(newPath)
