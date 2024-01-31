"""DutyCyclePropertySummary"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummary"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1605


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummary",)


Self = TypeVar("Self", bound="DutyCyclePropertySummary")
TMeasurement = TypeVar("TMeasurement", bound="_1605.MeasurementBase")
T = TypeVar("T")


class DutyCyclePropertySummary(_0.APIBase, Generic[TMeasurement, T]):
    """DutyCyclePropertySummary

    This is a mastapy class.

    Generic Types:
        TMeasurement
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCyclePropertySummary")

    class _Cast_DutyCyclePropertySummary:
        """Special nested class for casting DutyCyclePropertySummary to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
            parent: "DutyCyclePropertySummary",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary_force(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ):
            from mastapy.utility.property import _1838

            return self._parent._cast(_1838.DutyCyclePropertySummaryForce)

        @property
        def duty_cycle_property_summary_percentage(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ):
            from mastapy.utility.property import _1839

            return self._parent._cast(_1839.DutyCyclePropertySummaryPercentage)

        @property
        def duty_cycle_property_summary_small_angle(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ):
            from mastapy.utility.property import _1840

            return self._parent._cast(_1840.DutyCyclePropertySummarySmallAngle)

        @property
        def duty_cycle_property_summary_stress(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ):
            from mastapy.utility.property import _1841

            return self._parent._cast(_1841.DutyCyclePropertySummaryStress)

        @property
        def duty_cycle_property_summary_very_short_length(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ):
            from mastapy.utility.property import _1842

            return self._parent._cast(_1842.DutyCyclePropertySummaryVeryShortLength)

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "DutyCyclePropertySummary":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCyclePropertySummary.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAbsoluteValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary":
        return self._Cast_DutyCyclePropertySummary(self)
