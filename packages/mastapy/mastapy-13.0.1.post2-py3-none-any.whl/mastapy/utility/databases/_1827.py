"""DatabaseSettings"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.utility import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "DatabaseSettings"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1825


__docformat__ = "restructuredtext en"
__all__ = ("DatabaseSettings",)


Self = TypeVar("Self", bound="DatabaseSettings")


class DatabaseSettings(_1594.PerMachineSettings):
    """DatabaseSettings

    This is a mastapy class.
    """

    TYPE = _DATABASE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatabaseSettings")

    class _Cast_DatabaseSettings:
        """Special nested class for casting DatabaseSettings to subclasses."""

        def __init__(
            self: "DatabaseSettings._Cast_DatabaseSettings", parent: "DatabaseSettings"
        ):
            self._parent = parent

        @property
        def per_machine_settings(self: "DatabaseSettings._Cast_DatabaseSettings"):
            return self._parent._cast(_1594.PerMachineSettings)

        @property
        def persistent_singleton(self: "DatabaseSettings._Cast_DatabaseSettings"):
            from mastapy.utility import _1595

            return self._parent._cast(_1595.PersistentSingleton)

        @property
        def database_settings(
            self: "DatabaseSettings._Cast_DatabaseSettings",
        ) -> "DatabaseSettings":
            return self._parent

        def __getattr__(self: "DatabaseSettings._Cast_DatabaseSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatabaseSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_settings(self: Self) -> "_1825.DatabaseConnectionSettings":
        """mastapy.utility.databases.DatabaseConnectionSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DatabaseSettings._Cast_DatabaseSettings":
        return self._Cast_DatabaseSettings(self)
