"""AGMA2101RateableMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical import _471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2101_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA", "AGMA2101RateableMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMA2101RateableMesh",)


Self = TypeVar("Self", bound="AGMA2101RateableMesh")


class AGMA2101RateableMesh(_471.CylindricalRateableMesh):
    """AGMA2101RateableMesh

    This is a mastapy class.
    """

    TYPE = _AGMA2101_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA2101RateableMesh")

    class _Cast_AGMA2101RateableMesh:
        """Special nested class for casting AGMA2101RateableMesh to subclasses."""

        def __init__(
            self: "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh",
            parent: "AGMA2101RateableMesh",
        ):
            self._parent = parent

        @property
        def cylindrical_rateable_mesh(
            self: "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh",
        ):
            return self._parent._cast(_471.CylindricalRateableMesh)

        @property
        def rateable_mesh(self: "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh"):
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.RateableMesh)

        @property
        def agma2101_rateable_mesh(
            self: "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh",
        ) -> "AGMA2101RateableMesh":
            return self._parent

        def __getattr__(
            self: "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA2101RateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AGMA2101RateableMesh._Cast_AGMA2101RateableMesh":
        return self._Cast_AGMA2101RateableMesh(self)
