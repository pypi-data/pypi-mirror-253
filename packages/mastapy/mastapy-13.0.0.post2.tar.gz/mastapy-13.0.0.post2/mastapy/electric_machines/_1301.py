"""StatorRotorMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.materials import _270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "StatorRotorMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("StatorRotorMaterialDatabase",)


Self = TypeVar("Self", bound="StatorRotorMaterialDatabase")


class StatorRotorMaterialDatabase(_270.MaterialDatabase["_1300.StatorRotorMaterial"]):
    """StatorRotorMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorRotorMaterialDatabase")

    class _Cast_StatorRotorMaterialDatabase:
        """Special nested class for casting StatorRotorMaterialDatabase to subclasses."""

        def __init__(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
            parent: "StatorRotorMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ):
            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def stator_rotor_material_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "StatorRotorMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorRotorMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase":
        return self._Cast_StatorRotorMaterialDatabase(self)
