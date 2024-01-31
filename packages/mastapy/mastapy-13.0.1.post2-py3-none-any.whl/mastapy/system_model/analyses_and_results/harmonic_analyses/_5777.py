"""KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.system_deflections import _2769


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis")


class KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis(
    _5714.ConicalGearSetHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5714.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2769.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis(self)
