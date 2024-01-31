"""ConicalMeshSingleFlankRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalMeshSingleFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshSingleFlankRating",)


Self = TypeVar("Self", bound="ConicalMeshSingleFlankRating")


class ConicalMeshSingleFlankRating(_366.MeshSingleFlankRating):
    """ConicalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshSingleFlankRating")

    class _Cast_ConicalMeshSingleFlankRating:
        """Special nested class for casting ConicalMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
            parent: "ConicalMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            return self._parent._cast(_366.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _422

            return self._parent._cast(_422.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _423

            return self._parent._cast(_423.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _424

            return self._parent._cast(_424.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _425

            return self._parent._cast(_425.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _426

            return self._parent._cast(_426.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.hypoid.standards import _443

            return self._parent._cast(_443.GleasonHypoidMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _558

            return self._parent._cast(_558.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _560

            return self._parent._cast(_560.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _562

            return self._parent._cast(_562.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
        ) -> "ConicalMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating":
        return self._Cast_ConicalMeshSingleFlankRating(self)
