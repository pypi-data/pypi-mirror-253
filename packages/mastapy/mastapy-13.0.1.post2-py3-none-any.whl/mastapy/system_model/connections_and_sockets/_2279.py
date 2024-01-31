"""InnerShaftSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "InnerShaftSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("InnerShaftSocket",)


Self = TypeVar("Self", bound="InnerShaftSocket")


class InnerShaftSocket(_2280.InnerShaftSocketBase):
    """InnerShaftSocket

    This is a mastapy class.
    """

    TYPE = _INNER_SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerShaftSocket")

    class _Cast_InnerShaftSocket:
        """Special nested class for casting InnerShaftSocket to subclasses."""

        def __init__(
            self: "InnerShaftSocket._Cast_InnerShaftSocket", parent: "InnerShaftSocket"
        ):
            self._parent = parent

        @property
        def inner_shaft_socket_base(self: "InnerShaftSocket._Cast_InnerShaftSocket"):
            return self._parent._cast(_2280.InnerShaftSocketBase)

        @property
        def shaft_socket(self: "InnerShaftSocket._Cast_InnerShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.ShaftSocket)

        @property
        def cylindrical_socket(self: "InnerShaftSocket._Cast_InnerShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "InnerShaftSocket._Cast_InnerShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def inner_shaft_socket(
            self: "InnerShaftSocket._Cast_InnerShaftSocket",
        ) -> "InnerShaftSocket":
            return self._parent

        def __getattr__(self: "InnerShaftSocket._Cast_InnerShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InnerShaftSocket._Cast_InnerShaftSocket":
        return self._Cast_InnerShaftSocket(self)
