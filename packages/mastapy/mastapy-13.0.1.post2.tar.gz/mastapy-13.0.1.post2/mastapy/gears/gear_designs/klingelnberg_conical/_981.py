"""KlingelnbergConicalGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs.conical import _1154
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_KLINGELNBERG_CONICAL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical",
    "KlingelnbergConicalGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _601


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergConicalGearDesign")


class KlingelnbergConicalGearDesign(_1154.ConicalGearDesign):
    """KlingelnbergConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergConicalGearDesign")

    class _Cast_KlingelnbergConicalGearDesign:
        """Special nested class for casting KlingelnbergConicalGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
            parent: "KlingelnbergConicalGearDesign",
        ):
            self._parent = parent

        @property
        def conical_gear_design(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ):
            return self._parent._cast(_1154.ConicalGearDesign)

        @property
        def gear_design(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ):
            from mastapy.gears.gear_designs import _947

            return self._parent._cast(_947.GearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973

            return self._parent._cast(
                _973.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _977

            return self._parent._cast(_977.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
        ) -> "KlingelnbergConicalGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KlingelnbergConicalGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness_rz(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FlankRoughnessRZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @flank_roughness_rz.setter
    @enforce_parameter_types
    def flank_roughness_rz(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FlankRoughnessRZ = value

    @property
    def material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ""

        return temp

    @material.setter
    @enforce_parameter_types
    def material(self: Self, value: "str"):
        self.wrapped.Material.SetSelectedItem(str(value) if value is not None else "")

    @property
    def pitch_cone_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchConeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_sensitivity_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RelativeSensitivityFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @relative_sensitivity_factor.setter
    @enforce_parameter_types
    def relative_sensitivity_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RelativeSensitivityFactor = value

    @property
    def stress_correction_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @stress_correction_factor.setter
    @enforce_parameter_types
    def stress_correction_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StressCorrectionFactor = value

    @property
    def tooth_form_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToothFormFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tooth_form_factor.setter
    @enforce_parameter_types
    def tooth_form_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToothFormFactor = value

    @property
    def klingelnberg_cyclo_palloid_gear_material(
        self: Self,
    ) -> "_601.KlingelnbergCycloPalloidConicalGearMaterial":
        """mastapy.gears.materials.KlingelnbergCycloPalloidConicalGearMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidGearMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign":
        return self._Cast_KlingelnbergConicalGearDesign(self)
