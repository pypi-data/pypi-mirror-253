"""RawMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RAW_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "RawMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("RawMaterialDatabase",)


Self = TypeVar("Self", bound="RawMaterialDatabase")


class RawMaterialDatabase(_1828.NamedDatabase["_606.RawMaterial"]):
    """RawMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _RAW_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RawMaterialDatabase")

    class _Cast_RawMaterialDatabase:
        """Special nested class for casting RawMaterialDatabase to subclasses."""

        def __init__(
            self: "RawMaterialDatabase._Cast_RawMaterialDatabase",
            parent: "RawMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(self: "RawMaterialDatabase._Cast_RawMaterialDatabase"):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(self: "RawMaterialDatabase._Cast_RawMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "RawMaterialDatabase._Cast_RawMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def raw_material_database(
            self: "RawMaterialDatabase._Cast_RawMaterialDatabase",
        ) -> "RawMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "RawMaterialDatabase._Cast_RawMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RawMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RawMaterialDatabase._Cast_RawMaterialDatabase":
        return self._Cast_RawMaterialDatabase(self)
