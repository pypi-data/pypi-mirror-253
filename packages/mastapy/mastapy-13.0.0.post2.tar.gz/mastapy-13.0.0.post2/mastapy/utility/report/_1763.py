"""CustomReportItem"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItem",)


Self = TypeVar("Self", bound="CustomReportItem")


class CustomReportItem(_0.APIBase):
    """CustomReportItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItem")

    class _Cast_CustomReportItem:
        """Special nested class for casting CustomReportItem to subclasses."""

        def __init__(
            self: "CustomReportItem._Cast_CustomReportItem", parent: "CustomReportItem"
        ):
            self._parent = parent

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1035

            return self._parent._cast(_1035.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1742

            return self._parent._cast(_1742.AdHocCustomTable)

        @property
        def custom_chart(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1750

            return self._parent._cast(_1750.CustomChart)

        @property
        def custom_drawing(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.CustomDrawing)

        @property
        def custom_graphic(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1752

            return self._parent._cast(_1752.CustomGraphic)

        @property
        def custom_image(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1753

            return self._parent._cast(_1753.CustomImage)

        @property
        def custom_report(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1754

            return self._parent._cast(_1754.CustomReport)

        @property
        def custom_report_cad_drawing(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.CustomReportCadDrawing)

        @property
        def custom_report_chart(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1756

            return self._parent._cast(_1756.CustomReportChart)

        @property
        def custom_report_column(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1758

            return self._parent._cast(_1758.CustomReportColumn)

        @property
        def custom_report_columns(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1759

            return self._parent._cast(_1759.CustomReportColumns)

        @property
        def custom_report_definition_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_horizontal_line(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReportHorizontalLine)

        @property
        def custom_report_html_item(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1762

            return self._parent._cast(_1762.CustomReportHtmlItem)

        @property
        def custom_report_item_container(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1764

            return self._parent._cast(_1764.CustomReportItemContainer)

        @property
        def custom_report_item_container_collection(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1765

            return self._parent._cast(_1765.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_named_item(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1772

            return self._parent._cast(_1772.CustomReportNamedItem)

        @property
        def custom_report_status_item(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportStatusItem)

        @property
        def custom_report_tab(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1775

            return self._parent._cast(_1775.CustomReportTab)

        @property
        def custom_report_tabs(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportTabs)

        @property
        def custom_report_text(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportText)

        @property
        def custom_sub_report(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1779

            return self._parent._cast(_1779.CustomSubReport)

        @property
        def custom_table(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomTable)

        @property
        def dynamic_custom_report_item(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.DynamicCustomReportItem)

        @property
        def custom_line_chart(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility_gui.charts import _1854

            return self._parent._cast(_1854.CustomLineChart)

        @property
        def custom_table_and_chart(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.utility_gui.charts import _1855

            return self._parent._cast(_1855.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.bearings.bearing_results import _1946

            return self._parent._cast(_1946.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.bearings.bearing_results import _1950

            return self._parent._cast(_1950.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.bearings.bearing_results import _1958

            return self._parent._cast(_1958.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2849,
            )

            return self._parent._cast(_2849.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4716,
            )

            return self._parent._cast(_4716.CampbellDiagramReport)

        @property
        def per_mode_results_report(self: "CustomReportItem._Cast_CustomReportItem"):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4720,
            )

            return self._parent._cast(_4720.PerModeResultsReport)

        @property
        def custom_report_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "CustomReportItem":
            return self._parent

        def __getattr__(self: "CustomReportItem._Cast_CustomReportItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    @enforce_parameter_types
    def is_main_report_item(self: Self, value: "bool"):
        self.wrapped.IsMainReportItem = bool(value) if value is not None else False

    @property
    def item_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ItemType

        if temp is None:
            return ""

        return temp

    def add_condition(self: Self):
        """Method does not return."""
        self.wrapped.AddCondition()

    @property
    def cast_to(self: Self) -> "CustomReportItem._Cast_CustomReportItem":
        return self._Cast_CustomReportItem(self)
