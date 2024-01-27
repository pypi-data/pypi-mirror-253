from collections import OrderedDict
import functools
import logging
from multiprocessing import Pool

from silx.gui import qt as Qt

from ... import config
from ..model.Node import Node
from ..model.ModelDef import ModelColumns

from ..model.Model import Model
from ..model.Node import ModelDataList
from ..model.Nodes import ProgressBarEditor
from ..model.TreeView import TreeView
from ...io.XsocsH5 import XsocsH5

from .ProjectItem import ProjectItem
from .ProjectDef import ItemClassDef


_logger = logging.getLogger(__name__)


@ItemClassDef("IntensityItem")
class IntensityItem(ProjectItem):
    @property
    def entry(self):
        return self.path.rsplit("/")[-1]

    def getScatterData(self):
        intensity = self._get_array_data(self.path)
        scanPositions = self.xsocsH5.scan_positions(
            self.xsocsH5.entries()[0] if self.entry == "Total" else self.entry
        )
        return intensity, scanPositions

    def getPointValue(self, index):
        with self.item_context(self.path) as dsetCtx:
            value = dsetCtx[index]
        return value


@ItemClassDef("IntensityGroup")
class IntensityGroup(ProjectItem):
    IntensityPathTpl = "{0}/{1}"

    def _createItem(self):
        path_tpl = self.IntensityPathTpl.format(self.path, "{0}")
        getIntensity(self.filename, path_tpl, self.gui)

        with self:
            entries = self.xsocsH5.entries()
            intensity = self._get_array_data(path_tpl.format(entries[0]))
            for entry in entries[1:]:
                intensity += self._get_array_data(path_tpl.format(entry))
            itemPath = self.path + "/Total"
            IntensityItem(self.filename, itemPath, mode=self.mode, data=intensity)

    def getScatterData(self):
        entry = self.xsocsH5.entries()[0]
        entryPath = self.IntensityPathTpl.format(self.path, entry)
        intensity = self._get_array_data(entryPath)
        scanPositions = self.xsocsH5.scan_positions(entry)
        return intensity, scanPositions

    def getIntensityItems(self):
        return self.children(classinfo=IntensityItem)

    def getIntensityItem(self, entry):
        itemPath = self.IntensityPathTpl.format(self.path, entry)
        return IntensityItem(self.filename, itemPath)


def _getIntensity(entry_f):
    # TODO : this works because each entry has its own separate file. Watch
    # out errors (maybe?) if one day there is only one file for all
    # entries
    with XsocsH5(entry_f) as entryH5:
        cumul = entryH5.image_cumul()
    return cumul


def getIntensity(projectFile, pathTpl, view=None):
    xsocsH5 = ProjectItem(projectFile).xsocsH5

    with xsocsH5:
        entries = xsocsH5.entries()

    subject = ProgressSubject()
    tree = TreeView(view)
    tree.setShowUniqueGroup(True)
    model = Model()

    progressGroup = ProgressGroup(subject=subject, nodeName="Intensity")
    progressGroup.start()
    progressGroup.setEntries(entries)
    model.appendGroup(progressGroup)

    app = Qt.QApplication.instance()

    mw = Qt.QDialog(view)
    mw.setModal(True)
    mw.setWindowTitle("Setting up data.")
    layout = Qt.QVBoxLayout(mw)
    tree.setModel(model)
    layout.addWidget(tree)
    mw.show()
    app.processEvents()

    pool = Pool(config.DEFAULT_PROCESS_NUMBER)
    results = OrderedDict()

    def callback(subject, entry, _):
        """Callback handling apply_async success"""
        subject.sigStateChanged.emit({"id": entry, "state": "done"})

    def error_cb(subject, entry, _):
        """Callback handling apply_async error"""
        _logger.error("An error occured while processing entry: %s", entry)
        subject.sigStateChanged.emit({"id": entry, "state": "error"})

    # Start a task for each entry
    for entry in entries:
        subject.sigStateChanged.emit({"id": entry, "state": "started"})

        results[entry] = pool.apply_async(
            _getIntensity,
            args=(xsocsH5.object_filename(entry),),
            callback=functools.partial(callback, subject, entry),
            error_callback=functools.partial(error_cb, subject, entry),
        )

    pool.close()

    # Wait for all tasks to be complete while running Qt event loop
    while [res for res in results.values() if not res.ready()]:
        app.processEvents()

    # Make sure all tasks are done, but that should already be the case
    pool.join()

    # Saving result to file
    for entry, result in results.items():
        dsetPath = pathTpl.format(str(entry))

        # WARNING, make sure the file isn't opened in write mode elsewhere!!!
        if result.successful():
            IntensityItem(projectFile, dsetPath, mode="r+", data=result.get())
        else:
            _logger.error("Intensity computation failed for entry: %s", entry)

    mw.close()
    mw.deleteLater()


class ProgressSubject(Qt.QObject):
    sigStateChanged = Qt.Signal(object)

    def __init__(self, *args, **kwargs):
        super(ProgressSubject, self).__init__(*args, **kwargs)


class ProgressGroup(Node):
    editors = [ProgressBarEditor]

    def subjectSignals(self, column):
        subject = self.subject
        if subject:
            return [self.subject.sigStateChanged]
        return None

    def _setupNode(self):
        self.__completed = 0

    def pullModelData(self, column, event=None, force=False):
        if event is not None:
            self.__completed += 1
        childCount = self.childCount()
        if childCount > 0:
            return int(round(100 * self.__completed / childCount))
        else:
            return 0

    def filterEvent(self, column, event):
        args = (event and event.args and event.args[0]) or None
        if args is not None and args.get("state") == "done":
            return True, event
        return False, event

    def setEntries(self, entries):
        for entry in entries:
            self.appendChild(ProgressNode(nodeName=str(entry)))


class ProgressNode(Node):
    activeColumns = [ModelColumns.NameColumn, ModelColumns.ValueColumn]

    def filterEvent(self, column, event):
        args = (event and event.args and event.args[0]) or None
        if args is not None and args.get("id") == self.nodeName:
            return True, event
        return False, event

    def subjectSignals(self, column):
        subject = self.subject
        if subject:
            return [self.subject.sigStateChanged]
        return None

    def _setupNode(self):
        style = Qt.QApplication.style()
        icon = style.standardIcon(Qt.QStyle.SP_MediaPause)
        self._setDataInternal(ModelColumns.NameColumn, icon, Qt.Qt.DecorationRole)
        self._setDataInternal(ModelColumns.ValueColumn, "Queued", Qt.Qt.DisplayRole)

    def pullModelData(self, column, event=None, force=False):
        args = (event and event.args and event.args[0]) or None

        if args is not None:
            if column == ModelColumns.NameColumn:
                return self._setProgressIcon(args["state"])
            if column == ModelColumns.ValueColumn:
                return self._setProgressText(args["state"])

        return None

    def _setProgressIcon(self, state):
        style = Qt.QApplication.style()
        if state == "done":
            icon = style.standardIcon(Qt.QStyle.SP_DialogApplyButton)
        elif state == "started":
            icon = style.standardIcon(Qt.QStyle.SP_BrowserReload)
        elif state == "queued":
            icon = style.standardIcon(Qt.QStyle.SP_MediaPause)
        else:
            icon = style.standardIcon(Qt.QStyle.SP_TitleBarContextHelpButton)

        return ModelDataList(icon, None, Qt.Qt.DecorationRole)

    def _setProgressText(self, state):
        if state in ("done", "started", "queued"):
            text = state
        else:
            text = "?"
        return ModelDataList(text, None, Qt.Qt.DisplayRole)
