"""ConnectorModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConnectorModalAnalysisAtASpeed")


class ConnectorModalAnalysisAtASpeed(_5195.MountableComponentModalAnalysisAtASpeed):
    """ConnectorModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysisAtASpeed")

    class _Cast_ConnectorModalAnalysisAtASpeed:
        """Special nested class for casting ConnectorModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
            parent: "ConnectorModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.BearingModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.OilSealModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "ConnectorModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed":
        return self._Cast_ConnectorModalAnalysisAtASpeed(self)
