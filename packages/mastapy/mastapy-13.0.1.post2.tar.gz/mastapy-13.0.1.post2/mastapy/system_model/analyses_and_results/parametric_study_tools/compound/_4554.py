"""StraightBevelPlanetGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4548,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4425


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundParametricStudyTool")


class StraightBevelPlanetGearCompoundParametricStudyTool(
    _4548.StraightBevelDiffGearCompoundParametricStudyTool
):
    """StraightBevelPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundParametricStudyTool"
    )

    class _Cast_StraightBevelPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
            parent: "StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4548.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
        ) -> "StraightBevelPlanetGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "StraightBevelPlanetGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6966.StraightBevelPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4425.StraightBevelPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4425.StraightBevelPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearCompoundParametricStudyTool._Cast_StraightBevelPlanetGearCompoundParametricStudyTool":
        return self._Cast_StraightBevelPlanetGearCompoundParametricStudyTool(self)
