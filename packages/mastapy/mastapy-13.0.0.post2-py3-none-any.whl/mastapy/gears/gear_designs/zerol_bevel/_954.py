"""ZerolBevelGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _352
    from mastapy.gears.gear_designs.zerol_bevel import _952, _953


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetDesign",)


Self = TypeVar("Self", bound="ZerolBevelGearSetDesign")


class ZerolBevelGearSetDesign(_1182.BevelGearSetDesign):
    """ZerolBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetDesign")

    class _Cast_ZerolBevelGearSetDesign:
        """Special nested class for casting ZerolBevelGearSetDesign to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
            parent: "ZerolBevelGearSetDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_design(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ):
            return self._parent._cast(_1182.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ):
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearSetDesign)

        @property
        def gear_design_component(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign",
        ) -> "ZerolBevelGearSetDesign":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def tooth_taper_zerol(self: Self) -> "_352.ZerolBevelGleasonToothTaperOption":
        """mastapy.gears.ZerolBevelGleasonToothTaperOption"""
        temp = self.wrapped.ToothTaperZerol

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.ZerolBevelGleasonToothTaperOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._352", "ZerolBevelGleasonToothTaperOption"
        )(value)

    @tooth_taper_zerol.setter
    @enforce_parameter_types
    def tooth_taper_zerol(self: Self, value: "_352.ZerolBevelGleasonToothTaperOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.ZerolBevelGleasonToothTaperOption"
        )
        self.wrapped.ToothTaperZerol = value

    @property
    def gears(self: Self) -> "List[_952.ZerolBevelGearDesign]":
        """List[mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears(self: Self) -> "List[_952.ZerolBevelGearDesign]":
        """List[mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes(self: Self) -> "List[_953.ZerolBevelGearMeshDesign]":
        """List[mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign":
        return self._Cast_ZerolBevelGearSetDesign(self)
