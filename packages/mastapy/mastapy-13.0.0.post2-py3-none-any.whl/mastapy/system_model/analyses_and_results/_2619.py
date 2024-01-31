"""CompoundAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _7552
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7558
    from mastapy.system_model import _2203
    from mastapy.system_model.analyses_and_results.analysis_cases import _7542


__docformat__ = "restructuredtext en"
__all__ = ("CompoundAnalysis",)


Self = TypeVar("Self", bound="CompoundAnalysis")


class CompoundAnalysis(_7552.MarshalByRefObjectPermanent):
    """CompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundAnalysis")

    class _Cast_CompoundAnalysis:
        """Special nested class for casting CompoundAnalysis to subclasses."""

        def __init__(
            self: "CompoundAnalysis._Cast_CompoundAnalysis", parent: "CompoundAnalysis"
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_system_deflection_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.CompoundAdvancedSystemDeflectionAnalysis)

        @property
        def compound_advanced_system_deflection_sub_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.CompoundAdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_advanced_time_stepping_analysis_for_modulation(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2660

            return self._parent._cast(
                _2660.CompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def compound_critical_speed_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.CompoundCriticalSpeedAnalysis)

        @property
        def compound_dynamic_analysis(self: "CompoundAnalysis._Cast_CompoundAnalysis"):
            from mastapy.system_model.analyses_and_results import _2662

            return self._parent._cast(_2662.CompoundDynamicAnalysis)

        @property
        def compound_dynamic_model_at_a_stiffness_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2663

            return self._parent._cast(_2663.CompoundDynamicModelAtAStiffnessAnalysis)

        @property
        def compound_dynamic_model_for_harmonic_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2664

            return self._parent._cast(_2664.CompoundDynamicModelForHarmonicAnalysis)

        @property
        def compound_dynamic_model_for_modal_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.CompoundDynamicModelForModalAnalysis)

        @property
        def compound_dynamic_model_for_stability_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2666

            return self._parent._cast(_2666.CompoundDynamicModelForStabilityAnalysis)

        @property
        def compound_dynamic_model_for_steady_state_synchronous_response_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2667

            return self._parent._cast(
                _2667.CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
            )

        @property
        def compound_harmonic_analysis(self: "CompoundAnalysis._Cast_CompoundAnalysis"):
            from mastapy.system_model.analyses_and_results import _2668

            return self._parent._cast(_2668.CompoundHarmonicAnalysis)

        @property
        def compound_harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2669

            return self._parent._cast(
                _2669.CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def compound_harmonic_analysis_of_single_excitation_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(
                _2670.CompoundHarmonicAnalysisOfSingleExcitationAnalysis
            )

        @property
        def compound_modal_analysis(self: "CompoundAnalysis._Cast_CompoundAnalysis"):
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.CompoundModalAnalysis)

        @property
        def compound_modal_analysis_at_a_speed(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.CompoundModalAnalysisAtASpeed)

        @property
        def compound_modal_analysis_at_a_stiffness(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2673

            return self._parent._cast(_2673.CompoundModalAnalysisAtAStiffness)

        @property
        def compound_modal_analysis_for_harmonic_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.CompoundModalAnalysisForHarmonicAnalysis)

        @property
        def compound_multibody_dynamics_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2675

            return self._parent._cast(_2675.CompoundMultibodyDynamicsAnalysis)

        @property
        def compound_power_flow_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.CompoundPowerFlowAnalysis)

        @property
        def compound_stability_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2677

            return self._parent._cast(_2677.CompoundStabilityAnalysis)

        @property
        def compound_steady_state_synchronous_response_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(
                _2678.CompoundSteadyStateSynchronousResponseAnalysis
            )

        @property
        def compound_steady_state_synchronous_response_at_a_speed_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2679

            return self._parent._cast(
                _2679.CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
            )

        @property
        def compound_steady_state_synchronous_response_on_a_shaft_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(
                _2680.CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
            )

        @property
        def compound_system_deflection_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2681

            return self._parent._cast(_2681.CompoundSystemDeflectionAnalysis)

        @property
        def compound_torsional_system_deflection_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2682

            return self._parent._cast(_2682.CompoundTorsionalSystemDeflectionAnalysis)

        @property
        def compound_analysis(
            self: "CompoundAnalysis._Cast_CompoundAnalysis",
        ) -> "CompoundAnalysis":
            return self._parent

        def __getattr__(self: "CompoundAnalysis._Cast_CompoundAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @enforce_parameter_types
    def perform_analysis_with_progress(self: Self, progress: "_7558.TaskProgress"):
        """Method does not return.

        Args:
            progress (mastapy.TaskProgress)
        """
        self.wrapped.PerformAnalysis.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2203.DesignEntity"
    ) -> "Iterable[_7542.DesignEntityCompoundAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.analysis_cases.DesignEntityCompoundAnalysis]

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        )

    @property
    def cast_to(self: Self) -> "CompoundAnalysis._Cast_CompoundAnalysis":
        return self._Cast_CompoundAnalysis(self)
