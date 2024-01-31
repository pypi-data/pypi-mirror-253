"""CVTPulleyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6762,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundCriticalSpeedAnalysis")


class CVTPulleyCompoundCriticalSpeedAnalysis(_6762.PulleyCompoundCriticalSpeedAnalysis):
    """CVTPulleyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CVTPulleyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
            parent: "CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6762.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ) -> "CVTPulleyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6587.CVTPulleyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTPulleyCriticalSpeedAnalysis]

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
    ) -> "List[_6587.CVTPulleyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTPulleyCriticalSpeedAnalysis]

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
    ) -> "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis":
        return self._Cast_CVTPulleyCompoundCriticalSpeedAnalysis(self)
