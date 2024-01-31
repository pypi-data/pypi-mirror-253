"""TorqueConverterConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4894,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "TorqueConverterConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.static_loads import _6973


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="TorqueConverterConnectionModalAnalysisAtAStiffness")


class TorqueConverterConnectionModalAnalysisAtAStiffness(
    _4894.CouplingConnectionModalAnalysisAtAStiffness
):
    """TorqueConverterConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_TorqueConverterConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
            parent: "TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4894.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4923,
            )

            return self._parent._cast(
                _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "TorqueConverterConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6973.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness(self)
