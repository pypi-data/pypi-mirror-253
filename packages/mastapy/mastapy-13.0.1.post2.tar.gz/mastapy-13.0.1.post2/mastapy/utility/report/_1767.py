"""CustomReportItemContainerCollectionItem"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainerCollectionItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainerCollectionItem",)


Self = TypeVar("Self", bound="CustomReportItemContainerCollectionItem")


class CustomReportItemContainerCollectionItem(_1764.CustomReportItemContainer):
    """CustomReportItemContainerCollectionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CustomReportItemContainerCollectionItem"
    )

    class _Cast_CustomReportItemContainerCollectionItem:
        """Special nested class for casting CustomReportItemContainerCollectionItem to subclasses."""

        def __init__(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
            parent: "CustomReportItemContainerCollectionItem",
        ):
            self._parent = parent

        @property
        def custom_report_item_container(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ):
            return self._parent._cast(_1764.CustomReportItemContainer)

        @property
        def custom_report_item(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_report_column(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ):
            from mastapy.utility.report import _1758

            return self._parent._cast(_1758.CustomReportColumn)

        @property
        def custom_report_tab(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ):
            from mastapy.utility.report import _1775

            return self._parent._cast(_1775.CustomReportTab)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "CustomReportItemContainerCollectionItem":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
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
        self: Self, instance_to_wrap: "CustomReportItemContainerCollectionItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem":
        return self._Cast_CustomReportItemContainerCollectionItem(self)
