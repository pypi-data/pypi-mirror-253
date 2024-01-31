"""CycloidalDiscCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6675,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundCriticalSpeedAnalysis")


class CycloidalDiscCompoundCriticalSpeedAnalysis(
    _6675.AbstractShaftCompoundCriticalSpeedAnalysis
):
    """CycloidalDiscCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CycloidalDiscCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
            parent: "CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6675.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(
                _6676.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
        ) -> "CycloidalDiscCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6590.CycloidalDiscCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CycloidalDiscCriticalSpeedAnalysis]

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
    ) -> "List[_6590.CycloidalDiscCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CycloidalDiscCriticalSpeedAnalysis]

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
    ) -> "CycloidalDiscCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis":
        return self._Cast_CycloidalDiscCompoundCriticalSpeedAnalysis(self)
