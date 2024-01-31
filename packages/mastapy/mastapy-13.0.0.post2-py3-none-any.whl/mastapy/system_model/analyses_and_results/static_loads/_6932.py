"""PlanetaryConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionLoadCase",)


Self = TypeVar("Self", bound="PlanetaryConnectionLoadCase")


class PlanetaryConnectionLoadCase(_6951.ShaftToMountableComponentConnectionLoadCase):
    """PlanetaryConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionLoadCase")

    class _Cast_PlanetaryConnectionLoadCase:
        """Special nested class for casting PlanetaryConnectionLoadCase to subclasses."""

        def __init__(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
            parent: "PlanetaryConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            return self._parent._cast(_6951.ShaftToMountableComponentConnectionLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(
                _6809.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_load_case(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
        ) -> "PlanetaryConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryConnectionLoadCase.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionLoadCase._Cast_PlanetaryConnectionLoadCase":
        return self._Cast_PlanetaryConnectionLoadCase(self)
