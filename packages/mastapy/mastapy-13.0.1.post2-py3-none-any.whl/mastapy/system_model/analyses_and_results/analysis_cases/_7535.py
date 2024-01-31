"""AnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "AnalysisCase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1578
    from mastapy.system_model import _2203
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCase",)


Self = TypeVar("Self", bound="AnalysisCase")


class AnalysisCase(_2650.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisCase")

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self: "AnalysisCase._Cast_AnalysisCase", parent: "AnalysisCase"):
            self._parent = parent

        @property
        def context(self: "AnalysisCase._Cast_AnalysisCase"):
            return self._parent._cast(_2650.Context)

        @property
        def system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.SystemDeflection)

        @property
        def torsional_system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(
                _3035.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(_3089.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(_3350.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(_3609.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.StabilityAnalysis)

        @property
        def power_flow(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PowerFlow)

        @property
        def parametric_study_tool(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4388,
            )

            return self._parent._cast(_4388.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(_5465.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(
                _5765.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.DynamicAnalysis)

        @property
        def critical_speed_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7010,
            )

            return self._parent._cast(_7010.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7274,
            )

            return self._parent._cast(_7274.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(_7276.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.FEAnalysis)

        @property
        def static_load_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self: "AnalysisCase._Cast_AnalysisCase") -> "AnalysisCase":
            return self._parent

        def __getattr__(self: "AnalysisCase._Cast_AnalysisCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def analysis_run_information(self: Self) -> "_1578.AnalysisRunInformation":
        """mastapy.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2203.DesignEntity"
    ) -> "_2651.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self: Self) -> "AnalysisCase._Cast_AnalysisCase":
        return self._Cast_AnalysisCase(self)
