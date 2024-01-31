"""CustomLineChart"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1756
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_LINE_CHART = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "CustomLineChart"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomLineChart",)


Self = TypeVar("Self", bound="CustomLineChart")


class CustomLineChart(_1756.CustomReportChart):
    """CustomLineChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_LINE_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomLineChart")

    class _Cast_CustomLineChart:
        """Special nested class for casting CustomLineChart to subclasses."""

        def __init__(
            self: "CustomLineChart._Cast_CustomLineChart", parent: "CustomLineChart"
        ):
            self._parent = parent

        @property
        def custom_report_chart(self: "CustomLineChart._Cast_CustomLineChart"):
            return self._parent._cast(_1756.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CustomLineChart._Cast_CustomLineChart",
        ):
            pass

            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomLineChart._Cast_CustomLineChart",
        ):
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self: "CustomLineChart._Cast_CustomLineChart"):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(self: "CustomLineChart._Cast_CustomLineChart"):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomLineChart._Cast_CustomLineChart",
        ) -> "CustomLineChart":
            return self._parent

        def __getattr__(self: "CustomLineChart._Cast_CustomLineChart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomLineChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def x_values(self: Self):
        """Method does not return."""
        self.wrapped.XValues()

    def y_values(self: Self):
        """Method does not return."""
        self.wrapped.YValues()

    @property
    def cast_to(self: Self) -> "CustomLineChart._Cast_CustomLineChart":
        return self._Cast_CustomLineChart(self)
