"""ConceptGearDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _359


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearDutyCycleRating",)


Self = TypeVar("Self", bound="ConceptGearDutyCycleRating")


class ConceptGearDutyCycleRating(_358.GearDutyCycleRating):
    """ConceptGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearDutyCycleRating")

    class _Cast_ConceptGearDutyCycleRating:
        """Special nested class for casting ConceptGearDutyCycleRating to subclasses."""

        def __init__(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
            parent: "ConceptGearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
        ):
            return self._parent._cast(_358.GearDutyCycleRating)

        @property
        def abstract_gear_rating(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
        ):
            from mastapy.gears.rating import _354

            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def concept_gear_duty_cycle_rating(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
        ) -> "ConceptGearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self: Self) -> "_359.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_359.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating":
        return self._Cast_ConceptGearDutyCycleRating(self)
