"""CycloidalDiscMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.materials import _270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMaterialDatabase",)


Self = TypeVar("Self", bound="CycloidalDiscMaterialDatabase")


class CycloidalDiscMaterialDatabase(
    _270.MaterialDatabase["_1455.CycloidalDiscMaterial"]
):
    """CycloidalDiscMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscMaterialDatabase")

    class _Cast_CycloidalDiscMaterialDatabase:
        """Special nested class for casting CycloidalDiscMaterialDatabase to subclasses."""

        def __init__(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
            parent: "CycloidalDiscMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ):
            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cycloidal_disc_material_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "CycloidalDiscMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase":
        return self._Cast_CycloidalDiscMaterialDatabase(self)
