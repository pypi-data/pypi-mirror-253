from collections import namedtuple

from silx.gui import qt as Qt

from .ModelDef import ModelRoles

from silx.utils.weakref import WeakMethod


EditorInfo = namedtuple("EditorInfo", ["klass", "persistent"])


class EditorMixin(object):
    """
    To be used with a Qt.QWidget base.
    """

    persistent = False

    node = property(lambda self: self.__node)

    column = property(lambda self: self.__column)

    def __init__(self, parent, option, index):
        super(EditorMixin, self).__init__(parent)
        self.__node = index.data(ModelRoles.InternalDataRole)
        self.__column = index.column()
        self.setAutoFillBackground(True)
        self.__modelCb = None
        self.__viewCb = None

    @classmethod
    def paint(cls, painter, option, index):
        return False

    def notifyModel(self, *args, **kwargs):
        if not self.__modelCb:
            return
        modelCb = self.__modelCb()
        if modelCb:
            modelCb(self, *args, **kwargs)

    def notifyView(self, *args, **kwargs):
        if not self.__viewCb:
            return
        viewCb = self.__viewCb()
        if viewCb:
            viewCb(self, *args, **kwargs)

    def setViewCallback(self, callback):
        self.__viewCb = WeakMethod(callback)

    def setModelCallback(self, callback):
        self.__modelCb = WeakMethod(callback)

    def sizeHint(self):
        return Qt.QSize(0, 0)

    def setEditorData(self, index):
        node = index.data(ModelRoles.InternalDataRole)

        if node and not node.setEditorData(self, index.column()):
            value = index.data(Qt.Qt.EditRole)
            return self.setModelValue(value)

        return True

    def setModelValue(self, value):
        return False

    def getEditorData(self):
        pass
