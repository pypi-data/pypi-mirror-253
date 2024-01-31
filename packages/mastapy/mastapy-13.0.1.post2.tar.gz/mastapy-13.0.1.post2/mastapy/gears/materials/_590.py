"""CylindricalGearISOMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.materials import _592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearISOMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearISOMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearISOMaterialDatabase")


class CylindricalGearISOMaterialDatabase(
    _592.CylindricalGearMaterialDatabase["_597.ISOCylindricalGearMaterial"]
):
    """CylindricalGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearISOMaterialDatabase")

    class _Cast_CylindricalGearISOMaterialDatabase:
        """Special nested class for casting CylindricalGearISOMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
            parent: "CylindricalGearISOMaterialDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ):
            return self._parent._cast(_592.CylindricalGearMaterialDatabase)

        @property
        def material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ):
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_gear_iso_material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "CylindricalGearISOMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearISOMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase":
        return self._Cast_CylindricalGearISOMaterialDatabase(self)
