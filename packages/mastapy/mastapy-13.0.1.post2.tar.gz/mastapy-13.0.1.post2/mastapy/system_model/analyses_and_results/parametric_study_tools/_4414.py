"""SpiralBevelGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpiralBevelGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2809


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearParametricStudyTool",)


Self = TypeVar("Self", bound="SpiralBevelGearParametricStudyTool")


class SpiralBevelGearParametricStudyTool(_4313.BevelGearParametricStudyTool):
    """SpiralBevelGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearParametricStudyTool")

    class _Cast_SpiralBevelGearParametricStudyTool:
        """Special nested class for casting SpiralBevelGearParametricStudyTool to subclasses."""

        def __init__(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
            parent: "SpiralBevelGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
        ) -> "SpiralBevelGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpiralBevelGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6954.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2809.SpiralBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearParametricStudyTool._Cast_SpiralBevelGearParametricStudyTool":
        return self._Cast_SpiralBevelGearParametricStudyTool(self)
