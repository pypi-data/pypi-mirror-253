"""ZerolBevelGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _953


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMesh",)


Self = TypeVar("Self", bound="ZerolBevelGearMesh")


class ZerolBevelGearMesh(_2303.BevelGearMesh):
    """ZerolBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMesh")

    class _Cast_ZerolBevelGearMesh:
        """Special nested class for casting ZerolBevelGearMesh to subclasses."""

        def __init__(
            self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh",
            parent: "ZerolBevelGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh"):
            return self._parent._cast(_2303.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.ConicalGearMesh)

        @property
        def gear_mesh(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def zerol_bevel_gear_mesh(
            self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh",
        ) -> "ZerolBevelGearMesh":
            return self._parent

        def __getattr__(self: "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_953.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_mesh_design(self: Self) -> "_953.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ZerolBevelGearMesh._Cast_ZerolBevelGearMesh":
        return self._Cast_ZerolBevelGearMesh(self)
