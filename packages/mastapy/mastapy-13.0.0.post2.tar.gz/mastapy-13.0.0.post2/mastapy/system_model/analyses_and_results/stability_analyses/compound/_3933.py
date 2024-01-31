"""ConnectorCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConnectorCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3799


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundStabilityAnalysis")


class ConnectorCompoundStabilityAnalysis(
    _3974.MountableComponentCompoundStabilityAnalysis
):
    """ConnectorCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundStabilityAnalysis")

    class _Cast_ConnectorCompoundStabilityAnalysis:
        """Special nested class for casting ConnectorCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
            parent: "ConnectorCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.BearingCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(_3975.OilSealCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
        ) -> "ConnectorCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3799.ConnectorStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectorStabilityAnalysis]

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
    ) -> "List[_3799.ConnectorStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectorStabilityAnalysis]

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
    ) -> "ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis":
        return self._Cast_ConnectorCompoundStabilityAnalysis(self)
