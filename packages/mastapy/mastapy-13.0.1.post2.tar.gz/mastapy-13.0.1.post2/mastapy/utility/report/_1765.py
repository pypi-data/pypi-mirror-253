"""CustomReportItemContainerCollection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.utility.report import _1766
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainerCollection"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1767


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainerCollection",)


Self = TypeVar("Self", bound="CustomReportItemContainerCollection")
T = TypeVar("T", bound="_1767.CustomReportItemContainerCollectionItem")


class CustomReportItemContainerCollection(
    _1766.CustomReportItemContainerCollectionBase, Generic[T]
):
    """CustomReportItemContainerCollection

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItemContainerCollection")

    class _Cast_CustomReportItemContainerCollection:
        """Special nested class for casting CustomReportItemContainerCollection to subclasses."""

        def __init__(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
            parent: "CustomReportItemContainerCollection",
        ):
            self._parent = parent

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
        ):
            return self._parent._cast(_1766.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
        ):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_report_columns(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
        ):
            from mastapy.utility.report import _1759

            return self._parent._cast(_1759.CustomReportColumns)

        @property
        def custom_report_tabs(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
        ):
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportTabs)

        @property
        def custom_report_item_container_collection(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
        ) -> "CustomReportItemContainerCollection":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CustomReportItemContainerCollection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection"
    ):
        return self._Cast_CustomReportItemContainerCollection(self)
