"""GearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4520,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _358
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4362


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GearCompoundParametricStudyTool")


class GearCompoundParametricStudyTool(
    _4520.MountableComponentCompoundParametricStudyTool
):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundParametricStudyTool")

    class _Cast_GearCompoundParametricStudyTool:
        """Special nested class for casting GearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            parent: "GearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BevelGearCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConicalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(
                _4493.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def face_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.FaceGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(_4542.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4569,
            )

            return self._parent._cast(_4569.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "GearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_results(self: Self) -> "_358.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4362.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4362.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool":
        return self._Cast_GearCompoundParametricStudyTool(self)
