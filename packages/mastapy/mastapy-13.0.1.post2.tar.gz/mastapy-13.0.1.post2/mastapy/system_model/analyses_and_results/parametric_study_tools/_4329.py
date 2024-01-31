"""ConicalGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearParametricStudyTool")


class ConicalGearParametricStudyTool(_4362.GearParametricStudyTool):
    """ConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearParametricStudyTool")

    class _Cast_ConicalGearParametricStudyTool:
        """Special nested class for casting ConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
            parent: "ConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.StraightBevelSunGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.ZerolBevelGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "ConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool":
        return self._Cast_ConicalGearParametricStudyTool(self)
