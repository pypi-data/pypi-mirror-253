"""CylindricalGearTableWithMGCharts"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearTableWithMGCharts"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1034


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTableWithMGCharts",)


Self = TypeVar("Self", bound="CylindricalGearTableWithMGCharts")


class CylindricalGearTableWithMGCharts(_1780.CustomTable):
    """CylindricalGearTableWithMGCharts

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearTableWithMGCharts")

    class _Cast_CylindricalGearTableWithMGCharts:
        """Special nested class for casting CylindricalGearTableWithMGCharts to subclasses."""

        def __init__(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
            parent: "CylindricalGearTableWithMGCharts",
        ):
            self._parent = parent

        @property
        def custom_table(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ):
            return self._parent._cast(_1780.CustomTable)

        @property
        def custom_report_multi_property_item(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ):
            pass

            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ):
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
        ) -> "CylindricalGearTableWithMGCharts":
            return self._parent

        def __getattr__(
            self: "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearTableWithMGCharts.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_height(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ChartHeight

        if temp is None:
            return 0

        return temp

    @chart_height.setter
    @enforce_parameter_types
    def chart_height(self: Self, value: "int"):
        self.wrapped.ChartHeight = int(value) if value is not None else 0

    @property
    def chart_width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ChartWidth

        if temp is None:
            return 0

        return temp

    @chart_width.setter
    @enforce_parameter_types
    def chart_width(self: Self, value: "int"):
        self.wrapped.ChartWidth = int(value) if value is not None else 0

    @property
    def item_detail(self: Self) -> "_1034.CylindricalGearTableMGItemDetail":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearTableMGItemDetail"""
        temp = self.wrapped.ItemDetail

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1034",
            "CylindricalGearTableMGItemDetail",
        )(value)

    @item_detail.setter
    @enforce_parameter_types
    def item_detail(self: Self, value: "_1034.CylindricalGearTableMGItemDetail"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail",
        )
        self.wrapped.ItemDetail = value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts":
        return self._Cast_CylindricalGearTableWithMGCharts(self)
