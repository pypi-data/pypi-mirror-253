"""FaceGearMeshMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearMeshMicroGeometry"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _996, _991, _993


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshMicroGeometry",)


Self = TypeVar("Self", bound="FaceGearMeshMicroGeometry")


class FaceGearMeshMicroGeometry(_1225.GearMeshImplementationDetail):
    """FaceGearMeshMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshMicroGeometry")

    class _Cast_FaceGearMeshMicroGeometry:
        """Special nested class for casting FaceGearMeshMicroGeometry to subclasses."""

        def __init__(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry",
            parent: "FaceGearMeshMicroGeometry",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry",
        ):
            return self._parent._cast(_1225.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def face_gear_mesh_micro_geometry(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry",
        ) -> "FaceGearMeshMicroGeometry":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear_set_micro_geometry(self: Self) -> "_996.FaceGearSetMicroGeometry":
        """mastapy.gears.gear_designs.face.FaceGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSetMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_mesh(self: Self) -> "_991.FaceGearMeshDesign":
        """mastapy.gears.gear_designs.face.FaceGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear_micro_geometries(self: Self) -> "List[_993.FaceGearMicroGeometry]":
        """List[mastapy.gears.gear_designs.face.FaceGearMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearMeshMicroGeometry._Cast_FaceGearMeshMicroGeometry":
        return self._Cast_FaceGearMeshMicroGeometry(self)
