"""PlanetaryConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4956,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PlanetaryConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6933


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetaryConnectionModalAnalysisAtAStiffness")


class PlanetaryConnectionModalAnalysisAtAStiffness(
    _4956.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
):
    """PlanetaryConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetaryConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetaryConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
            parent: "PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4956.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4860,
            )

            return self._parent._cast(
                _4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
        ) -> "PlanetaryConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PlanetaryConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6933.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionModalAnalysisAtAStiffness._Cast_PlanetaryConnectionModalAnalysisAtAStiffness":
        return self._Cast_PlanetaryConnectionModalAnalysisAtAStiffness(self)
