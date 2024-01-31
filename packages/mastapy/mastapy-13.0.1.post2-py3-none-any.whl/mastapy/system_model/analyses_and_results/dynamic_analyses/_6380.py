"""SpiralBevelGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SpiralBevelGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378, _6379


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetDynamicAnalysis")


class SpiralBevelGearSetDynamicAnalysis(_6295.BevelGearSetDynamicAnalysis):
    """SpiralBevelGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetDynamicAnalysis")

    class _Cast_SpiralBevelGearSetDynamicAnalysis:
        """Special nested class for casting SpiralBevelGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
            parent: "SpiralBevelGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6295.BevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
        ) -> "SpiralBevelGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6956.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6378.SpiralBevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6379.SpiralBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetDynamicAnalysis._Cast_SpiralBevelGearSetDynamicAnalysis":
        return self._Cast_SpiralBevelGearSetDynamicAnalysis(self)
