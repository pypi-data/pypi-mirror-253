"""ComponentMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Materials", "ComponentMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("ComponentMaterialDatabase",)


Self = TypeVar("Self", bound="ComponentMaterialDatabase")


class ComponentMaterialDatabase(_1828.NamedDatabase["_269.Material"]):
    """ComponentMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentMaterialDatabase")

    class _Cast_ComponentMaterialDatabase:
        """Special nested class for casting ComponentMaterialDatabase to subclasses."""

        def __init__(
            self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase",
            parent: "ComponentMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def component_material_database(
            self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase",
        ) -> "ComponentMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentMaterialDatabase._Cast_ComponentMaterialDatabase":
        return self._Cast_ComponentMaterialDatabase(self)
