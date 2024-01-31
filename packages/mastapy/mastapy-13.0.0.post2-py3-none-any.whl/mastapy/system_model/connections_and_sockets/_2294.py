"""ShaftSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ShaftSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSocket",)


Self = TypeVar("Self", bound="ShaftSocket")


class ShaftSocket(_2276.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSocket")

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self: "ShaftSocket._Cast_ShaftSocket", parent: "ShaftSocket"):
            self._parent = parent

        @property
        def cylindrical_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def inner_shaft_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2333

            return self._parent._cast(_2333.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2334

            return self._parent._cast(_2334.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(self: "ShaftSocket._Cast_ShaftSocket"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self: "ShaftSocket._Cast_ShaftSocket") -> "ShaftSocket":
            return self._parent

        def __getattr__(self: "ShaftSocket._Cast_ShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSocket._Cast_ShaftSocket":
        return self._Cast_ShaftSocket(self)
