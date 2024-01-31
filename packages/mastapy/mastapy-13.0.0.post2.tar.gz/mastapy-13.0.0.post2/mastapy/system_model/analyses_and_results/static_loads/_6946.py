"""RollingRingConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionLoadCase",)


Self = TypeVar("Self", bound="RollingRingConnectionLoadCase")


class RollingRingConnectionLoadCase(_6911.InterMountableComponentConnectionLoadCase):
    """RollingRingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingConnectionLoadCase")

    class _Cast_RollingRingConnectionLoadCase:
        """Special nested class for casting RollingRingConnectionLoadCase to subclasses."""

        def __init__(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
            parent: "RollingRingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ):
            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_load_case(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
        ) -> "RollingRingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2292.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingConnectionLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionLoadCase._Cast_RollingRingConnectionLoadCase":
        return self._Cast_RollingRingConnectionLoadCase(self)
