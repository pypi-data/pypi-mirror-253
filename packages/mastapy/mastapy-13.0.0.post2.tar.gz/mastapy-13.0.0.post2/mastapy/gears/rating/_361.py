"""GearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearRating")

if TYPE_CHECKING:
    from mastapy.materials import _280
    from mastapy.gears.rating import _356


__docformat__ = "restructuredtext en"
__all__ = ("GearRating",)


Self = TypeVar("Self", bound="GearRating")


class GearRating(_354.AbstractGearRating):
    """GearRating

    This is a mastapy class.
    """

    TYPE = _GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearRating")

    class _Cast_GearRating:
        """Special nested class for casting GearRating to subclasses."""

        def __init__(self: "GearRating._Cast_GearRating", parent: "GearRating"):
            self._parent = parent

        @property
        def abstract_gear_rating(self: "GearRating._Cast_GearRating"):
            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.zerol_bevel import _370

            return self._parent._cast(_370.ZerolBevelGearRating)

        @property
        def worm_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.worm import _374

            return self._parent._cast(_374.WormGearRating)

        @property
        def straight_bevel_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.straight_bevel import _396

            return self._parent._cast(_396.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.straight_bevel_diff import _399

            return self._parent._cast(_399.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.spiral_bevel import _403

            return self._parent._cast(_403.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _406

            return self._parent._cast(
                _406.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "GearRating._Cast_GearRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _409

            return self._parent._cast(_409.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.hypoid import _439

            return self._parent._cast(_439.HypoidGearRating)

        @property
        def face_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.face import _448

            return self._parent._cast(_448.FaceGearRating)

        @property
        def cylindrical_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.cylindrical import _460

            return self._parent._cast(_460.CylindricalGearRating)

        @property
        def conical_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearRating)

        @property
        def concept_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.concept import _551

            return self._parent._cast(_551.ConceptGearRating)

        @property
        def bevel_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.bevel import _555

            return self._parent._cast(_555.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self: "GearRating._Cast_GearRating"):
            from mastapy.gears.rating.agma_gleason_conical import _566

            return self._parent._cast(_566.AGMAGleasonConicalGearRating)

        @property
        def gear_rating(self: "GearRating._Cast_GearRating") -> "GearRating":
            return self._parent

        def __getattr__(self: "GearRating._Cast_GearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_results(self: Self) -> "_280.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_safety_factor_results(self: Self) -> "_280.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factor(self: Self) -> "_356.BendingAndContactReportingObject":
        """mastapy.gears.rating.BendingAndContactReportingObject

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearRating._Cast_GearRating":
        return self._Cast_GearRating(self)
