"""FEUserSettings"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_USER_SETTINGS = python_net_import("SMT.MastaAPI.NodalAnalysis", "FEUserSettings")


__docformat__ = "restructuredtext en"
__all__ = ("FEUserSettings",)


Self = TypeVar("Self", bound="FEUserSettings")


class FEUserSettings(_1594.PerMachineSettings):
    """FEUserSettings

    This is a mastapy class.
    """

    TYPE = _FE_USER_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEUserSettings")

    class _Cast_FEUserSettings:
        """Special nested class for casting FEUserSettings to subclasses."""

        def __init__(
            self: "FEUserSettings._Cast_FEUserSettings", parent: "FEUserSettings"
        ):
            self._parent = parent

        @property
        def per_machine_settings(self: "FEUserSettings._Cast_FEUserSettings"):
            return self._parent._cast(_1594.PerMachineSettings)

        @property
        def persistent_singleton(self: "FEUserSettings._Cast_FEUserSettings"):
            from mastapy.utility import _1595

            return self._parent._cast(_1595.PersistentSingleton)

        @property
        def fe_user_settings(
            self: "FEUserSettings._Cast_FEUserSettings",
        ) -> "FEUserSettings":
            return self._parent

        def __getattr__(self: "FEUserSettings._Cast_FEUserSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEUserSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FEUserSettings._Cast_FEUserSettings":
        return self._Cast_FEUserSettings(self)
