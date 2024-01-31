"""CylindricalRateableMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalRateableMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRateableMesh",)


Self = TypeVar("Self", bound="CylindricalRateableMesh")


class CylindricalRateableMesh(_367.RateableMesh):
    """CylindricalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalRateableMesh")

    class _Cast_CylindricalRateableMesh:
        """Special nested class for casting CylindricalRateableMesh to subclasses."""

        def __init__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
            parent: "CylindricalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            return self._parent._cast(_367.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493

            return self._parent._cast(_493.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498

            return self._parent._cast(_498.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _499

            return self._parent._cast(_499.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500

            return self._parent._cast(_500.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _522

            return self._parent._cast(_522.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.agma import _536

            return self._parent._cast(_536.AGMA2101RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "CylindricalRateableMesh":
            return self._parent

        def __getattr__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalRateableMesh._Cast_CylindricalRateableMesh":
        return self._Cast_CylindricalRateableMesh(self)
