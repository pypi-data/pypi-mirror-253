"""StraightBevelGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _962


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMesh",)


Self = TypeVar("Self", bound="StraightBevelGearMesh")


class StraightBevelGearMesh(_2303.BevelGearMesh):
    """StraightBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMesh")

    class _Cast_StraightBevelGearMesh:
        """Special nested class for casting StraightBevelGearMesh to subclasses."""

        def __init__(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
            parent: "StraightBevelGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            return self._parent._cast(_2303.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.ConicalGearMesh)

        @property
        def gear_mesh(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def straight_bevel_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ) -> "StraightBevelGearMesh":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_962.StraightBevelGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_mesh_design(
        self: Self,
    ) -> "_962.StraightBevelGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StraightBevelGearMesh._Cast_StraightBevelGearMesh":
        return self._Cast_StraightBevelGearMesh(self)
