from .ProjectItem import ProjectItem
from .ProjectDef import ItemClassDef


@ItemClassDef("AcqDataGroup")
class AcqDataGroup(ProjectItem):
    itemName = "Acquisition"

    ScanCommandPath = "Scan"
    SamplePath = "Sample"
    EntriesPath = "Entries"

    def _createItem(self):
        with self.xsocsH5 as xsocsH5:
            with self:
                # adding parameter values to this item
                entries = xsocsH5.entries()
                # TODO : make sure that all parameters are consistent
                scan_params = xsocsH5.scan_params(entries[0])
                path_tpl = "{0}/{1}/{{0}}".format(
                    self.path, AcqDataGroup.ScanCommandPath
                )
                for key, value in scan_params.items():
                    self._set_scalar_data(path_tpl.format(key), value)

                path = self.path + "/" + AcqDataGroup.EntriesPath
                self.add_soft_link(path, ProjectItem.XsocsH5FilePath)
