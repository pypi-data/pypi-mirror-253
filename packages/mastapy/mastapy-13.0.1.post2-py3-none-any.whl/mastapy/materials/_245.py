"""BearingMaterial"""
from __future__ import annotations

from typing import TypeVar

from mastapy.materials import _269
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_MATERIAL = python_net_import("SMT.MastaAPI.Materials", "BearingMaterial")


__docformat__ = "restructuredtext en"
__all__ = ("BearingMaterial",)


Self = TypeVar("Self", bound="BearingMaterial")


class BearingMaterial(_269.Material):
    """BearingMaterial

    This is a mastapy class.
    """

    TYPE = _BEARING_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingMaterial")

    class _Cast_BearingMaterial:
        """Special nested class for casting BearingMaterial to subclasses."""

        def __init__(
            self: "BearingMaterial._Cast_BearingMaterial", parent: "BearingMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "BearingMaterial._Cast_BearingMaterial"):
            return self._parent._cast(_269.Material)

        @property
        def named_database_item(self: "BearingMaterial._Cast_BearingMaterial"):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def bearing_material(
            self: "BearingMaterial._Cast_BearingMaterial",
        ) -> "BearingMaterial":
            return self._parent

        def __getattr__(self: "BearingMaterial._Cast_BearingMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BearingMaterial._Cast_BearingMaterial":
        return self._Cast_BearingMaterial(self)
