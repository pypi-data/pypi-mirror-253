"""SynchroniserSleeveCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4558,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SynchroniserSleeveCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4430


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundParametricStudyTool")


class SynchroniserSleeveCompoundParametricStudyTool(
    _4558.SynchroniserPartCompoundParametricStudyTool
):
    """SynchroniserSleeveCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundParametricStudyTool"
    )

    class _Cast_SynchroniserSleeveCompoundParametricStudyTool:
        """Special nested class for casting SynchroniserSleeveCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
            parent: "SynchroniserSleeveCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4558.SynchroniserPartCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
        ) -> "SynchroniserSleeveCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
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
        instance_to_wrap: "SynchroniserSleeveCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "_6971.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "List[_4430.SynchroniserSleeveParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool]

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
    ) -> "List[_4430.SynchroniserSleeveParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool]

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
    ) -> "SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool":
        return self._Cast_SynchroniserSleeveCompoundParametricStudyTool(self)
