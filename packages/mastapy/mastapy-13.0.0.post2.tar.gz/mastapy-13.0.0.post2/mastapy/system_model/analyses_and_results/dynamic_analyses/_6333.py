"""FaceGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "FaceGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331, _6332


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetDynamicAnalysis")


class FaceGearSetDynamicAnalysis(_6338.GearSetDynamicAnalysis):
    """FaceGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetDynamicAnalysis")

    class _Cast_FaceGearSetDynamicAnalysis:
        """Special nested class for casting FaceGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
            parent: "FaceGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_dynamic_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6338.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
        ) -> "FaceGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6886.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6331.FaceGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6332.FaceGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetDynamicAnalysis._Cast_FaceGearSetDynamicAnalysis":
        return self._Cast_FaceGearSetDynamicAnalysis(self)
