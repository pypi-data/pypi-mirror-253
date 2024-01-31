"""BevelGearTeethSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearTeethSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearTeethSocket",)


Self = TypeVar("Self", bound="BevelGearTeethSocket")


class BevelGearTeethSocket(_2300.AGMAGleasonConicalGearTeethSocket):
    """BevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearTeethSocket")

    class _Cast_BevelGearTeethSocket:
        """Special nested class for casting BevelGearTeethSocket to subclasses."""

        def __init__(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
            parent: "BevelGearTeethSocket",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            return self._parent._cast(_2300.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.GearTeethSocket)

        @property
        def socket(self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket"):
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.Socket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.BevelDifferentialGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.ZerolBevelGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "BevelGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearTeethSocket._Cast_BevelGearTeethSocket":
        return self._Cast_BevelGearTeethSocket(self)
