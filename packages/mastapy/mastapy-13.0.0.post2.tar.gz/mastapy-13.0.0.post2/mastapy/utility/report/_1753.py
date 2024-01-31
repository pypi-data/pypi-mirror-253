"""CustomImage"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_IMAGE = python_net_import("SMT.MastaAPI.Utility.Report", "CustomImage")


__docformat__ = "restructuredtext en"
__all__ = ("CustomImage",)


Self = TypeVar("Self", bound="CustomImage")


class CustomImage(_1752.CustomGraphic):
    """CustomImage

    This is a mastapy class.
    """

    TYPE = _CUSTOM_IMAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomImage")

    class _Cast_CustomImage:
        """Special nested class for casting CustomImage to subclasses."""

        def __init__(self: "CustomImage._Cast_CustomImage", parent: "CustomImage"):
            self._parent = parent

        @property
        def custom_graphic(self: "CustomImage._Cast_CustomImage"):
            return self._parent._cast(_1752.CustomGraphic)

        @property
        def custom_report_definition_item(self: "CustomImage._Cast_CustomImage"):
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self: "CustomImage._Cast_CustomImage"):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(self: "CustomImage._Cast_CustomImage"):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def loaded_bearing_chart_reporter(self: "CustomImage._Cast_CustomImage"):
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingChartReporter)

        @property
        def custom_image(self: "CustomImage._Cast_CustomImage") -> "CustomImage":
            return self._parent

        def __getattr__(self: "CustomImage._Cast_CustomImage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomImage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomImage._Cast_CustomImage":
        return self._Cast_CustomImage(self)
