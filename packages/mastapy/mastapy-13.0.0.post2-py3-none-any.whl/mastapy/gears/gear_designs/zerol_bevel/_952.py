"""ZerolBevelGearDesign"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.bevel import _1180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelGearDesign"
)


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearDesign",)


Self = TypeVar("Self", bound="ZerolBevelGearDesign")


class ZerolBevelGearDesign(_1180.BevelGearDesign):
    """ZerolBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearDesign")

    class _Cast_ZerolBevelGearDesign:
        """Special nested class for casting ZerolBevelGearDesign to subclasses."""

        def __init__(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign",
            parent: "ZerolBevelGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign"):
            return self._parent._cast(_1180.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1193

            return self._parent._cast(_1193.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign",
        ):
            from mastapy.gears.gear_designs.conical import _1154

            return self._parent._cast(_1154.ConicalGearDesign)

        @property
        def gear_design(self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign"):
            from mastapy.gears.gear_designs import _947

            return self._parent._cast(_947.GearDesign)

        @property
        def gear_design_component(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign",
        ) -> "ZerolBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ZerolBevelGearDesign._Cast_ZerolBevelGearDesign":
        return self._Cast_ZerolBevelGearDesign(self)
