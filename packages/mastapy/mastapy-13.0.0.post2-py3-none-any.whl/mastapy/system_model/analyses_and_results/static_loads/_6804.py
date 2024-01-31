"""StaticLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2478
from mastapy.system_model.analyses_and_results.static_loads import _6803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "StaticLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results import (
        _2646,
        _2641,
        _2621,
        _2632,
        _2640,
        _2624,
        _2643,
        _2635,
        _2625,
        _2642,
        _2623,
        _2629,
        _2683,
        _2620,
    )
    from mastapy.gears import _341
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7274,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5660,
        _5661,
        _5662,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6817


__docformat__ = "restructuredtext en"
__all__ = ("StaticLoadCase",)


Self = TypeVar("Self", bound="StaticLoadCase")


class StaticLoadCase(_6803.LoadCase):
    """StaticLoadCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticLoadCase")

    class _Cast_StaticLoadCase:
        """Special nested class for casting StaticLoadCase to subclasses."""

        def __init__(
            self: "StaticLoadCase._Cast_StaticLoadCase", parent: "StaticLoadCase"
        ):
            self._parent = parent

        @property
        def load_case(self: "StaticLoadCase._Cast_StaticLoadCase"):
            return self._parent._cast(_6803.LoadCase)

        @property
        def context(self: "StaticLoadCase._Cast_StaticLoadCase"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def parametric_study_static_load(self: "StaticLoadCase._Cast_StaticLoadCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.ParametricStudyStaticLoad)

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "StaticLoadCase._Cast_StaticLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(
                _5769.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
            )

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "StaticLoadCase._Cast_StaticLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(
                _6811.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
            )

        @property
        def static_load_case(
            self: "StaticLoadCase._Cast_StaticLoadCase",
        ) -> "StaticLoadCase":
            return self._parent

        def __getattr__(self: "StaticLoadCase._Cast_StaticLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def system_deflection(self: Self) -> "_2646.SystemDeflectionAnalysis":
        """mastapy.system_model.analyses_and_results.SystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_2641.PowerFlowAnalysis":
        """mastapy.system_model.analyses_and_results.PowerFlowAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def advanced_system_deflection(
        self: Self,
    ) -> "_2621.AdvancedSystemDeflectionAnalysis":
        """mastapy.system_model.analyses_and_results.AdvancedSystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis(self: Self) -> "_2632.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool(self: Self) -> "_2640.ParametricStudyToolAnalysis":
        """mastapy.system_model.analyses_and_results.ParametricStudyToolAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_parametric_study_tool(
        self: Self,
    ) -> "_2624.CompoundParametricStudyToolAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundParametricStudyToolAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response(
        self: Self,
    ) -> "_2643.SteadyStateSynchronousResponseAnalysis":
        """mastapy.system_model.analyses_and_results.SteadyStateSynchronousResponseAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis(self: Self) -> "_2635.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis(self: Self) -> "_2625.CriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.CriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis(self: Self) -> "_2642.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "_2623.AdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.AdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_model_for_modal_analysis(
        self: Self,
    ) -> "_2629.DynamicModelForModalAnalysis":
        """mastapy.system_model.analyses_and_results.DynamicModelForModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def current_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    @enforce_parameter_types
    def current_time(self: Self, value: "float"):
        self.wrapped.CurrentTime = float(value) if value is not None else 0.0

    @property
    def design_state(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignState

        if temp is None:
            return ""

        return temp

    @property
    def duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    @enforce_parameter_types
    def duration(self: Self, value: "float"):
        self.wrapped.Duration = float(value) if value is not None else 0.0

    @property
    def input_shaft_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InputShaftCycles

        if temp is None:
            return 0.0

        return temp

    @input_shaft_cycles.setter
    @enforce_parameter_types
    def input_shaft_cycles(self: Self, value: "float"):
        self.wrapped.InputShaftCycles = float(value) if value is not None else 0.0

    @property
    def is_stop_start_load_case(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsStopStartLoadCase

        if temp is None:
            return False

        return temp

    @is_stop_start_load_case.setter
    @enforce_parameter_types
    def is_stop_start_load_case(self: Self, value: "bool"):
        self.wrapped.IsStopStartLoadCase = bool(value) if value is not None else False

    @property
    def number_of_stop_start_cycles(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStopStartCycles

        if temp is None:
            return 0

        return temp

    @number_of_stop_start_cycles.setter
    @enforce_parameter_types
    def number_of_stop_start_cycles(self: Self, value: "int"):
        self.wrapped.NumberOfStopStartCycles = int(value) if value is not None else 0

    @property
    def percentage_of_shaft_torque_alternating(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageOfShaftTorqueAlternating

        if temp is None:
            return 0.0

        return temp

    @percentage_of_shaft_torque_alternating.setter
    @enforce_parameter_types
    def percentage_of_shaft_torque_alternating(self: Self, value: "float"):
        self.wrapped.PercentageOfShaftTorqueAlternating = (
            float(value) if value is not None else 0.0
        )

    @property
    def planetary_rating_load_sharing_method(
        self: Self,
    ) -> "_341.PlanetaryRatingLoadSharingOption":
        """mastapy.gears.PlanetaryRatingLoadSharingOption"""
        temp = self.wrapped.PlanetaryRatingLoadSharingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._341", "PlanetaryRatingLoadSharingOption"
        )(value)

    @planetary_rating_load_sharing_method.setter
    @enforce_parameter_types
    def planetary_rating_load_sharing_method(
        self: Self, value: "_341.PlanetaryRatingLoadSharingOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption"
        )
        self.wrapped.PlanetaryRatingLoadSharingMethod = value

    @property
    def power_convergence_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PowerConvergenceTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @power_convergence_tolerance.setter
    @enforce_parameter_types
    def power_convergence_tolerance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PowerConvergenceTolerance = value

    @property
    def unbalanced_mass_inclusion(
        self: Self,
    ) -> "overridable.Overridable_UnbalancedMassInclusionOption":
        """Overridable[mastapy.system_model.part_model.UnbalancedMassInclusionOption]"""
        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = overridable.Overridable_UnbalancedMassInclusionOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @unbalanced_mass_inclusion.setter
    @enforce_parameter_types
    def unbalanced_mass_inclusion(
        self: Self,
        value: "Union[_2478.UnbalancedMassInclusionOption, Tuple[_2478.UnbalancedMassInclusionOption, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_UnbalancedMassInclusionOption.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def advanced_system_deflection_options(
        self: Self,
    ) -> "_7274.AdvancedSystemDeflectionOptions":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflectionOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflectionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5765.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options_for_atsam(
        self: Self,
    ) -> "_5765.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptionsForATSAM

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def te_set_up_for_dynamic_analyses_options(
        self: Self,
    ) -> "_2683.TESetUpForDynamicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.TESetUpForDynamicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TESetUpForDynamicAnalysesOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clutch_engagements(self: Self) -> "List[_5660.ClutchEngagementStatus]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.ClutchEngagementStatus]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_clutch_engagements(
        self: Self,
    ) -> "List[_5661.ConceptSynchroGearEngagementStatus]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.ConceptSynchroGearEngagementStatus]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def design_state_load_case_group(self: Self) -> "_5662.DesignState":
        """mastapy.system_model.analyses_and_results.load_case_groups.DesignState

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStateLoadCaseGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_of(
        self: Self, analysis_type: "_6817.AnalysisType"
    ) -> "_2620.SingleAnalysis":
        """mastapy.system_model.analyses_and_results.SingleAnalysis

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_time_series_load_case(self: Self):
        """Method does not return."""
        self.wrapped.CreateTimeSeriesLoadCase()

    def run_power_flow(self: Self):
        """Method does not return."""
        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    @enforce_parameter_types
    def duplicate(
        self: Self, new_design_state_group: "_5662.DesignState", name: "str" = "None"
    ) -> "StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Args:
            new_design_state_group (mastapy.system_model.analyses_and_results.load_case_groups.DesignState)
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.Duplicate(
            new_design_state_group.wrapped if new_design_state_group else None,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "StaticLoadCase._Cast_StaticLoadCase":
        return self._Cast_StaticLoadCase(self)
