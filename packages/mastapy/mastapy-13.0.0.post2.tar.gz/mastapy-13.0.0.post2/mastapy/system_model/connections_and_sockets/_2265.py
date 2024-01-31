"""AbstractShaftToMountableComponentConnection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464, _2435


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnection",)


Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnection")


class AbstractShaftToMountableComponentConnection(_2272.Connection):
    """AbstractShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftToMountableComponentConnection"
    )

    class _Cast_AbstractShaftToMountableComponentConnection:
        """Special nested class for casting AbstractShaftToMountableComponentConnection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
            parent: "AbstractShaftToMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def coaxial_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.CoaxialConnection)

        @property
        def planetary_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.PlanetaryConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2295

            return self._parent._cast(_2295.ShaftToMountableComponentConnection)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2335

            return self._parent._cast(_2335.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2338

            return self._parent._cast(_2338.CycloidalDiscPlanetaryBearingConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "AbstractShaftToMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
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
        self: Self, instance_to_wrap: "AbstractShaftToMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mountable_component(self: Self) -> "_2464.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft(self: Self) -> "_2435.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection":
        return self._Cast_AbstractShaftToMountableComponentConnection(self)
