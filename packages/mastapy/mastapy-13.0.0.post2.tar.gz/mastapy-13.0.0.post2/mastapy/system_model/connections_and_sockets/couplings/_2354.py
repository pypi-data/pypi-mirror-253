"""TorqueConverterTurbineSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2347
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterTurbineSocket",
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineSocket",)


Self = TypeVar("Self", bound="TorqueConverterTurbineSocket")


class TorqueConverterTurbineSocket(_2347.CouplingSocket):
    """TorqueConverterTurbineSocket

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterTurbineSocket")

    class _Cast_TorqueConverterTurbineSocket:
        """Special nested class for casting TorqueConverterTurbineSocket to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
            parent: "TorqueConverterTurbineSocket",
        ):
            self._parent = parent

        @property
        def coupling_socket(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
        ):
            return self._parent._cast(_2347.CouplingSocket)

        @property
        def cylindrical_socket(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def torque_converter_turbine_socket(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
        ) -> "TorqueConverterTurbineSocket":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterTurbineSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket":
        return self._Cast_TorqueConverterTurbineSocket(self)
