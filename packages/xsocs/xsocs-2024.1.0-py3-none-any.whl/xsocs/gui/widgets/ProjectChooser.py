import os

from silx.gui import qt as Qt

from ...io.XsocsH5 import XsocsH5
from .FileChooser import FileChooser
from ..widgets.Containers import GroupBox
from ..project.XsocsProject import XsocsProject


class ProjectChooserDialog(Qt.QDialog):
    projectFile = property(lambda self: self.__projectFile)

    def __init__(self, parent=None):
        super(ProjectChooserDialog, self).__init__(parent)

        self.__projectFile = None

        layout = Qt.QVBoxLayout(self)

        prjChooser = ProjectChooser()
        layout.addWidget(prjChooser)
        prjChooser.sigProjectPicked.connect(self.__prjPicked)

        self.__bnBox = bnBox = Qt.QDialogButtonBox(
            Qt.QDialogButtonBox.Open | Qt.QDialogButtonBox.Cancel
        )

        bnBox.rejected.connect(self.reject)
        bnBox.accepted.connect(self.accept)

        bnBox.button(Qt.QDialogButtonBox.Open).setEnabled(False)

        layout.addWidget(bnBox)

    def __prjPicked(self, filename):
        if filename:
            self.__projectFile = filename
            enabled = True
        else:
            self.__projectFile = None
            enabled = False
        self.__bnBox.button(Qt.QDialogButtonBox.Open).setEnabled(enabled)


class ProjectChooser(Qt.QWidget):
    sigProjectPicked = Qt.Signal(object)

    projectSummary = property(lambda self: self.findChild(ProjectSummaryWidget))

    def __init__(self, parent=None):
        super(ProjectChooser, self).__init__(parent)

        layout = Qt.QVBoxLayout(self)

        self.__isValid = False
        self.__selectedPath = None

        group = GroupBox("Please select the project file to open.")
        layout.addWidget(group)

        grpLayout = Qt.QHBoxLayout(group)
        filePicker = FileChooser(fileMode=Qt.QFileDialog.ExistingFile)
        filePicker.setObjectName("PROJ_FILEPICKER")
        grpLayout.addWidget(filePicker)

        filePicker.sigSelectionChanged.connect(self.__filePicked)

        fileDialog = filePicker.fileDialog
        fileDialog.setNameFilters(["Xsocs project files (*.prj)", "Any files (*)"])

        group = GroupBox("Project Summary")
        layout.addWidget(group)
        grpLayout = Qt.QVBoxLayout(group)
        view = ProjectSummaryWidget()
        grpLayout.addWidget(view)

    def __filePicked(self, selectedPath):
        self.__selectedPath = selectedPath

        view = self.projectSummary
        view.setProjectFile(selectedPath)

        valid = view.isValidProject()

        self.__isValid = valid

        if valid:
            self.sigProjectPicked.emit(selectedPath)
        else:
            self.sigProjectPicked.emit("")

    def isValid(self):
        return self.__isValid


class ProjectSummaryWidget(Qt.QWidget):
    def __init__(self, projectFile=None, parent=None):
        super(ProjectSummaryWidget, self).__init__(parent)

        self.__valid = False

        layout = Qt.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        view = Qt.QTreeWidget()
        view.setColumnCount(2)
        view.setHeaderLabels(["Name", "Value"])

        view.header().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)

        layout.addWidget(view)

        self.setProjectFile(projectFile)

    def isValidProject(self):
        return self.__valid

    def setProjectFile(self, projectFile):
        view = self.findChild(Qt.QTreeWidget)

        view.clear()

        self.__valid = False

        if projectFile is None:
            return

        errMsg = ""

        try:
            # reading project file
            errMsg = "Failed to open X-Socs project file."
            projectH5 = XsocsProject(projectFile, mode="r")

            # reading XSOCS data file
            errMsg = "Failed to open X-Socs data file."
            xsocsFile = projectH5.xsocsFile
            xsocsH5 = XsocsH5(xsocsFile, mode="r")

            # getting entries
            errMsg = "Failed to read entries from data file."
            entries = xsocsH5.entries()

            # getting entries
            errMsg = "Failed to read scan parameters."
            params = xsocsH5.scan_params(entries[0])

            inputItem = Qt.QTreeWidgetItem(["Data file", os.path.basename(xsocsFile)])
            inputItem.setToolTip(0, xsocsFile)
            inputItem.setToolTip(1, xsocsFile)
            inputItem.addChild(Qt.QTreeWidgetItem(["Full path", xsocsFile]))
            view.addTopLevelItem(inputItem)

            # getting acquisition params
            errMsg = "Failed to read Acquisition parameters."
            title = " ".join(str(value) for value in params.values())
            commandItem = Qt.QTreeWidgetItem(["Scan", title])
            commandItem.setToolTip(0, title)
            commandItem.setToolTip(1, title)
            for key, value in params.items():
                commandItem.addChild(Qt.QTreeWidgetItem([key, str(value)]))
            view.addTopLevelItem(commandItem)

            # getting scan angles and energies
            errMsg = "Failed to read scan angles and energies."
            text = (
                "{nb_scan} (eta:[{eta1:g}°;{eta2:g}°] "
                "phi:[{phi1:g}°;{phi2:g}°] "
                "energy:[{energy1:g}eV;{energy2:g}eV])".format(
                    nb_scan=len(entries),
                    eta1=xsocsH5.positioner(entries[0], "eta"),
                    eta2=xsocsH5.positioner(entries[-1], "eta"),
                    phi1=xsocsH5.positioner(entries[0], "phi"),
                    phi2=xsocsH5.positioner(entries[-1], "phi"),
                    energy1=xsocsH5.beam_energy(entries[0]),
                    energy2=xsocsH5.beam_energy(entries[-1]),
                )
            )
            entriesItem = Qt.QTreeWidgetItem(["Scans", text])
            for entry in entries:
                text = "eta:{eta:g}°\tphi:{phi:g}°\tenergy:{nrj:g}eV".format(
                    eta=xsocsH5.positioner(entry, "eta"),
                    phi=xsocsH5.positioner(entry, "phi"),
                    nrj=xsocsH5.beam_energy(entry),
                )
                entryItem = Qt.QTreeWidgetItem([entry, text])
                entriesItem.addChild(entryItem)
            view.addTopLevelItem(entriesItem)

            for key, value in xsocsH5.acquisition_params(entries[0]).items():
                if key == "beam_energy":
                    continue  # Skip beam_energy
                view.addTopLevelItem(Qt.QTreeWidgetItem([key, str(value)]))

        except Exception as ex:
            style = Qt.QApplication.style()
            errorItem = Qt.QTreeWidgetItem(["", errMsg])
            icon = style.standardIcon(Qt.QStyle.SP_MessageBoxCritical)
            errorItem.setIcon(0, icon)
            errorItem.setBackground(1, Qt.QBrush(Qt.Qt.red))
            exItem = Qt.QTreeWidgetItem([ex.__class__.__name__, str(ex)])
            errorItem.addChild(exItem)
            view.addTopLevelItem(errorItem)
            errorItem.setExpanded(True)
            return

        self.__valid = True
