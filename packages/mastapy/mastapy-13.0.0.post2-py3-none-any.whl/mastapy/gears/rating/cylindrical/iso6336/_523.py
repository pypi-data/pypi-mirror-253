"""ISO6336RateableMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO6336RateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _478


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336RateableMesh",)


Self = TypeVar("Self", bound="ISO6336RateableMesh")


class ISO6336RateableMesh(_471.CylindricalRateableMesh):
    """ISO6336RateableMesh

    This is a mastapy class.
    """

    TYPE = _ISO6336_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336RateableMesh")

    class _Cast_ISO6336RateableMesh:
        """Special nested class for casting ISO6336RateableMesh to subclasses."""

        def __init__(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
            parent: "ISO6336RateableMesh",
        ):
            self._parent = parent

        @property
        def cylindrical_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            return self._parent._cast(_471.CylindricalRateableMesh)

        @property
        def rateable_mesh(self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh"):
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493

            return self._parent._cast(_493.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498

            return self._parent._cast(_498.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _499

            return self._parent._cast(_499.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500

            return self._parent._cast(_500.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _522

            return self._parent._cast(_522.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh",
        ) -> "ISO6336RateableMesh":
            return self._parent

        def __getattr__(
            self: "ISO6336RateableMesh._Cast_ISO6336RateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336RateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignment_contact_pattern_enhancement(
        self: Self,
    ) -> "_478.MisalignmentContactPatternEnhancements":
        """mastapy.gears.rating.cylindrical.MisalignmentContactPatternEnhancements"""
        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._478",
            "MisalignmentContactPatternEnhancements",
        )(value)

    @misalignment_contact_pattern_enhancement.setter
    @enforce_parameter_types
    def misalignment_contact_pattern_enhancement(
        self: Self, value: "_478.MisalignmentContactPatternEnhancements"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )
        self.wrapped.MisalignmentContactPatternEnhancement = value

    @property
    def cast_to(self: Self) -> "ISO6336RateableMesh._Cast_ISO6336RateableMesh":
        return self._Cast_ISO6336RateableMesh(self)
