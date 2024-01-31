"""BevelDifferentialGearTeethSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "BevelDifferentialGearTeethSocket",
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearTeethSocket",)


Self = TypeVar("Self", bound="BevelDifferentialGearTeethSocket")


class BevelDifferentialGearTeethSocket(_2304.BevelGearTeethSocket):
    """BevelDifferentialGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearTeethSocket")

    class _Cast_BevelDifferentialGearTeethSocket:
        """Special nested class for casting BevelDifferentialGearTeethSocket to subclasses."""

        def __init__(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
            parent: "BevelDifferentialGearTeethSocket",
        ):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ):
            return self._parent._cast(_2304.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2300

            return self._parent._cast(_2300.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.GearTeethSocket)

        @property
        def socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
        ) -> "BevelDifferentialGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket":
        return self._Cast_BevelDifferentialGearTeethSocket(self)
