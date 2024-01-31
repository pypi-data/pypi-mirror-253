"""CADMagnetsForLayer"""
from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines import _1280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_MAGNETS_FOR_LAYER = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CADMagnetsForLayer"
)


__docformat__ = "restructuredtext en"
__all__ = ("CADMagnetsForLayer",)


Self = TypeVar("Self", bound="CADMagnetsForLayer")


class CADMagnetsForLayer(_1280.MagnetDesign):
    """CADMagnetsForLayer

    This is a mastapy class.
    """

    TYPE = _CAD_MAGNETS_FOR_LAYER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADMagnetsForLayer")

    class _Cast_CADMagnetsForLayer:
        """Special nested class for casting CADMagnetsForLayer to subclasses."""

        def __init__(
            self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer",
            parent: "CADMagnetsForLayer",
        ):
            self._parent = parent

        @property
        def magnet_design(self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer"):
            return self._parent._cast(_1280.MagnetDesign)

        @property
        def cad_magnets_for_layer(
            self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer",
        ) -> "CADMagnetsForLayer":
            return self._parent

        def __getattr__(self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADMagnetsForLayer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CADMagnetsForLayer._Cast_CADMagnetsForLayer":
        return self._Cast_CADMagnetsForLayer(self)
