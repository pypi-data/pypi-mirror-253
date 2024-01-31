"""AGMAGleasonConicalRateableMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.conical import _547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalRateableMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalRateableMesh",)


Self = TypeVar("Self", bound="AGMAGleasonConicalRateableMesh")


class AGMAGleasonConicalRateableMesh(_547.ConicalRateableMesh):
    """AGMAGleasonConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalRateableMesh")

    class _Cast_AGMAGleasonConicalRateableMesh:
        """Special nested class for casting AGMAGleasonConicalRateableMesh to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
            parent: "AGMAGleasonConicalRateableMesh",
        ):
            self._parent = parent

        @property
        def conical_rateable_mesh(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
        ):
            return self._parent._cast(_547.ConicalRateableMesh)

        @property
        def rateable_mesh(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
        ):
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.RateableMesh)

        @property
        def hypoid_rateable_mesh(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
        ):
            from mastapy.gears.rating.hypoid.standards import _444

            return self._parent._cast(_444.HypoidRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
        ):
            from mastapy.gears.rating.bevel.standards import _564

            return self._parent._cast(_564.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
        ) -> "AGMAGleasonConicalRateableMesh":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalRateableMesh._Cast_AGMAGleasonConicalRateableMesh":
        return self._Cast_AGMAGleasonConicalRateableMesh(self)
