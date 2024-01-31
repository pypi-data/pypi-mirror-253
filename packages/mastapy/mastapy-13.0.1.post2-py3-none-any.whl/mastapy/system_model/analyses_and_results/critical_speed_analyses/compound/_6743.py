"""KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6709,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis(
    _6709.ConicalGearSetCompoundCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6709.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis(
            self
        )
