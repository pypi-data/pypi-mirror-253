from silx.gui import qt as Qt


class ModelColumns(object):
    NameColumn, ValueColumn, ColumnMax = range(3)
    ColumnNames = ["Name", "Value"]


class ModelRoles(object):
    _RoleMin = Qt.Qt.UserRole
    RoleMax = _RoleMin + 4

    RolesList = range(_RoleMin, RoleMax)
    (InternalDataRole, EditorClassRole, PersistentEditorRole, EnabledRole) = RolesList
