"""CylindricalGearMicroGeometrySettingsDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearMicroGeometrySettingsDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometrySettingsDatabase",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometrySettingsDatabase")


class CylindricalGearMicroGeometrySettingsDatabase(
    _1828.NamedDatabase["_1022.CylindricalGearMicroGeometrySettingsItem"]
):
    """CylindricalGearMicroGeometrySettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMicroGeometrySettingsDatabase"
    )

    class _Cast_CylindricalGearMicroGeometrySettingsDatabase:
        """Special nested class for casting CylindricalGearMicroGeometrySettingsDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
            parent: "CylindricalGearMicroGeometrySettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
        ) -> "CylindricalGearMicroGeometrySettingsDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase",
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
        self: Self,
        instance_to_wrap: "CylindricalGearMicroGeometrySettingsDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase":
        return self._Cast_CylindricalGearMicroGeometrySettingsDatabase(self)
