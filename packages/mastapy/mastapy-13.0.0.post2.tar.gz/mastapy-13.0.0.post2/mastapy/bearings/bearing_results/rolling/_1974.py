"""ISO14179Settings"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO14179_SETTINGS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISO14179Settings"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2065
    from mastapy.math_utility.measured_data import _1567, _1568


__docformat__ = "restructuredtext en"
__all__ = ("ISO14179Settings",)


Self = TypeVar("Self", bound="ISO14179Settings")


class ISO14179Settings(_1829.NamedDatabaseItem):
    """ISO14179Settings

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO14179Settings")

    class _Cast_ISO14179Settings:
        """Special nested class for casting ISO14179Settings to subclasses."""

        def __init__(
            self: "ISO14179Settings._Cast_ISO14179Settings", parent: "ISO14179Settings"
        ):
            self._parent = parent

        @property
        def named_database_item(self: "ISO14179Settings._Cast_ISO14179Settings"):
            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def iso14179_settings(
            self: "ISO14179Settings._Cast_ISO14179Settings",
        ) -> "ISO14179Settings":
            return self._parent

        def __getattr__(self: "ISO14179Settings._Cast_ISO14179Settings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO14179Settings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def isotr141792001f1_specification_method(
        self: Self,
    ) -> "_2065.PowerRatingF1EstimationMethod":
        """mastapy.bearings.bearing_results.rolling.PowerRatingF1EstimationMethod"""
        temp = self.wrapped.ISOTR141792001F1SpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.PowerRatingF1EstimationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._2065",
            "PowerRatingF1EstimationMethod",
        )(value)

    @isotr141792001f1_specification_method.setter
    @enforce_parameter_types
    def isotr141792001f1_specification_method(
        self: Self, value: "_2065.PowerRatingF1EstimationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.PowerRatingF1EstimationMethod",
        )
        self.wrapped.ISOTR141792001F1SpecificationMethod = value

    @property
    def user_specified_f1_for_isotr141792001(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedF1ForISOTR141792001

        if temp is None:
            return 0.0

        return temp

    @user_specified_f1_for_isotr141792001.setter
    @enforce_parameter_types
    def user_specified_f1_for_isotr141792001(self: Self, value: "float"):
        self.wrapped.UserSpecifiedF1ForISOTR141792001 = (
            float(value) if value is not None else 0.0
        )

    @property
    def power_rating_f0_scaling_factor_one_dimensional_lookup_table(
        self: Self,
    ) -> "_1567.OnedimensionalFunctionLookupTable":
        """mastapy.math_utility.measured_data.OnedimensionalFunctionLookupTable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF0ScalingFactorOneDimensionalLookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_rating_f1_one_dimensional_lookup_table(
        self: Self,
    ) -> "_1567.OnedimensionalFunctionLookupTable":
        """mastapy.math_utility.measured_data.OnedimensionalFunctionLookupTable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF1OneDimensionalLookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_rating_f1_scaling_factor_one_dimensional_lookup_table(
        self: Self,
    ) -> "_1567.OnedimensionalFunctionLookupTable":
        """mastapy.math_utility.measured_data.OnedimensionalFunctionLookupTable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF1ScalingFactorOneDimensionalLookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_rating_f1_two_dimensional_lookup_table(
        self: Self,
    ) -> "_1568.TwodimensionalFunctionLookupTable":
        """mastapy.math_utility.measured_data.TwodimensionalFunctionLookupTable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerRatingF1TwoDimensionalLookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ISO14179Settings._Cast_ISO14179Settings":
        return self._Cast_ISO14179Settings(self)
