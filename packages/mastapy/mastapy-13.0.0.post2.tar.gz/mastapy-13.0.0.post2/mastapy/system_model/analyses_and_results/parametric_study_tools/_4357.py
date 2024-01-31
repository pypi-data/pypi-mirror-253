"""FaceGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "FaceGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.system_deflections import _2755
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4356,
        _4355,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="FaceGearSetParametricStudyTool")


class FaceGearSetParametricStudyTool(_4362.GearSetParametricStudyTool):
    """FaceGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetParametricStudyTool")

    class _Cast_FaceGearSetParametricStudyTool:
        """Special nested class for casting FaceGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
            parent: "FaceGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_set_parametric_study_tool(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4362.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_parametric_study_tool(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
        ) -> "FaceGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetParametricStudyTool.TYPE"):
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
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2755.FaceGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4356.FaceGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4355.FaceGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetParametricStudyTool._Cast_FaceGearSetParametricStudyTool":
        return self._Cast_FaceGearSetParametricStudyTool(self)
