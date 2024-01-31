"""FaceGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "FaceGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.system_deflections import _2755
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5747, _5748


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetHarmonicAnalysis")


class FaceGearSetHarmonicAnalysis(_5758.GearSetHarmonicAnalysis):
    """FaceGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetHarmonicAnalysis")

    class _Cast_FaceGearSetHarmonicAnalysis:
        """Special nested class for casting FaceGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
            parent: "FaceGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5758.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "FaceGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetHarmonicAnalysis.TYPE"):
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
    def assembly_load_case(self: Self) -> "_6887.FaceGearSetLoadCase":
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
    def system_deflection_results(self: Self) -> "_2755.FaceGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(self: Self) -> "List[_5747.FaceGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5747.FaceGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5748.FaceGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5748.FaceGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis":
        return self._Cast_FaceGearSetHarmonicAnalysis(self)
