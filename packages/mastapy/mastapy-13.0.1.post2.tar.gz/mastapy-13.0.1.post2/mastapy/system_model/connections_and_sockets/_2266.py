"""BearingInnerSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2282
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_INNER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BearingInnerSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingInnerSocket",)


Self = TypeVar("Self", bound="BearingInnerSocket")


class BearingInnerSocket(_2282.MountableComponentInnerSocket):
    """BearingInnerSocket

    This is a mastapy class.
    """

    TYPE = _BEARING_INNER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingInnerSocket")

    class _Cast_BearingInnerSocket:
        """Special nested class for casting BearingInnerSocket to subclasses."""

        def __init__(
            self: "BearingInnerSocket._Cast_BearingInnerSocket",
            parent: "BearingInnerSocket",
        ):
            self._parent = parent

        @property
        def mountable_component_inner_socket(
            self: "BearingInnerSocket._Cast_BearingInnerSocket",
        ):
            return self._parent._cast(_2282.MountableComponentInnerSocket)

        @property
        def mountable_component_socket(
            self: "BearingInnerSocket._Cast_BearingInnerSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.MountableComponentSocket)

        @property
        def cylindrical_socket(self: "BearingInnerSocket._Cast_BearingInnerSocket"):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "BearingInnerSocket._Cast_BearingInnerSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def bearing_inner_socket(
            self: "BearingInnerSocket._Cast_BearingInnerSocket",
        ) -> "BearingInnerSocket":
            return self._parent

        def __getattr__(self: "BearingInnerSocket._Cast_BearingInnerSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingInnerSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BearingInnerSocket._Cast_BearingInnerSocket":
        return self._Cast_BearingInnerSocket(self)
