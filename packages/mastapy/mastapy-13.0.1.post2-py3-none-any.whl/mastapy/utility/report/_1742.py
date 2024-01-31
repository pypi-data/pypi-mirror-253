"""AdHocCustomTable"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AD_HOC_CUSTOM_TABLE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "AdHocCustomTable"
)


__docformat__ = "restructuredtext en"
__all__ = ("AdHocCustomTable",)


Self = TypeVar("Self", bound="AdHocCustomTable")


class AdHocCustomTable(_1760.CustomReportDefinitionItem):
    """AdHocCustomTable

    This is a mastapy class.
    """

    TYPE = _AD_HOC_CUSTOM_TABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdHocCustomTable")

    class _Cast_AdHocCustomTable:
        """Special nested class for casting AdHocCustomTable to subclasses."""

        def __init__(
            self: "AdHocCustomTable._Cast_AdHocCustomTable", parent: "AdHocCustomTable"
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "AdHocCustomTable._Cast_AdHocCustomTable",
        ):
            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "AdHocCustomTable._Cast_AdHocCustomTable",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(self: "AdHocCustomTable._Cast_AdHocCustomTable"):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def ad_hoc_custom_table(
            self: "AdHocCustomTable._Cast_AdHocCustomTable",
        ) -> "AdHocCustomTable":
            return self._parent

        def __getattr__(self: "AdHocCustomTable._Cast_AdHocCustomTable", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdHocCustomTable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AdHocCustomTable._Cast_AdHocCustomTable":
        return self._Cast_AdHocCustomTable(self)
