"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2619 import CompoundAnalysis
    from ._2620 import SingleAnalysis
    from ._2621 import AdvancedSystemDeflectionAnalysis
    from ._2622 import AdvancedSystemDeflectionSubAnalysis
    from ._2623 import AdvancedTimeSteppingAnalysisForModulation
    from ._2624 import CompoundParametricStudyToolAnalysis
    from ._2625 import CriticalSpeedAnalysis
    from ._2626 import DynamicAnalysis
    from ._2627 import DynamicModelAtAStiffnessAnalysis
    from ._2628 import DynamicModelForHarmonicAnalysis
    from ._2629 import DynamicModelForModalAnalysis
    from ._2630 import DynamicModelForStabilityAnalysis
    from ._2631 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2632 import HarmonicAnalysis
    from ._2633 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2634 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2635 import ModalAnalysis
    from ._2636 import ModalAnalysisAtASpeed
    from ._2637 import ModalAnalysisAtAStiffness
    from ._2638 import ModalAnalysisForHarmonicAnalysis
    from ._2639 import MultibodyDynamicsAnalysis
    from ._2640 import ParametricStudyToolAnalysis
    from ._2641 import PowerFlowAnalysis
    from ._2642 import StabilityAnalysis
    from ._2643 import SteadyStateSynchronousResponseAnalysis
    from ._2644 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2645 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2646 import SystemDeflectionAnalysis
    from ._2647 import TorsionalSystemDeflectionAnalysis
    from ._2648 import AnalysisCaseVariable
    from ._2649 import ConnectionAnalysis
    from ._2650 import Context
    from ._2651 import DesignEntityAnalysis
    from ._2652 import DesignEntityGroupAnalysis
    from ._2653 import DesignEntitySingleContextAnalysis
    from ._2657 import PartAnalysis
    from ._2658 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2659 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2660 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2661 import CompoundCriticalSpeedAnalysis
    from ._2662 import CompoundDynamicAnalysis
    from ._2663 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2664 import CompoundDynamicModelForHarmonicAnalysis
    from ._2665 import CompoundDynamicModelForModalAnalysis
    from ._2666 import CompoundDynamicModelForStabilityAnalysis
    from ._2667 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2668 import CompoundHarmonicAnalysis
    from ._2669 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2670 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2671 import CompoundModalAnalysis
    from ._2672 import CompoundModalAnalysisAtASpeed
    from ._2673 import CompoundModalAnalysisAtAStiffness
    from ._2674 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2675 import CompoundMultibodyDynamicsAnalysis
    from ._2676 import CompoundPowerFlowAnalysis
    from ._2677 import CompoundStabilityAnalysis
    from ._2678 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2679 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2680 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2681 import CompoundSystemDeflectionAnalysis
    from ._2682 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2683 import TESetUpForDynamicAnalysisOptions
    from ._2684 import TimeOptions
else:
    import_structure = {
        "_2619": ["CompoundAnalysis"],
        "_2620": ["SingleAnalysis"],
        "_2621": ["AdvancedSystemDeflectionAnalysis"],
        "_2622": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2623": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2624": ["CompoundParametricStudyToolAnalysis"],
        "_2625": ["CriticalSpeedAnalysis"],
        "_2626": ["DynamicAnalysis"],
        "_2627": ["DynamicModelAtAStiffnessAnalysis"],
        "_2628": ["DynamicModelForHarmonicAnalysis"],
        "_2629": ["DynamicModelForModalAnalysis"],
        "_2630": ["DynamicModelForStabilityAnalysis"],
        "_2631": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2632": ["HarmonicAnalysis"],
        "_2633": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2634": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2635": ["ModalAnalysis"],
        "_2636": ["ModalAnalysisAtASpeed"],
        "_2637": ["ModalAnalysisAtAStiffness"],
        "_2638": ["ModalAnalysisForHarmonicAnalysis"],
        "_2639": ["MultibodyDynamicsAnalysis"],
        "_2640": ["ParametricStudyToolAnalysis"],
        "_2641": ["PowerFlowAnalysis"],
        "_2642": ["StabilityAnalysis"],
        "_2643": ["SteadyStateSynchronousResponseAnalysis"],
        "_2644": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2645": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2646": ["SystemDeflectionAnalysis"],
        "_2647": ["TorsionalSystemDeflectionAnalysis"],
        "_2648": ["AnalysisCaseVariable"],
        "_2649": ["ConnectionAnalysis"],
        "_2650": ["Context"],
        "_2651": ["DesignEntityAnalysis"],
        "_2652": ["DesignEntityGroupAnalysis"],
        "_2653": ["DesignEntitySingleContextAnalysis"],
        "_2657": ["PartAnalysis"],
        "_2658": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2659": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2660": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2661": ["CompoundCriticalSpeedAnalysis"],
        "_2662": ["CompoundDynamicAnalysis"],
        "_2663": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2664": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2665": ["CompoundDynamicModelForModalAnalysis"],
        "_2666": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2667": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2668": ["CompoundHarmonicAnalysis"],
        "_2669": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2670": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2671": ["CompoundModalAnalysis"],
        "_2672": ["CompoundModalAnalysisAtASpeed"],
        "_2673": ["CompoundModalAnalysisAtAStiffness"],
        "_2674": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2675": ["CompoundMultibodyDynamicsAnalysis"],
        "_2676": ["CompoundPowerFlowAnalysis"],
        "_2677": ["CompoundStabilityAnalysis"],
        "_2678": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2679": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2680": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2681": ["CompoundSystemDeflectionAnalysis"],
        "_2682": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2683": ["TESetUpForDynamicAnalysisOptions"],
        "_2684": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
