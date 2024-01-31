"""StraightBevelPlanetGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "StraightBevelPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearParametricStudyTool")


class StraightBevelPlanetGearParametricStudyTool(
    _4420.StraightBevelDiffGearParametricStudyTool
):
    """StraightBevelPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearParametricStudyTool"
    )

    class _Cast_StraightBevelPlanetGearParametricStudyTool:
        """Special nested class for casting StraightBevelPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
            parent: "StraightBevelPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            return self._parent._cast(_4420.StraightBevelDiffGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
        ) -> "StraightBevelPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearParametricStudyTool._Cast_StraightBevelPlanetGearParametricStudyTool":
        return self._Cast_StraightBevelPlanetGearParametricStudyTool(self)
