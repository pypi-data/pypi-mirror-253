"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6743,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6747,
        _6748,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis(
    _6743.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6747.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundCriticalSpeedAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6748.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundCriticalSpeedAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis(
            self
        )
