"""ConicalRateableMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalRateableMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalRateableMesh",)


Self = TypeVar("Self", bound="ConicalRateableMesh")


class ConicalRateableMesh(_367.RateableMesh):
    """ConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalRateableMesh")

    class _Cast_ConicalRateableMesh:
        """Special nested class for casting ConicalRateableMesh to subclasses."""

        def __init__(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
            parent: "ConicalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(self: "ConicalRateableMesh._Cast_ConicalRateableMesh"):
            return self._parent._cast(_367.RateableMesh)

        @property
        def iso10300_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ):
            from mastapy.gears.rating.iso_10300 import _427

            return self._parent._cast(_427.ISO10300RateableMesh)

        @property
        def hypoid_rateable_mesh(self: "ConicalRateableMesh._Cast_ConicalRateableMesh"):
            from mastapy.gears.rating.hypoid.standards import _444

            return self._parent._cast(_444.HypoidRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ):
            from mastapy.gears.rating.bevel.standards import _564

            return self._parent._cast(_564.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _568

            return self._parent._cast(_568.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "ConicalRateableMesh":
            return self._parent

        def __getattr__(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalRateableMesh._Cast_ConicalRateableMesh":
        return self._Cast_ConicalRateableMesh(self)
