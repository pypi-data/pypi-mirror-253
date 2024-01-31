"""PlanetCarrierCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6751,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6630


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundCriticalSpeedAnalysis")


class PlanetCarrierCompoundCriticalSpeedAnalysis(
    _6751.MountableComponentCompoundCriticalSpeedAnalysis
):
    """PlanetCarrierCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierCompoundCriticalSpeedAnalysis"
    )

    class _Cast_PlanetCarrierCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PlanetCarrierCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
            parent: "PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
        ) -> "PlanetCarrierCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetCarrierCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

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
    ) -> "List[_6630.PlanetCarrierCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PlanetCarrierCriticalSpeedAnalysis]

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
    ) -> "List[_6630.PlanetCarrierCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PlanetCarrierCriticalSpeedAnalysis]

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
    ) -> "PlanetCarrierCompoundCriticalSpeedAnalysis._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis":
        return self._Cast_PlanetCarrierCompoundCriticalSpeedAnalysis(self)
