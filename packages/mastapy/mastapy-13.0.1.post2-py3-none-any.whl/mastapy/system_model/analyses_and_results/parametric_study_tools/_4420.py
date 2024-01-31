"""StraightBevelDiffGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "StraightBevelDiffGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.system_deflections import _2815


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelDiffGearParametricStudyTool")


class StraightBevelDiffGearParametricStudyTool(_4313.BevelGearParametricStudyTool):
    """StraightBevelDiffGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearParametricStudyTool"
    )

    class _Cast_StraightBevelDiffGearParametricStudyTool:
        """Special nested class for casting StraightBevelDiffGearParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
            parent: "StraightBevelDiffGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.StraightBevelSunGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
        ) -> "StraightBevelDiffGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "List[_2815.StraightBevelDiffGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection]

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
    ) -> "StraightBevelDiffGearParametricStudyTool._Cast_StraightBevelDiffGearParametricStudyTool":
        return self._Cast_StraightBevelDiffGearParametricStudyTool(self)
