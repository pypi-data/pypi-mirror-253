"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1577 import Command
    from ._1578 import AnalysisRunInformation
    from ._1579 import DispatcherHelper
    from ._1580 import EnvironmentSummary
    from ._1581 import ExternalFullFEFileOption
    from ._1582 import FileHistory
    from ._1583 import FileHistoryItem
    from ._1584 import FolderMonitor
    from ._1586 import IndependentReportablePropertiesBase
    from ._1587 import InputNamePrompter
    from ._1588 import IntegerRange
    from ._1589 import LoadCaseOverrideOption
    from ._1590 import MethodOutcome
    from ._1591 import MethodOutcomeWithResult
    from ._1592 import MKLVersion
    from ._1593 import NumberFormatInfoSummary
    from ._1594 import PerMachineSettings
    from ._1595 import PersistentSingleton
    from ._1596 import ProgramSettings
    from ._1597 import PushbulletSettings
    from ._1598 import RoundingMethods
    from ._1599 import SelectableFolder
    from ._1600 import SystemDirectory
    from ._1601 import SystemDirectoryPopulator
else:
    import_structure = {
        "_1577": ["Command"],
        "_1578": ["AnalysisRunInformation"],
        "_1579": ["DispatcherHelper"],
        "_1580": ["EnvironmentSummary"],
        "_1581": ["ExternalFullFEFileOption"],
        "_1582": ["FileHistory"],
        "_1583": ["FileHistoryItem"],
        "_1584": ["FolderMonitor"],
        "_1586": ["IndependentReportablePropertiesBase"],
        "_1587": ["InputNamePrompter"],
        "_1588": ["IntegerRange"],
        "_1589": ["LoadCaseOverrideOption"],
        "_1590": ["MethodOutcome"],
        "_1591": ["MethodOutcomeWithResult"],
        "_1592": ["MKLVersion"],
        "_1593": ["NumberFormatInfoSummary"],
        "_1594": ["PerMachineSettings"],
        "_1595": ["PersistentSingleton"],
        "_1596": ["ProgramSettings"],
        "_1597": ["PushbulletSettings"],
        "_1598": ["RoundingMethods"],
        "_1599": ["SelectableFolder"],
        "_1600": ["SystemDirectory"],
        "_1601": ["SystemDirectoryPopulator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Command",
    "AnalysisRunInformation",
    "DispatcherHelper",
    "EnvironmentSummary",
    "ExternalFullFEFileOption",
    "FileHistory",
    "FileHistoryItem",
    "FolderMonitor",
    "IndependentReportablePropertiesBase",
    "InputNamePrompter",
    "IntegerRange",
    "LoadCaseOverrideOption",
    "MethodOutcome",
    "MethodOutcomeWithResult",
    "MKLVersion",
    "NumberFormatInfoSummary",
    "PerMachineSettings",
    "PersistentSingleton",
    "ProgramSettings",
    "PushbulletSettings",
    "RoundingMethods",
    "SelectableFolder",
    "SystemDirectory",
    "SystemDirectoryPopulator",
)
