"""CustomReportStatusItem"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_STATUS_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportStatusItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportStatusItem",)


Self = TypeVar("Self", bound="CustomReportStatusItem")


class CustomReportStatusItem(_1760.CustomReportDefinitionItem):
    """CustomReportStatusItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_STATUS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportStatusItem")

    class _Cast_CustomReportStatusItem:
        """Special nested class for casting CustomReportStatusItem to subclasses."""

        def __init__(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem",
            parent: "CustomReportStatusItem",
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem",
        ):
            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem",
        ):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_report_status_item(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem",
        ) -> "CustomReportStatusItem":
            return self._parent

        def __getattr__(
            self: "CustomReportStatusItem._Cast_CustomReportStatusItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportStatusItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomReportStatusItem._Cast_CustomReportStatusItem":
        return self._Cast_CustomReportStatusItem(self)
