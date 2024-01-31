"""RingPinsMaterial"""
from __future__ import annotations

from typing import TypeVar

from mastapy.materials import _269
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MATERIAL = python_net_import("SMT.MastaAPI.Cycloidal", "RingPinsMaterial")


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsMaterial",)


Self = TypeVar("Self", bound="RingPinsMaterial")


class RingPinsMaterial(_269.Material):
    """RingPinsMaterial

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsMaterial")

    class _Cast_RingPinsMaterial:
        """Special nested class for casting RingPinsMaterial to subclasses."""

        def __init__(
            self: "RingPinsMaterial._Cast_RingPinsMaterial", parent: "RingPinsMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "RingPinsMaterial._Cast_RingPinsMaterial"):
            return self._parent._cast(_269.Material)

        @property
        def named_database_item(self: "RingPinsMaterial._Cast_RingPinsMaterial"):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def ring_pins_material(
            self: "RingPinsMaterial._Cast_RingPinsMaterial",
        ) -> "RingPinsMaterial":
            return self._parent

        def __getattr__(self: "RingPinsMaterial._Cast_RingPinsMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RingPinsMaterial._Cast_RingPinsMaterial":
        return self._Cast_RingPinsMaterial(self)
