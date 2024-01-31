"""RingPinsSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal", "RingPinsSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsSocket",)


Self = TypeVar("Self", bound="RingPinsSocket")


class RingPinsSocket(_2276.CylindricalSocket):
    """RingPinsSocket

    This is a mastapy class.
    """

    TYPE = _RING_PINS_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsSocket")

    class _Cast_RingPinsSocket:
        """Special nested class for casting RingPinsSocket to subclasses."""

        def __init__(
            self: "RingPinsSocket._Cast_RingPinsSocket", parent: "RingPinsSocket"
        ):
            self._parent = parent

        @property
        def cylindrical_socket(self: "RingPinsSocket._Cast_RingPinsSocket"):
            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "RingPinsSocket._Cast_RingPinsSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def ring_pins_socket(
            self: "RingPinsSocket._Cast_RingPinsSocket",
        ) -> "RingPinsSocket":
            return self._parent

        def __getattr__(self: "RingPinsSocket._Cast_RingPinsSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RingPinsSocket._Cast_RingPinsSocket":
        return self._Cast_RingPinsSocket(self)
