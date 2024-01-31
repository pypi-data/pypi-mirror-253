"""ToothFlankFractureAnalysisSettings"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility import _1586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ToothFlankFractureAnalysisSettings"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1534


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisSettings",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisSettings")


class ToothFlankFractureAnalysisSettings(
    _1586.IndependentReportablePropertiesBase["ToothFlankFractureAnalysisSettings"]
):
    """ToothFlankFractureAnalysisSettings

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothFlankFractureAnalysisSettings")

    class _Cast_ToothFlankFractureAnalysisSettings:
        """Special nested class for casting ToothFlankFractureAnalysisSettings to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
            parent: "ToothFlankFractureAnalysisSettings",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
        ):
            pass

            return self._parent._cast(_1586.IndependentReportablePropertiesBase)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
        ) -> "ToothFlankFractureAnalysisSettings":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measured_residual_stress_profile_property(
        self: Self,
    ) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredResidualStressProfileProperty

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_residual_stress_profile_property.setter
    @enforce_parameter_types
    def measured_residual_stress_profile_property(
        self: Self, value: "_1534.Vector2DListAccessor"
    ):
        self.wrapped.MeasuredResidualStressProfileProperty = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings":
        return self._Cast_ToothFlankFractureAnalysisSettings(self)
