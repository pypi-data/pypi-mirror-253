"""CVTBeltConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CVTBeltConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundDynamicAnalysis")


class CVTBeltConnectionCompoundDynamicAnalysis(
    _6416.BeltConnectionCompoundDynamicAnalysis
):
    """CVTBeltConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundDynamicAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
            parent: "CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6416.BeltConnectionCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
        ) -> "CVTBeltConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6316.CVTBeltConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis]

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
    ) -> "List[_6316.CVTBeltConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis]

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
    ) -> "CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis":
        return self._Cast_CVTBeltConnectionCompoundDynamicAnalysis(self)
