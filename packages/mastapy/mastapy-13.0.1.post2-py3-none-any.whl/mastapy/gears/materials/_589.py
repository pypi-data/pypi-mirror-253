"""CylindricalGearAGMAMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.materials import _592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_AGMA_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearAGMAMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAGMAMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearAGMAMaterialDatabase")


class CylindricalGearAGMAMaterialDatabase(
    _592.CylindricalGearMaterialDatabase["_583.AGMACylindricalGearMaterial"]
):
    """CylindricalGearAGMAMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_AGMA_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearAGMAMaterialDatabase")

    class _Cast_CylindricalGearAGMAMaterialDatabase:
        """Special nested class for casting CylindricalGearAGMAMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
            parent: "CylindricalGearAGMAMaterialDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ):
            return self._parent._cast(_592.CylindricalGearMaterialDatabase)

        @property
        def material_database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ):
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_gear_agma_material_database(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
        ) -> "CylindricalGearAGMAMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearAGMAMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase"
    ):
        return self._Cast_CylindricalGearAGMAMaterialDatabase(self)
