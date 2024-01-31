"""AbstractShaftCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractShaftCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundDynamicAnalysis")


class AbstractShaftCompoundDynamicAnalysis(
    _6409.AbstractShaftOrHousingCompoundDynamicAnalysis
):
    """AbstractShaftCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftCompoundDynamicAnalysis")

    class _Cast_AbstractShaftCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
            parent: "AbstractShaftCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            return self._parent._cast(
                _6409.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def component_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.ShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "AbstractShaftCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6277.AbstractShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis]

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
    ) -> "List[_6277.AbstractShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis]

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
    ) -> "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis":
        return self._Cast_AbstractShaftCompoundDynamicAnalysis(self)
