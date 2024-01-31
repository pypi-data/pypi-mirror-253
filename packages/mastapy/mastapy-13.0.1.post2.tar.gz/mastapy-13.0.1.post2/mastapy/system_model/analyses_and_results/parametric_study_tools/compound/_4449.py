"""AGMAGleasonConicalGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4477,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundParametricStudyTool")


class AGMAGleasonConicalGearSetCompoundParametricStudyTool(
    _4477.ConicalGearSetCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
            parent: "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4477.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BevelGearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.HypoidGearSetCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4302.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4302.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool(self)
