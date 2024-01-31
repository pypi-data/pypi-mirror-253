"""ConicalGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConicalGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundDynamicAnalysis")


class ConicalGearSetCompoundDynamicAnalysis(_6468.GearSetCompoundDynamicAnalysis):
    """ConicalGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundDynamicAnalysis"
    )

    class _Cast_ConicalGearSetCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
            parent: "ConicalGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
        ) -> "ConicalGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6311.ConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis]

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
    ) -> "List[_6311.ConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis]

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
    ) -> "ConicalGearSetCompoundDynamicAnalysis._Cast_ConicalGearSetCompoundDynamicAnalysis":
        return self._Cast_ConicalGearSetCompoundDynamicAnalysis(self)
