"""SynchroniserPartCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4482,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SynchroniserPartCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4429


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundParametricStudyTool")


class SynchroniserPartCompoundParametricStudyTool(
    _4482.CouplingHalfCompoundParametricStudyTool
):
    """SynchroniserPartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundParametricStudyTool"
    )

    class _Cast_SynchroniserPartCompoundParametricStudyTool:
        """Special nested class for casting SynchroniserPartCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
            parent: "SynchroniserPartCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(_4557.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
        ) -> "SynchroniserPartCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4429.SynchroniserPartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserPartParametricStudyTool]

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
    ) -> "List[_4429.SynchroniserPartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserPartParametricStudyTool]

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
    ) -> "SynchroniserPartCompoundParametricStudyTool._Cast_SynchroniserPartCompoundParametricStudyTool":
        return self._Cast_SynchroniserPartCompoundParametricStudyTool(self)
