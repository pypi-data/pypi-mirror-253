"""CustomTableAndChart"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE_AND_CHART = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "CustomTableAndChart"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomTableAndChart",)


Self = TypeVar("Self", bound="CustomTableAndChart")


class CustomTableAndChart(_1780.CustomTable):
    """CustomTableAndChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE_AND_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomTableAndChart")

    class _Cast_CustomTableAndChart:
        """Special nested class for casting CustomTableAndChart to subclasses."""

        def __init__(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
            parent: "CustomTableAndChart",
        ):
            self._parent = parent

        @property
        def custom_table(self: "CustomTableAndChart._Cast_CustomTableAndChart"):
            return self._parent._cast(_1780.CustomTable)

        @property
        def custom_report_multi_property_item(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ):
            pass

            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ):
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(self: "CustomTableAndChart._Cast_CustomTableAndChart"):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_table_and_chart(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "CustomTableAndChart":
            return self._parent

        def __getattr__(
            self: "CustomTableAndChart._Cast_CustomTableAndChart", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomTableAndChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomTableAndChart._Cast_CustomTableAndChart":
        return self._Cast_CustomTableAndChart(self)
