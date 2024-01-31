"""InnerShaftSocketBase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SHAFT_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "InnerShaftSocketBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("InnerShaftSocketBase",)


Self = TypeVar("Self", bound="InnerShaftSocketBase")


class InnerShaftSocketBase(_2294.ShaftSocket):
    """InnerShaftSocketBase

    This is a mastapy class.
    """

    TYPE = _INNER_SHAFT_SOCKET_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerShaftSocketBase")

    class _Cast_InnerShaftSocketBase:
        """Special nested class for casting InnerShaftSocketBase to subclasses."""

        def __init__(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
            parent: "InnerShaftSocketBase",
        ):
            self._parent = parent

        @property
        def shaft_socket(self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase"):
            return self._parent._cast(_2294.ShaftSocket)

        @property
        def cylindrical_socket(self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase"):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def inner_shaft_socket(self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase"):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InnerShaftSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2333

            return self._parent._cast(_2333.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscInnerSocket)

        @property
        def inner_shaft_socket_base(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "InnerShaftSocketBase":
            return self._parent

        def __getattr__(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerShaftSocketBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InnerShaftSocketBase._Cast_InnerShaftSocketBase":
        return self._Cast_InnerShaftSocketBase(self)
