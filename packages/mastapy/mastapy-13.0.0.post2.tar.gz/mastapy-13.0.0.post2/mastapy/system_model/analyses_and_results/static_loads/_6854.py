"""CVTBeltConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionLoadCase",)


Self = TypeVar("Self", bound="CVTBeltConnectionLoadCase")


class CVTBeltConnectionLoadCase(_6820.BeltConnectionLoadCase):
    """CVTBeltConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionLoadCase")

    class _Cast_CVTBeltConnectionLoadCase:
        """Special nested class for casting CVTBeltConnectionLoadCase to subclasses."""

        def __init__(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
            parent: "CVTBeltConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def belt_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            return self._parent._cast(_6820.BeltConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_load_case(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase",
        ) -> "CVTBeltConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionLoadCase.TYPE"):
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
    ) -> "CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase":
        return self._Cast_CVTBeltConnectionLoadCase(self)
