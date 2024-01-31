"""DatabaseKey"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_KEY = python_net_import("SMT.MastaAPI.Utility.Databases", "DatabaseKey")


__docformat__ = "restructuredtext en"
__all__ = ("DatabaseKey",)


Self = TypeVar("Self", bound="DatabaseKey")


class DatabaseKey(_0.APIBase):
    """DatabaseKey

    This is a mastapy class.
    """

    TYPE = _DATABASE_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatabaseKey")

    class _Cast_DatabaseKey:
        """Special nested class for casting DatabaseKey to subclasses."""

        def __init__(self: "DatabaseKey._Cast_DatabaseKey", parent: "DatabaseKey"):
            self._parent = parent

        @property
        def user_defined_property_key(self: "DatabaseKey._Cast_DatabaseKey"):
            from mastapy.utility.scripting import _1740

            return self._parent._cast(_1740.UserDefinedPropertyKey)

        @property
        def custom_report_key(self: "DatabaseKey._Cast_DatabaseKey"):
            from mastapy.utility.report import _1768

            return self._parent._cast(_1768.CustomReportKey)

        @property
        def named_key(self: "DatabaseKey._Cast_DatabaseKey"):
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedKey)

        @property
        def rolling_bearing_key(self: "DatabaseKey._Cast_DatabaseKey"):
            from mastapy.bearings import _1894

            return self._parent._cast(_1894.RollingBearingKey)

        @property
        def database_key(self: "DatabaseKey._Cast_DatabaseKey") -> "DatabaseKey":
            return self._parent

        def __getattr__(self: "DatabaseKey._Cast_DatabaseKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatabaseKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DatabaseKey._Cast_DatabaseKey":
        return self._Cast_DatabaseKey(self)
