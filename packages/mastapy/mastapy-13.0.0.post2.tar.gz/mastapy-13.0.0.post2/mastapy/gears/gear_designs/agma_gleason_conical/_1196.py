"""AGMAGleasonConicalMeshedGearDesign"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalMeshedGearDesign",
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalMeshedGearDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalMeshedGearDesign")


class AGMAGleasonConicalMeshedGearDesign(_1159.ConicalMeshedGearDesign):
    """AGMAGleasonConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalMeshedGearDesign")

    class _Cast_AGMAGleasonConicalMeshedGearDesign:
        """Special nested class for casting AGMAGleasonConicalMeshedGearDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
            parent: "AGMAGleasonConicalMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            return self._parent._cast(_1159.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _955

            return self._parent._cast(_955.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _964

            return self._parent._cast(_964.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _968

            return self._parent._cast(_968.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _972

            return self._parent._cast(_972.SpiralBevelMeshedGearDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.hypoid import _988

            return self._parent._cast(_988.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ):
            from mastapy.gears.gear_designs.bevel import _1183

            return self._parent._cast(_1183.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "AGMAGleasonConicalMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "AGMAGleasonConicalMeshedGearDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_topland_to_module_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumToplandToModuleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def required_mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredMeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign":
        return self._Cast_AGMAGleasonConicalMeshedGearDesign(self)
