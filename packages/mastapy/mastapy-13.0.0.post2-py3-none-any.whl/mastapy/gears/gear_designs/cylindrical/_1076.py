"""StandardRack"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1008
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_RACK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "StandardRack"
)


__docformat__ = "restructuredtext en"
__all__ = ("StandardRack",)


Self = TypeVar("Self", bound="StandardRack")


class StandardRack(_1008.CylindricalGearBasicRack):
    """StandardRack

    This is a mastapy class.
    """

    TYPE = _STANDARD_RACK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StandardRack")

    class _Cast_StandardRack:
        """Special nested class for casting StandardRack to subclasses."""

        def __init__(self: "StandardRack._Cast_StandardRack", parent: "StandardRack"):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack(self: "StandardRack._Cast_StandardRack"):
            return self._parent._cast(_1008.CylindricalGearBasicRack)

        @property
        def cylindrical_gear_abstract_rack(self: "StandardRack._Cast_StandardRack"):
            from mastapy.gears.gear_designs.cylindrical import _1006

            return self._parent._cast(_1006.CylindricalGearAbstractRack)

        @property
        def standard_rack(self: "StandardRack._Cast_StandardRack") -> "StandardRack":
            return self._parent

        def __getattr__(self: "StandardRack._Cast_StandardRack", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StandardRack.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StandardRack._Cast_StandardRack":
        return self._Cast_StandardRack(self)
