"""GearTeethSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearTeethSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearTeethSocket",)


Self = TypeVar("Self", bound="GearTeethSocket")


class GearTeethSocket(_2296.Socket):
    """GearTeethSocket

    This is a mastapy class.
    """

    TYPE = _GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearTeethSocket")

    class _Cast_GearTeethSocket:
        """Special nested class for casting GearTeethSocket to subclasses."""

        def __init__(
            self: "GearTeethSocket._Cast_GearTeethSocket", parent: "GearTeethSocket"
        ):
            self._parent = parent

        @property
        def socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            return self._parent._cast(_2296.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2300

            return self._parent._cast(_2300.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.ConicalGearTeethSocket)

        @property
        def face_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.FaceGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(self: "GearTeethSocket._Cast_GearTeethSocket"):
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.ZerolBevelGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "GearTeethSocket":
            return self._parent

        def __getattr__(self: "GearTeethSocket._Cast_GearTeethSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearTeethSocket._Cast_GearTeethSocket":
        return self._Cast_GearTeethSocket(self)
