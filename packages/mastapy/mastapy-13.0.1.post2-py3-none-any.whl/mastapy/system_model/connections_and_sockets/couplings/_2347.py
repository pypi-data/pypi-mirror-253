"""CouplingSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSocket",)


Self = TypeVar("Self", bound="CouplingSocket")


class CouplingSocket(_2276.CylindricalSocket):
    """CouplingSocket

    This is a mastapy class.
    """

    TYPE = _COUPLING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingSocket")

    class _Cast_CouplingSocket:
        """Special nested class for casting CouplingSocket to subclasses."""

        def __init__(
            self: "CouplingSocket._Cast_CouplingSocket", parent: "CouplingSocket"
        ):
            self._parent = parent

        @property
        def cylindrical_socket(self: "CouplingSocket._Cast_CouplingSocket"):
            return self._parent._cast(_2276.CylindricalSocket)

        @property
        def socket(self: "CouplingSocket._Cast_CouplingSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def clutch_socket(self: "CouplingSocket._Cast_CouplingSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2343

            return self._parent._cast(_2343.ClutchSocket)

        @property
        def concept_coupling_socket(self: "CouplingSocket._Cast_CouplingSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2345

            return self._parent._cast(_2345.ConceptCouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(self: "CouplingSocket._Cast_CouplingSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(self: "CouplingSocket._Cast_CouplingSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2354

            return self._parent._cast(_2354.TorqueConverterTurbineSocket)

        @property
        def coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "CouplingSocket":
            return self._parent

        def __getattr__(self: "CouplingSocket._Cast_CouplingSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CouplingSocket._Cast_CouplingSocket":
        return self._Cast_CouplingSocket(self)
