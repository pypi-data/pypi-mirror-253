"""SpiralBevelGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6426
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpiralBevelGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6507,
        _6508,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundDynamicAnalysis")


class SpiralBevelGearSetCompoundDynamicAnalysis(
    _6426.BevelGearSetCompoundDynamicAnalysis
):
    """SpiralBevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundDynamicAnalysis"
    )

    class _Cast_SpiralBevelGearSetCompoundDynamicAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
            parent: "SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "SpiralBevelGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

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
    ) -> "List[_6380.SpiralBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis]

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
    def spiral_bevel_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6507.SpiralBevelGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6508.SpiralBevelGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6380.SpiralBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis]

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
    ) -> "SpiralBevelGearSetCompoundDynamicAnalysis._Cast_SpiralBevelGearSetCompoundDynamicAnalysis":
        return self._Cast_SpiralBevelGearSetCompoundDynamicAnalysis(self)
