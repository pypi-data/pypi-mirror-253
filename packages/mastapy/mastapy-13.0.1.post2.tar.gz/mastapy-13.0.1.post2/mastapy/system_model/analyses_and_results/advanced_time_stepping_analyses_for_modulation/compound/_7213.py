"""KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7207,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7084,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7207.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7207.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7084.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7084.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
