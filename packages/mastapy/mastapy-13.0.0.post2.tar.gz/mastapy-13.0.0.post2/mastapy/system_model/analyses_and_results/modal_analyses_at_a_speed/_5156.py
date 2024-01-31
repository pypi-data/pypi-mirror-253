"""CVTBeltConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTBeltConnectionModalAnalysisAtASpeed")


class CVTBeltConnectionModalAnalysisAtASpeed(_5125.BeltConnectionModalAnalysisAtASpeed):
    """CVTBeltConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionModalAnalysisAtASpeed"
    )

    class _Cast_CVTBeltConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CVTBeltConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
            parent: "CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5125.BeltConnectionModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(
                _5181.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
        ) -> "CVTBeltConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2273.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionModalAnalysisAtASpeed._Cast_CVTBeltConnectionModalAnalysisAtASpeed":
        return self._Cast_CVTBeltConnectionModalAnalysisAtASpeed(self)
