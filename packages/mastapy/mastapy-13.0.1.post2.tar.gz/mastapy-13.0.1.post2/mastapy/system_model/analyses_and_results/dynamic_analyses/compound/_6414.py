"""AGMAGleasonConicalGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6442
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundDynamicAnalysis")


class AGMAGleasonConicalGearSetCompoundDynamicAnalysis(
    _6442.ConicalGearSetCompoundDynamicAnalysis
):
    """AGMAGleasonConicalGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6283.AGMAGleasonConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis]

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
    ) -> "List[_6283.AGMAGleasonConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundDynamicAnalysis(self)
