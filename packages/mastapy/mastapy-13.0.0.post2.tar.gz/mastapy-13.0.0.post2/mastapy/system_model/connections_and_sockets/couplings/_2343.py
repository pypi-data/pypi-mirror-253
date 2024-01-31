"""ClutchSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2347
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("ClutchSocket",)


Self = TypeVar("Self", bound="ClutchSocket")


class ClutchSocket(_2347.CouplingSocket):
    """ClutchSocket

    This is a mastapy class.
    """

    TYPE = _CLUTCH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchSocket")

    class _Cast_ClutchSocket:
        """Special nested class for casting ClutchSocket to subclasses."""

        def __init__(self: "ClutchSocket._Cast_ClutchSocket", parent: "ClutchSocket"):
            self._parent = parent

        @property
        def coupling_socket(self: "ClutchSocket._Cast_ClutchSocket"):
            return self._parent._cast(_2347.CouplingSocket)

        @property
        def cylindrical_socket(self: "ClutchSocket._Cast_ClutchSocket"):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "ClutchSocket._Cast_ClutchSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def clutch_socket(self: "ClutchSocket._Cast_ClutchSocket") -> "ClutchSocket":
            return self._parent

        def __getattr__(self: "ClutchSocket._Cast_ClutchSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ClutchSocket._Cast_ClutchSocket":
        return self._Cast_ClutchSocket(self)
