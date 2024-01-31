"""BevelGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="BevelGearSetParametricStudyTool")


class BevelGearSetParametricStudyTool(
    _4302.AGMAGleasonConicalGearSetParametricStudyTool
):
    """BevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetParametricStudyTool")

    class _Cast_BevelGearSetParametricStudyTool:
        """Special nested class for casting BevelGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
            parent: "BevelGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            return self._parent._cast(
                _4302.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelDifferentialGearSetParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.ZerolBevelGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
        ) -> "BevelGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2520.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetParametricStudyTool._Cast_BevelGearSetParametricStudyTool":
        return self._Cast_BevelGearSetParametricStudyTool(self)
