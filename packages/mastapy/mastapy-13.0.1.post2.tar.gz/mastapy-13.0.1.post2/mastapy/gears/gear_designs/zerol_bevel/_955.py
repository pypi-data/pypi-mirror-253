"""ZerolBevelMeshedGearDesign"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.bevel import _1183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelMeshedGearDesign"
)


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelMeshedGearDesign",)


Self = TypeVar("Self", bound="ZerolBevelMeshedGearDesign")


class ZerolBevelMeshedGearDesign(_1183.BevelMeshedGearDesign):
    """ZerolBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelMeshedGearDesign")

    class _Cast_ZerolBevelMeshedGearDesign:
        """Special nested class for casting ZerolBevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
            parent: "ZerolBevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ):
            return self._parent._cast(_1183.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1196

            return self._parent._cast(_1196.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.conical import _1159

            return self._parent._cast(_1159.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "ZerolBevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign":
        return self._Cast_ZerolBevelMeshedGearDesign(self)
