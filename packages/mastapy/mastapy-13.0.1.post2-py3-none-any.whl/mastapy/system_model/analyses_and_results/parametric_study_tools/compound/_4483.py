"""CVTBeltConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4452,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CVTBeltConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundParametricStudyTool")


class CVTBeltConnectionCompoundParametricStudyTool(
    _4452.BeltConnectionCompoundParametricStudyTool
):
    """CVTBeltConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundParametricStudyTool"
    )

    class _Cast_CVTBeltConnectionCompoundParametricStudyTool:
        """Special nested class for casting CVTBeltConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
            parent: "CVTBeltConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4452.BeltConnectionCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
        ) -> "CVTBeltConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "CVTBeltConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4336.CVTBeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTBeltConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4336.CVTBeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTBeltConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionCompoundParametricStudyTool._Cast_CVTBeltConnectionCompoundParametricStudyTool":
        return self._Cast_CVTBeltConnectionCompoundParametricStudyTool(self)
