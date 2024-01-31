"""CADExportSettings"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_EXPORT_SETTINGS = python_net_import(
    "SMT.MastaAPI.Utility.CadExport", "CADExportSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("CADExportSettings",)


Self = TypeVar("Self", bound="CADExportSettings")


class CADExportSettings(_1594.PerMachineSettings):
    """CADExportSettings

    This is a mastapy class.
    """

    TYPE = _CAD_EXPORT_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADExportSettings")

    class _Cast_CADExportSettings:
        """Special nested class for casting CADExportSettings to subclasses."""

        def __init__(
            self: "CADExportSettings._Cast_CADExportSettings",
            parent: "CADExportSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(self: "CADExportSettings._Cast_CADExportSettings"):
            return self._parent._cast(_1594.PerMachineSettings)

        @property
        def persistent_singleton(self: "CADExportSettings._Cast_CADExportSettings"):
            from mastapy.utility import _1595

            return self._parent._cast(_1595.PersistentSingleton)

        @property
        def cad_export_settings(
            self: "CADExportSettings._Cast_CADExportSettings",
        ) -> "CADExportSettings":
            return self._parent

        def __getattr__(self: "CADExportSettings._Cast_CADExportSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADExportSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CADExportSettings._Cast_CADExportSettings":
        return self._Cast_CADExportSettings(self)
