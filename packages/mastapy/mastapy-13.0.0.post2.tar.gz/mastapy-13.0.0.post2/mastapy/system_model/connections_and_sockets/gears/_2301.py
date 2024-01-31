"""BevelDifferentialGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1181


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMesh",)


Self = TypeVar("Self", bound="BevelDifferentialGearMesh")


class BevelDifferentialGearMesh(_2303.BevelGearMesh):
    """BevelDifferentialGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearMesh")

    class _Cast_BevelDifferentialGearMesh:
        """Special nested class for casting BevelDifferentialGearMesh to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
            parent: "BevelDifferentialGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            return self._parent._cast(_2303.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "BevelDifferentialGearMesh":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_1181.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh":
        return self._Cast_BevelDifferentialGearMesh(self)
