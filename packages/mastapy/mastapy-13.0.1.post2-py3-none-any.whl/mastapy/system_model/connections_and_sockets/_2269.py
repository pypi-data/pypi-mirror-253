"""CoaxialConnection"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnection",)


Self = TypeVar("Self", bound="CoaxialConnection")


class CoaxialConnection(_2295.ShaftToMountableComponentConnection):
    """CoaxialConnection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnection")

    class _Cast_CoaxialConnection:
        """Special nested class for casting CoaxialConnection to subclasses."""

        def __init__(
            self: "CoaxialConnection._Cast_CoaxialConnection",
            parent: "CoaxialConnection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ):
            return self._parent._cast(_2295.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2265

            return self._parent._cast(_2265.AbstractShaftToMountableComponentConnection)

        @property
        def connection(self: "CoaxialConnection._Cast_CoaxialConnection"):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(self: "CoaxialConnection._Cast_CoaxialConnection"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2335

            return self._parent._cast(_2335.CycloidalDiscCentralBearingConnection)

        @property
        def coaxial_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "CoaxialConnection":
            return self._parent

        def __getattr__(self: "CoaxialConnection._Cast_CoaxialConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CoaxialConnection._Cast_CoaxialConnection":
        return self._Cast_CoaxialConnection(self)
