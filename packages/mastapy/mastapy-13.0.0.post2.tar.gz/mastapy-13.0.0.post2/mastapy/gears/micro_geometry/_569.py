"""BiasModification"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.micro_geometry import _579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BIAS_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "BiasModification"
)


__docformat__ = "restructuredtext en"
__all__ = ("BiasModification",)


Self = TypeVar("Self", bound="BiasModification")


class BiasModification(_579.Modification):
    """BiasModification

    This is a mastapy class.
    """

    TYPE = _BIAS_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BiasModification")

    class _Cast_BiasModification:
        """Special nested class for casting BiasModification to subclasses."""

        def __init__(
            self: "BiasModification._Cast_BiasModification", parent: "BiasModification"
        ):
            self._parent = parent

        @property
        def modification(self: "BiasModification._Cast_BiasModification"):
            return self._parent._cast(_579.Modification)

        @property
        def cylindrical_gear_bias_modification(
            self: "BiasModification._Cast_BiasModification",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093

            return self._parent._cast(_1093.CylindricalGearBiasModification)

        @property
        def conical_gear_bias_modification(
            self: "BiasModification._Cast_BiasModification",
        ):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1172

            return self._parent._cast(_1172.ConicalGearBiasModification)

        @property
        def bias_modification(
            self: "BiasModification._Cast_BiasModification",
        ) -> "BiasModification":
            return self._parent

        def __getattr__(self: "BiasModification._Cast_BiasModification", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BiasModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_evaluation_left_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationLeftLimitFactor

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_left_limit_factor.setter
    @enforce_parameter_types
    def lead_evaluation_left_limit_factor(self: Self, value: "float"):
        self.wrapped.LeadEvaluationLeftLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_evaluation_right_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationRightLimitFactor

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_right_limit_factor.setter
    @enforce_parameter_types
    def lead_evaluation_right_limit_factor(self: Self, value: "float"):
        self.wrapped.LeadEvaluationRightLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitFactor

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_factor.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_factor(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitFactor

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_factor.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_factor(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_factor_for_0_bias_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileFactorFor0BiasRelief

        if temp is None:
            return 0.0

        return temp

    @profile_factor_for_0_bias_relief.setter
    @enforce_parameter_types
    def profile_factor_for_0_bias_relief(self: Self, value: "float"):
        self.wrapped.ProfileFactorFor0BiasRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief_at_left_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtLeftLimit

        if temp is None:
            return 0.0

        return temp

    @relief_at_left_limit.setter
    @enforce_parameter_types
    def relief_at_left_limit(self: Self, value: "float"):
        self.wrapped.ReliefAtLeftLimit = float(value) if value is not None else 0.0

    @property
    def relief_at_right_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReliefAtRightLimit

        if temp is None:
            return 0.0

        return temp

    @relief_at_right_limit.setter
    @enforce_parameter_types
    def relief_at_right_limit(self: Self, value: "float"):
        self.wrapped.ReliefAtRightLimit = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "BiasModification._Cast_BiasModification":
        return self._Cast_BiasModification(self)
