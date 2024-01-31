"""ISO63362006MeshSingleFlankRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362006_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63362006MeshSingleFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISO63362006MeshSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63362006MeshSingleFlankRating")


class ISO63362006MeshSingleFlankRating(_520.ISO6336AbstractMetalMeshSingleFlankRating):
    """ISO63362006MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362006_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63362006MeshSingleFlankRating")

    class _Cast_ISO63362006MeshSingleFlankRating:
        """Special nested class for casting ISO63362006MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
            parent: "ISO63362006MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ):
            return self._parent._cast(_520.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ):
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _516

            return self._parent._cast(_516.ISO63362019MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
        ) -> "ISO63362006MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63362006MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def deep_tooth_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeepToothFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorSource

        if temp is None:
            return ""

        return temp

    @property
    def helix_angle_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_stiffness_face(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffnessFace

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_stiffness_transverse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffnessTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def transverse_load_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating":
        return self._Cast_ISO63362006MeshSingleFlankRating(self)
