"""BevelDifferentialGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4459,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BevelDifferentialGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.static_loads import _6823
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundParametricStudyTool")


class BevelDifferentialGearCompoundParametricStudyTool(
    _4459.BevelGearCompoundParametricStudyTool
):
    """BevelDifferentialGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundParametricStudyTool"
    )

    class _Cast_BevelDifferentialGearCompoundParametricStudyTool:
        """Special nested class for casting BevelDifferentialGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
            parent: "BevelDifferentialGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4459.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
        ) -> "BevelDifferentialGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool",
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
        instance_to_wrap: "BevelDifferentialGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6823.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "List[_4308.BevelDifferentialGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool]

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
    ) -> "List[_4308.BevelDifferentialGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool]

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
    ) -> "BevelDifferentialGearCompoundParametricStudyTool._Cast_BevelDifferentialGearCompoundParametricStudyTool":
        return self._Cast_BevelDifferentialGearCompoundParametricStudyTool(self)
