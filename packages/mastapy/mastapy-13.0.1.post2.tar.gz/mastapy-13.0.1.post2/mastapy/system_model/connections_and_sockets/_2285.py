"""OuterShaftSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "OuterShaftSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("OuterShaftSocket",)


Self = TypeVar("Self", bound="OuterShaftSocket")


class OuterShaftSocket(_2286.OuterShaftSocketBase):
    """OuterShaftSocket

    This is a mastapy class.
    """

    TYPE = _OUTER_SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterShaftSocket")

    class _Cast_OuterShaftSocket:
        """Special nested class for casting OuterShaftSocket to subclasses."""

        def __init__(
            self: "OuterShaftSocket._Cast_OuterShaftSocket", parent: "OuterShaftSocket"
        ):
            self._parent = parent

        @property
        def outer_shaft_socket_base(self: "OuterShaftSocket._Cast_OuterShaftSocket"):
            return self._parent._cast(_2286.OuterShaftSocketBase)

        @property
        def shaft_socket(self: "OuterShaftSocket._Cast_OuterShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.ShaftSocket)

        @property
        def cylindrical_socket(self: "OuterShaftSocket._Cast_OuterShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "OuterShaftSocket._Cast_OuterShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def outer_shaft_socket(
            self: "OuterShaftSocket._Cast_OuterShaftSocket",
        ) -> "OuterShaftSocket":
            return self._parent

        def __getattr__(self: "OuterShaftSocket._Cast_OuterShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OuterShaftSocket._Cast_OuterShaftSocket":
        return self._Cast_OuterShaftSocket(self)
