"""SpiralBevelGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpiralBevelGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4414,
        _4413,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="SpiralBevelGearSetParametricStudyTool")


class SpiralBevelGearSetParametricStudyTool(_4314.BevelGearSetParametricStudyTool):
    """SpiralBevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetParametricStudyTool"
    )

    class _Cast_SpiralBevelGearSetParametricStudyTool:
        """Special nested class for casting SpiralBevelGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
            parent: "SpiralBevelGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4314.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(
                _4302.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
        ) -> "SpiralBevelGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetParametricStudyTool.TYPE"
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
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2808.SpiralBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection]

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
    def spiral_bevel_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4414.SpiralBevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4413.SpiralBevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetParametricStudyTool._Cast_SpiralBevelGearSetParametricStudyTool":
        return self._Cast_SpiralBevelGearSetParametricStudyTool(self)
