"""AbstractShaftOrHousingCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4467,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundParametricStudyTool")


class AbstractShaftOrHousingCompoundParametricStudyTool(
    _4467.ComponentCompoundParametricStudyTool
):
    """AbstractShaftOrHousingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundParametricStudyTool"
    )

    class _Cast_AbstractShaftOrHousingCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftOrHousingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
            parent: "AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4467.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractShaftCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.CycloidalDiscCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.FEPartCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.ShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
        ) -> "AbstractShaftOrHousingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4296.AbstractShaftOrHousingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool]

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
    ) -> "List[_4296.AbstractShaftOrHousingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool]

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
    ) -> "AbstractShaftOrHousingCompoundParametricStudyTool._Cast_AbstractShaftOrHousingCompoundParametricStudyTool":
        return self._Cast_AbstractShaftOrHousingCompoundParametricStudyTool(self)
