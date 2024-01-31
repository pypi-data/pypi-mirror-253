"""AbstractGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _328
    from mastapy.gears.rating import _353, _354


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetRating",)


Self = TypeVar("Self", bound="AbstractGearSetRating")


class AbstractGearSetRating(_1217.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetRating")

    class _Cast_AbstractGearSetRating:
        """Special nested class for casting AbstractGearSetRating to subclasses."""

        def __init__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
            parent: "AbstractGearSetRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.GearSetDutyCycleRating)

        @property
        def gear_set_rating(self: "AbstractGearSetRating._Cast_AbstractGearSetRating"):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _371

            return self._parent._cast(_371.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.worm import _375

            return self._parent._cast(_375.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.worm import _376

            return self._parent._cast(_376.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel import _397

            return self._parent._cast(_397.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _400

            return self._parent._cast(_400.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _404

            return self._parent._cast(_404.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _407

            return self._parent._cast(
                _407.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _410

            return self._parent._cast(_410.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.hypoid import _440

            return self._parent._cast(_440.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.face import _449

            return self._parent._cast(_449.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.face import _450

            return self._parent._cast(_450.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _463

            return self._parent._cast(_463.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _464

            return self._parent._cast(_464.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _480

            return self._parent._cast(_480.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.conical import _541

            return self._parent._cast(_541.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.concept import _552

            return self._parent._cast(_552.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.concept import _553

            return self._parent._cast(_553.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.bevel import _556

            return self._parent._cast(_556.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _567

            return self._parent._cast(_567.AGMAGleasonConicalGearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "AbstractGearSetRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue_and_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigueAndStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def transmission_properties_gears(self: Self) -> "_328.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_353.AbstractGearMeshRating]":
        """List[mastapy.gears.rating.AbstractGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_ratings(self: Self) -> "List[_354.AbstractGearRating]":
        """List[mastapy.gears.rating.AbstractGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "AbstractGearSetRating._Cast_AbstractGearSetRating":
        return self._Cast_AbstractGearSetRating(self)
