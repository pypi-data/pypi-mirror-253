"""AbstractShaftOrHousingCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6433
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractShaftOrHousingCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundDynamicAnalysis")


class AbstractShaftOrHousingCompoundDynamicAnalysis(
    _6433.ComponentCompoundDynamicAnalysis
):
    """AbstractShaftOrHousingCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundDynamicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
            parent: "AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(_6409.AbstractShaftCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.FEPartCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.ShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "AbstractShaftOrHousingCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6279.AbstractShaftOrHousingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis]

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
    ) -> "List[_6279.AbstractShaftOrHousingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis(self)
