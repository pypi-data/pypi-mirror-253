"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1742 import AdHocCustomTable
    from ._1743 import AxisSettings
    from ._1744 import BlankRow
    from ._1745 import CadPageOrientation
    from ._1746 import CadPageSize
    from ._1747 import CadTableBorderType
    from ._1748 import ChartDefinition
    from ._1749 import SMTChartPointShape
    from ._1750 import CustomChart
    from ._1751 import CustomDrawing
    from ._1752 import CustomGraphic
    from ._1753 import CustomImage
    from ._1754 import CustomReport
    from ._1755 import CustomReportCadDrawing
    from ._1756 import CustomReportChart
    from ._1757 import CustomReportChartItem
    from ._1758 import CustomReportColumn
    from ._1759 import CustomReportColumns
    from ._1760 import CustomReportDefinitionItem
    from ._1761 import CustomReportHorizontalLine
    from ._1762 import CustomReportHtmlItem
    from ._1763 import CustomReportItem
    from ._1764 import CustomReportItemContainer
    from ._1765 import CustomReportItemContainerCollection
    from ._1766 import CustomReportItemContainerCollectionBase
    from ._1767 import CustomReportItemContainerCollectionItem
    from ._1768 import CustomReportKey
    from ._1769 import CustomReportMultiPropertyItem
    from ._1770 import CustomReportMultiPropertyItemBase
    from ._1771 import CustomReportNameableItem
    from ._1772 import CustomReportNamedItem
    from ._1773 import CustomReportPropertyItem
    from ._1774 import CustomReportStatusItem
    from ._1775 import CustomReportTab
    from ._1776 import CustomReportTabs
    from ._1777 import CustomReportText
    from ._1778 import CustomRow
    from ._1779 import CustomSubReport
    from ._1780 import CustomTable
    from ._1781 import DefinitionBooleanCheckOptions
    from ._1782 import DynamicCustomReportItem
    from ._1783 import FontStyle
    from ._1784 import FontWeight
    from ._1785 import HeadingSize
    from ._1786 import SimpleChartDefinition
    from ._1787 import UserTextRow
else:
    import_structure = {
        "_1742": ["AdHocCustomTable"],
        "_1743": ["AxisSettings"],
        "_1744": ["BlankRow"],
        "_1745": ["CadPageOrientation"],
        "_1746": ["CadPageSize"],
        "_1747": ["CadTableBorderType"],
        "_1748": ["ChartDefinition"],
        "_1749": ["SMTChartPointShape"],
        "_1750": ["CustomChart"],
        "_1751": ["CustomDrawing"],
        "_1752": ["CustomGraphic"],
        "_1753": ["CustomImage"],
        "_1754": ["CustomReport"],
        "_1755": ["CustomReportCadDrawing"],
        "_1756": ["CustomReportChart"],
        "_1757": ["CustomReportChartItem"],
        "_1758": ["CustomReportColumn"],
        "_1759": ["CustomReportColumns"],
        "_1760": ["CustomReportDefinitionItem"],
        "_1761": ["CustomReportHorizontalLine"],
        "_1762": ["CustomReportHtmlItem"],
        "_1763": ["CustomReportItem"],
        "_1764": ["CustomReportItemContainer"],
        "_1765": ["CustomReportItemContainerCollection"],
        "_1766": ["CustomReportItemContainerCollectionBase"],
        "_1767": ["CustomReportItemContainerCollectionItem"],
        "_1768": ["CustomReportKey"],
        "_1769": ["CustomReportMultiPropertyItem"],
        "_1770": ["CustomReportMultiPropertyItemBase"],
        "_1771": ["CustomReportNameableItem"],
        "_1772": ["CustomReportNamedItem"],
        "_1773": ["CustomReportPropertyItem"],
        "_1774": ["CustomReportStatusItem"],
        "_1775": ["CustomReportTab"],
        "_1776": ["CustomReportTabs"],
        "_1777": ["CustomReportText"],
        "_1778": ["CustomRow"],
        "_1779": ["CustomSubReport"],
        "_1780": ["CustomTable"],
        "_1781": ["DefinitionBooleanCheckOptions"],
        "_1782": ["DynamicCustomReportItem"],
        "_1783": ["FontStyle"],
        "_1784": ["FontWeight"],
        "_1785": ["HeadingSize"],
        "_1786": ["SimpleChartDefinition"],
        "_1787": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
