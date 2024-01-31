"""CylindricalSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalSocket",)


Self = TypeVar("Self", bound="CylindricalSocket")


class CylindricalSocket(_2296.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalSocket")

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(
            self: "CylindricalSocket._Cast_CylindricalSocket",
            parent: "CylindricalSocket",
        ):
            self._parent = parent

        @property
        def socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            return self._parent._cast(_2296.Socket)

        @property
        def bearing_inner_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2266

            return self._parent._cast(_2266.BearingInnerSocket)

        @property
        def bearing_outer_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2267

            return self._parent._cast(_2267.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.CVTPulleySocket)

        @property
        def inner_shaft_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2282

            return self._parent._cast(_2282.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.MountableComponentSocket)

        @property
        def outer_shaft_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.OuterShaftSocketBase)

        @property
        def planetary_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.PlanetarySocket)

        @property
        def planetary_socket_base(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.PlanetarySocketBase)

        @property
        def pulley_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.PulleySocket)

        @property
        def rolling_ring_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.RollingRingSocket)

        @property
        def shaft_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.ShaftSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.CylindricalGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2333

            return self._parent._cast(_2333.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2334

            return self._parent._cast(_2334.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2337

            return self._parent._cast(_2337.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2339

            return self._parent._cast(_2339.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2340

            return self._parent._cast(_2340.RingPinsSocket)

        @property
        def clutch_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2343

            return self._parent._cast(_2343.ClutchSocket)

        @property
        def concept_coupling_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2345

            return self._parent._cast(_2345.ConceptCouplingSocket)

        @property
        def coupling_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2347

            return self._parent._cast(_2347.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(self: "CylindricalSocket._Cast_CylindricalSocket"):
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2354

            return self._parent._cast(_2354.TorqueConverterTurbineSocket)

        @property
        def cylindrical_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "CylindricalSocket":
            return self._parent

        def __getattr__(self: "CylindricalSocket._Cast_CylindricalSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalSocket._Cast_CylindricalSocket":
        return self._Cast_CylindricalSocket(self)
