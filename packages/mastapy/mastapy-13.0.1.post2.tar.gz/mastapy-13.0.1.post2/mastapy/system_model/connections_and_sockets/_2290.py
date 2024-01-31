"""PulleySocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PulleySocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("PulleySocket",)


Self = TypeVar("Self", bound="PulleySocket")


class PulleySocket(_2276.CylindricalSocket):
    """PulleySocket

    This is a mastapy class.
    """

    TYPE = _PULLEY_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleySocket")

    class _Cast_PulleySocket:
        """Special nested class for casting PulleySocket to subclasses."""

        def __init__(self: "PulleySocket._Cast_PulleySocket", parent: "PulleySocket"):
            self._parent = parent

        @property
        def cylindrical_socket(self: "PulleySocket._Cast_PulleySocket"):
            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "PulleySocket._Cast_PulleySocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def cvt_pulley_socket(self: "PulleySocket._Cast_PulleySocket"):
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.CVTPulleySocket)

        @property
        def pulley_socket(self: "PulleySocket._Cast_PulleySocket") -> "PulleySocket":
            return self._parent

        def __getattr__(self: "PulleySocket._Cast_PulleySocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleySocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PulleySocket._Cast_PulleySocket":
        return self._Cast_PulleySocket(self)
