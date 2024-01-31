"""BevelGearISOMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.materials import _584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ISO_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearISOMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearISOMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearISOMaterialDatabase")


class BevelGearISOMaterialDatabase(
    _584.BevelGearAbstractMaterialDatabase["_585.BevelGearISOMaterial"]
):
    """BevelGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ISO_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearISOMaterialDatabase")

    class _Cast_BevelGearISOMaterialDatabase:
        """Special nested class for casting BevelGearISOMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
            parent: "BevelGearISOMaterialDatabase",
        ):
            self._parent = parent

        @property
        def bevel_gear_abstract_material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ):
            return self._parent._cast(_584.BevelGearAbstractMaterialDatabase)

        @property
        def material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ):
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def bevel_gear_iso_material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "BevelGearISOMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearISOMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase":
        return self._Cast_BevelGearISOMaterialDatabase(self)
