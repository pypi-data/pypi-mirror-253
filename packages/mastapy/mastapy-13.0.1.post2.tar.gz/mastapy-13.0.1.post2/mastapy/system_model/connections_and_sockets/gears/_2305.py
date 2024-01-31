"""ConceptGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1177


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMesh",)


Self = TypeVar("Self", bound="ConceptGearMesh")


class ConceptGearMesh(_2313.GearMesh):
    """ConceptGearMesh

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMesh")

    class _Cast_ConceptGearMesh:
        """Special nested class for casting ConceptGearMesh to subclasses."""

        def __init__(
            self: "ConceptGearMesh._Cast_ConceptGearMesh", parent: "ConceptGearMesh"
        ):
            self._parent = parent

        @property
        def gear_mesh(self: "ConceptGearMesh._Cast_ConceptGearMesh"):
            return self._parent._cast(_2313.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(self: "ConceptGearMesh._Cast_ConceptGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(self: "ConceptGearMesh._Cast_ConceptGearMesh"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def concept_gear_mesh(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "ConceptGearMesh":
            return self._parent

        def __getattr__(self: "ConceptGearMesh._Cast_ConceptGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def active_gear_mesh_design(self: Self) -> "_1177.ConceptGearMeshDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_mesh_design(self: Self) -> "_1177.ConceptGearMeshDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearMesh._Cast_ConceptGearMesh":
        return self._Cast_ConceptGearMesh(self)
