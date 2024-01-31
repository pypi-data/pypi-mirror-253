"""UnbalancedMassCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6796,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6666


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundCriticalSpeedAnalysis")


class UnbalancedMassCompoundCriticalSpeedAnalysis(
    _6796.VirtualComponentCompoundCriticalSpeedAnalysis
):
    """UnbalancedMassCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundCriticalSpeedAnalysis"
    )

    class _Cast_UnbalancedMassCompoundCriticalSpeedAnalysis:
        """Special nested class for casting UnbalancedMassCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
            parent: "UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6796.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_6666.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "List[_6666.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis":
        return self._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis(self)
