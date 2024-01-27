from ...io.XsocsH5 import ScanPositions

from .ProjectItem import ProjectItem
from .ProjectDef import ItemClassDef


@ItemClassDef("ScanPositionsItem")
class ScanPositionsItem(ProjectItem):
    def _createItem(self):
        with self.xsocsH5 as h5f:
            entries = h5f.entries()
            entry = entries[0]
            scan_positions = h5f.scan_positions(entry)
            pathTpl = self.path + "/" + "{0}"
            with self:
                itemPath = pathTpl.format("pos_0")
                self._set_array_data(itemPath, scan_positions.pos_0)
                itemPath = pathTpl.format("pos_1")
                self._set_array_data(itemPath, scan_positions.pos_1)
                itemPath = pathTpl.format("motor_0")
                self._set_scalar_data(itemPath, scan_positions.motor_0)
                itemPath = pathTpl.format("motor_1")
                self._set_scalar_data(itemPath, scan_positions.motor_1)
                itemPath = pathTpl.format("n_0")
                self._set_scalar_data(itemPath, scan_positions.shape[0])
                itemPath = pathTpl.format("n_1")
                self._set_scalar_data(itemPath, scan_positions.shape[1])

    def positions(self):
        pathTpl = self.path + "/" + "{0}"
        with self:
            itemPath = pathTpl.format("pos_0")
            pos_0 = self._get_array_data(itemPath)
            itemPath = pathTpl.format("pos_1")
            pos_1 = self._get_array_data(itemPath)
            itemPath = pathTpl.format("motor_0")
            motor_0 = self._get_scalar_data(itemPath)
            itemPath = pathTpl.format("motor_1")
            motor_1 = self._get_scalar_data(itemPath)
            itemPath = pathTpl.format("n_0")
            n_0 = self._get_scalar_data(itemPath)
            itemPath = pathTpl.format("n_1")
            n_1 = self._get_scalar_data(itemPath)
        return ScanPositions(
            motor_0=motor_0, pos_0=pos_0, motor_1=motor_1, pos_1=pos_1, shape=(n_0, n_1)
        )
