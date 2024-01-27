import functools
import os

from silx.gui import qt as Qt
from silx.gui.icons import getQIcon
from silx.utils.weakref import WeakList

from .Utils import nextFileName

from .widgets.Wizard import XsocsWizard
from .widgets.ProjectChooser import ProjectChooserDialog

from .view.FitView import FitView

from .model.TreeView import TreeView
from .model.ModelDef import ModelRoles
from .model.Model import Model, RootNode

from .process.QSpaceWidget import QSpaceWidget

from .project.FitGroup import FitItem
from .project.QSpaceGroup import QSpaceItem
from .project.XsocsProject import XsocsProject
from .project.IntensityGroup import IntensityGroup
from .project.Hdf5Nodes import setH5NodeFactory, H5File
from .project.ProjectNodes import IntensityGroupNode, QSpaceItemNode, FitItemNode
from .project.XsocsH5Factory import XsocsH5Factory, h5NodeToProjectItem


_COMPANY_NAME = "ESRF"
_APP_NAME = "XSOCS"


class ProjectRoot(RootNode):
    ColumnNames = ["Item", ""]


class ProjectModel(Model):
    RootNode = ProjectRoot


class ProjectTree(TreeView):
    sigDelegateEvent = Qt.Signal(object, object)

    def delegateEvent(self, column, node, *args, **kwargs):
        # TODO : proper event
        event = (args and args[0]) or None
        self.sigDelegateEvent.emit(node, event)


class XsocsGui(Qt.QMainWindow):
    """
    Xsocs main window.
    """

    def __init__(self, parent=None, projectH5File=None):
        """

        :param parent:
        :param projectH5File: Xsocs project file to load.
        """
        super(XsocsGui, self).__init__(parent)

        self.setWindowTitle("XSOCS")

        self.statusBar()

        setH5NodeFactory(XsocsH5Factory)

        self.move(0, 0)
        self.resize(300, 600)

        self.__project = None

        self.__openedViews = WeakList()

        self.__createViews()
        self.__createActions()
        self.__createMenus()
        self.__createToolBars()

        self.__widget_setup = False

        self.__readSettings()

        self.__setupProject(projectFile=projectH5File)

    def __closeAllDataViews(self):
        """
        Closes all currently opened views.
        :return:
        """

        views = [view for view in self.__openedViews]
        for view in views:
            view.close()
            view.deleteLater()
        view = None

    def __createViews(self):
        """

        :return:
        """
        tree = ProjectTree()
        tree.setShowUniqueGroup(False)
        tree.sigDelegateEvent.connect(self.__slotViewEvent)
        model = ProjectModel(parent=tree)
        model.startModel()
        tree.setModel(model)
        self.setCentralWidget(tree)

    def __slotViewEvent(self, node, event):
        projectItem = h5NodeToProjectItem(node)
        if projectItem is None:
            raise ValueError(
                "Unknwown event for node {0} : {1}." "".format(node, event)
            )

        if isinstance(projectItem, IntensityGroup) and event["event"] == "scatter":
            self.__showIntensity(node)
        elif isinstance(projectItem, QSpaceItem) and event["event"] == "qspace":
            self.__showQSpace(node)
        elif isinstance(projectItem, FitItem) and event["event"] == "fit":
            self.__showFit(node)
        else:
            ValueError(
                "Unknwown event for item {0} : {1}." "".format(projectItem, event)
            )

    def __showIntensity(self, node=None):
        if node is None:
            intensityGroup = self.__project.intensityGroup()
            index = self.tree.pathToIndex(intensityGroup.path)
            node = index.data(ModelRoles.InternalDataRole)
        elif not isinstance(node, IntensityGroupNode):
            return

        view = node.getView(self)
        if view not in self.__openedViews:
            self.__openedViews.append(view)
        view.show()
        view.setAttribute(Qt.Qt.WA_DeleteOnClose, True)
        view.sigProcessApplied.connect(self.__intensityRoiApplied)
        view.raise_()
        # screen = Qt.QApplication.desktop()
        #     size = screen.availableGeometry(view).size()
        #     size.scale(size.width() * 0.6,
        #                size.height() * 0.6,
        #                Qt.Qt.IgnoreAspectRatio)
        #     view.resize(size)

    def __qspaceProcessDone(self, output_f):
        """Handle end of QSpace processing, add link to output file

        :param str output_f: The HDF5 file name storing the result
        """
        self.__project.qspaceGroup().addQSpace(output_f)
        self.model().refresh()

    def __intensityRoiApplied(self, event):
        xsocsFile = os.path.basename(self.__project.xsocsFile)
        xsocsPrefix = xsocsFile.rpartition(".")[0]
        template = "{0}_qspace_{{0:>04}}.h5".format(xsocsPrefix)
        output_f = nextFileName(self.__project.workdir, template)
        widget = QSpaceWidget(
            self.__project.xsocsFile,
            outQSpaceH5=output_f,
            qspaceDims=None,
            roi=event.roi,
            entries=event.entries,
            parent=self.sender(),
            shiftH5File=event.shiftFile,
            normalizer=self.sender().getNormalizer(),
        )
        widget.sigProcessDone.connect(
            functools.partial(self.__qspaceProcessDone, output_f)
        )

        widget.exec_()
        if widget.status == QSpaceWidget.StatusCompleted:
            # Select and display the QSpace
            qspaceItem = self.__project.qspaceGroup().getQspaceItems()[-1]
            index = self.tree.pathToIndex(qspaceItem.path)
            if index.isValid():
                self.tree.setCurrentIndex(index)
                self.__showQSpace(index.data(ModelRoles.InternalDataRole))
        widget.deleteLater()

    tree = property(lambda self: self.centralWidget())

    def __showQSpace(self, node, bringToFront=True):
        if not isinstance(node, QSpaceItemNode):
            return
        view = node.getView(self)
        if view not in self.__openedViews:
            self.__openedViews.append(view)
            view.sigFitDone.connect(self.__slotFitDone)
        view.show()
        view.setAttribute(Qt.Qt.WA_DeleteOnClose, True)
        if bringToFront:
            view.raise_()
        return view

    def __slotFitDone(self, qspaceItemPath, fitFile):
        item = QSpaceItem(self.__project.filename, qspaceItemPath)
        # item = h5NodeToProjectItem(node)
        fitGroup = item.fitGroup()
        fitItem = fitGroup.addFitFile(fitFile)
        self.model().refresh()
        index = self.tree.pathToIndex(fitItem.customPath)
        if index.isValid():
            self.tree.setCurrentIndex(index)
            self.__showFit(index.data(ModelRoles.InternalDataRole))

    def __showFit(self, node):
        if not isinstance(node, FitItemNode):
            return
        view = node.getView(self)
        if view not in self.__openedViews:
            self.__openedViews.append(view)
        view.setAttribute(Qt.Qt.WA_DeleteOnClose, True)
        view.sigPointSelected.connect(self.__fitViewPointSelected)
        view.show()

    def __fitViewPointSelected(self, point):
        sender = self.sender()
        if not isinstance(sender, FitView):
            return

        qspaceItem = sender.getFitItem().parent(QSpaceItem)
        if qspaceItem is None:
            raise ValueError("This fitItem doesnt have a parent.")

        index = self.centralWidget().pathToIndex(qspaceItem.customPath)
        node = index.data(ModelRoles.InternalDataRole)
        qspaceView = self.__showQSpace(node, bringToFront=False)
        qspaceView.selectPoint(point.x, point.y)

    def model(self):
        return self.tree.model()

    def closeEvent(self, event):
        self.__writeSettings()
        super(XsocsGui, self).closeEvent(event)

    def __writeSettings(self):
        settings = Qt.QSettings(_COMPANY_NAME, _APP_NAME)
        settings.beginGroup("GUI")
        settings.setValue("MainWindow/size", self.size())
        settings.setValue("MainWindow/pos", self.pos())
        settings.setValue("MainWindow/state", self.saveState())
        settings.endGroup()

    def __readSettings(self):
        settings = Qt.QSettings(_COMPANY_NAME, _APP_NAME)
        settings.beginGroup("gui")
        self.resize(settings.value("MainWindow/size", Qt.QSize(400, 400)))
        self.move(settings.value("MainWindow/pos", Qt.QPoint(200, 200)))
        self.restoreState(settings.value("MainWindow/state", Qt.QByteArray()))
        settings.endGroup()

    def __setupProject(self, projectFile=None):
        if projectFile is None:
            self.__project = None
            return

        if not os.path.exists(projectFile):
            return

        mode = "r+"
        project = XsocsProject(projectFile, mode=mode)
        rootNode = H5File(h5File=projectFile)
        model = self.tree.model()
        model.removeRow(0)
        model.appendGroup(rootNode)
        self.__project = project

        self.__showIntensity()
        return True

    def __createActions(self):
        style = Qt.QApplication.style()
        self.__actions = actions = {}

        # load
        icon = style.standardIcon(Qt.QStyle.SP_DialogOpenButton)
        openAct = Qt.QAction(icon, "&Open project", self)
        openAct.setShortcuts(Qt.QKeySequence.Open)
        openAct.setStatusTip("Open an existing project")
        openAct.triggered.connect(self.__openProject)
        actions["open"] = openAct

        # create
        icon = getQIcon("xsocs:gui/icons/create_project")
        createAct = Qt.QAction(icon, "&Create project", self)
        createAct.setShortcuts(Qt.QKeySequence.New)
        createAct.setStatusTip("Create a new project")
        createAct.triggered.connect(self.__createProject)
        actions["create"] = createAct

        # exit the application
        icon = style.standardIcon(Qt.QStyle.SP_DialogCancelButton)
        quitAct = Qt.QAction(icon, "E&xit", self)
        quitAct.setShortcuts(Qt.QKeySequence.Quit)
        quitAct.setStatusTip("Exit the application")
        quitAct.triggered.connect(Qt.QApplication.instance().closeAllWindows)
        actions["quit"] = quitAct

        # "about" action
        aboutAct = Qt.QAction("&About", self)
        aboutAct.setStatusTip("Show the application's About box")
        actions["about"] = aboutAct

    def __createMenus(self):
        self.__menus = menus = {}
        actions = self.__actions
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(actions["open"])
        fileMenu.addAction(actions["create"])
        fileMenu.addSeparator()
        fileMenu.addAction(actions["quit"])

        menuBar.addSeparator()

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(actions["about"])

        menus["file"] = fileMenu
        menus["help"] = helpMenu

    def __createToolBars(self):
        actions = self.__actions
        toolBar = self.addToolBar("File")
        toolBar.setObjectName("Toolbar/File")
        toolBar.addAction(actions["open"])
        toolBar.addAction(actions["create"])

    def __openProject(self):
        dialog = ProjectChooserDialog(self)
        dialog.setMinimumWidth(500)
        rc = dialog.exec_()
        if rc == Qt.QDialog.Accepted:
            projectFile = dialog.projectFile
            dialog.deleteLater()
        else:
            dialog.deleteLater()
            return
        self.__closeAllDataViews()
        self.__setupProject(projectFile)

    def __createProject(self):
        wizard = XsocsWizard(parent=self)
        if wizard.exec_() == Qt.QDialog.Accepted:
            # TODO : we suppose that we get a valid file... maybe we should
            # perform some checks...
            projectFile = wizard.projectFile
            wizard.deleteLater()
        else:
            wizard.deleteLater()
            return False

        self.__setupProject(projectFile=projectFile)
        return True
