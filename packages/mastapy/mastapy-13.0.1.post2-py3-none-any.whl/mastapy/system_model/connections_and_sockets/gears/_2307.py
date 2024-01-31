"""ConicalGearMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets.gears import _2313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMesh",)


Self = TypeVar("Self", bound="ConicalGearMesh")


class ConicalGearMesh(_2313.GearMesh):
    """ConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMesh")

    class _Cast_ConicalGearMesh:
        """Special nested class for casting ConicalGearMesh to subclasses."""

        def __init__(
            self: "ConicalGearMesh._Cast_ConicalGearMesh", parent: "ConicalGearMesh"
        ):
            self._parent = parent

        @property
        def gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            return self._parent._cast(_2313.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2303

            return self._parent._cast(_2303.BevelGearMesh)

        @property
        def hypoid_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(self: "ConicalGearMesh._Cast_ConicalGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.ZerolBevelGearMesh)

        @property
        def conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "ConicalGearMesh":
            return self._parent

        def __getattr__(self: "ConicalGearMesh._Cast_ConicalGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "float"):
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def pinion_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: Self, value: "float"):
        self.wrapped.PinionDropAngle = float(value) if value is not None else 0.0

    @property
    def wheel_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: Self, value: "float"):
        self.wrapped.WheelDropAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConicalGearMesh._Cast_ConicalGearMesh":
        return self._Cast_ConicalGearMesh(self)
