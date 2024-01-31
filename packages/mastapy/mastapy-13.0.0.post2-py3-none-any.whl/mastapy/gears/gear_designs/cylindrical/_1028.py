"""CylindricalGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Union, Tuple, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy.gears import _319
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs import _950
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _294
    from mastapy.gears.gear_designs.cylindrical import (
        _1047,
        _998,
        _1022,
        _1060,
        _1029,
        _1063,
        _1070,
        _1088,
        _1012,
        _1018,
        _1030,
    )
    from mastapy.gears.rating.cylindrical.iso6336 import _510
    from mastapy.gears.manufacturing.cylindrical import _625
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107
    from mastapy.gears.rating.cylindrical import _454, _463


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetDesign",)


Self = TypeVar("Self", bound="CylindricalGearSetDesign")


class CylindricalGearSetDesign(_950.GearSetDesign):
    """CylindricalGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetDesign")

    class _Cast_CylindricalGearSetDesign:
        """Special nested class for casting CylindricalGearSetDesign to subclasses."""

        def __init__(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign",
            parent: "CylindricalGearSetDesign",
        ):
            self._parent = parent

        @property
        def gear_set_design(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign",
        ):
            return self._parent._cast(_950.GearSetDesign)

        @property
        def gear_design_component(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1041

            return self._parent._cast(_1041.CylindricalPlanetaryGearSetDesign)

        @property
        def cylindrical_gear_set_design(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign",
        ) -> "CylindricalGearSetDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_gears_number_of_teeth(self: Self) -> "List[int]":
        """List[int]"""
        temp = self.wrapped.AllGearsNumberOfTeeth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @all_gears_number_of_teeth.setter
    @enforce_parameter_types
    def all_gears_number_of_teeth(self: Self, value: "List[int]"):
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.AllGearsNumberOfTeeth = value

    @property
    def axial_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_calculation_method(
        self: Self,
    ) -> "overridable.Overridable_CoefficientOfFrictionCalculationMethod":
        """Overridable[mastapy.gears.CoefficientOfFrictionCalculationMethod]"""
        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = (
            overridable.Overridable_CoefficientOfFrictionCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_calculation_method(
        self: Self,
        value: "Union[_319.CoefficientOfFrictionCalculationMethod, Tuple[_319.CoefficientOfFrictionCalculationMethod, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_CoefficientOfFrictionCalculationMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_CoefficientOfFrictionCalculationMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def diametral_pitch_per_inch(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametralPitchPerInch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch_per_inch.setter
    @enforce_parameter_types
    def diametral_pitch_per_inch(self: Self, value: "float"):
        self.wrapped.DiametralPitchPerInch = float(value) if value is not None else 0.0

    @property
    def diametral_pitch_per_inch_with_centre_distance_adjustment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametralPitchPerInchWithCentreDistanceAdjustment

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch_per_inch_with_centre_distance_adjustment.setter
    @enforce_parameter_types
    def diametral_pitch_per_inch_with_centre_distance_adjustment(
        self: Self, value: "float"
    ):
        self.wrapped.DiametralPitchPerInchWithCentreDistanceAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def efficiency_rating_method(self: Self) -> "_294.EfficiencyRatingMethod":
        """mastapy.materials.efficiency.EfficiencyRatingMethod"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._294", "EfficiencyRatingMethod"
        )(value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(self: Self, value: "_294.EfficiencyRatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def fe_model_for_tiff(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FEModelForTIFF.SelectedItemName

        if temp is None:
            return ""

        return temp

    @fe_model_for_tiff.setter
    @enforce_parameter_types
    def fe_model_for_tiff(self: Self, value: "str"):
        self.wrapped.FEModelForTIFF.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def face_width(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return None

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "Optional[float]"):
        self.wrapped.FaceWidth = value

    @property
    def face_width_with_constant_axial_contact_ratio(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.FaceWidthWithConstantAxialContactRatio

        if temp is None:
            return None

        return temp

    @face_width_with_constant_axial_contact_ratio.setter
    @enforce_parameter_types
    def face_width_with_constant_axial_contact_ratio(
        self: Self, value: "Optional[float]"
    ):
        self.wrapped.FaceWidthWithConstantAxialContactRatio = value

    @property
    def gear_fit_system(self: Self) -> "_1047.GearFitSystems":
        """mastapy.gears.gear_designs.cylindrical.GearFitSystems"""
        temp = self.wrapped.GearFitSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.GearFitSystems"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1047", "GearFitSystems"
        )(value)

    @gear_fit_system.setter
    @enforce_parameter_types
    def gear_fit_system(self: Self, value: "_1047.GearFitSystems"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.GearFitSystems"
        )
        self.wrapped.GearFitSystem = value

    @property
    def gear_tooth_thickness_reduction_allowance(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.GearToothThicknessReductionAllowance

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @gear_tooth_thickness_reduction_allowance.setter
    @enforce_parameter_types
    def gear_tooth_thickness_reduction_allowance(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.GearToothThicknessReductionAllowance = value

    @property
    def gear_tooth_thickness_tolerance(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.GearToothThicknessTolerance

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @gear_tooth_thickness_tolerance.setter
    @enforce_parameter_types
    def gear_tooth_thickness_tolerance(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.GearToothThicknessTolerance = value

    @property
    def helical_gear_micro_geometry_option(
        self: Self,
    ) -> "_510.HelicalGearMicroGeometryOption":
        """mastapy.gears.rating.cylindrical.iso6336.HelicalGearMicroGeometryOption"""
        temp = self.wrapped.HelicalGearMicroGeometryOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336.HelicalGearMicroGeometryOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical.iso6336._510",
            "HelicalGearMicroGeometryOption",
        )(value)

    @helical_gear_micro_geometry_option.setter
    @enforce_parameter_types
    def helical_gear_micro_geometry_option(
        self: Self, value: "_510.HelicalGearMicroGeometryOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336.HelicalGearMicroGeometryOption",
        )
        self.wrapped.HelicalGearMicroGeometryOption = value

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def helix_angle_maintain_transverse_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleMaintainTransverseProfile

        if temp is None:
            return 0.0

        return temp

    @helix_angle_maintain_transverse_profile.setter
    @enforce_parameter_types
    def helix_angle_maintain_transverse_profile(self: Self, value: "float"):
        self.wrapped.HelixAngleMaintainTransverseProfile = (
            float(value) if value is not None else 0.0
        )

    @property
    def helix_angle_calculating_gear_teeth_numbers(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleCalculatingGearTeethNumbers

        if temp is None:
            return 0.0

        return temp

    @helix_angle_calculating_gear_teeth_numbers.setter
    @enforce_parameter_types
    def helix_angle_calculating_gear_teeth_numbers(self: Self, value: "float"):
        self.wrapped.HelixAngleCalculatingGearTeethNumbers = (
            float(value) if value is not None else 0.0
        )

    @property
    def helix_angle_with_centre_distance_adjustment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleWithCentreDistanceAdjustment

        if temp is None:
            return 0.0

        return temp

    @helix_angle_with_centre_distance_adjustment.setter
    @enforce_parameter_types
    def helix_angle_with_centre_distance_adjustment(self: Self, value: "float"):
        self.wrapped.HelixAngleWithCentreDistanceAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def is_asymmetric(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsAsymmetric

        if temp is None:
            return False

        return temp

    @is_asymmetric.setter
    @enforce_parameter_types
    def is_asymmetric(self: Self, value: "bool"):
        self.wrapped.IsAsymmetric = bool(value) if value is not None else False

    @property
    def maximum_acceptable_transverse_contact_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_transverse_contact_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumAcceptableTransverseContactRatio = value

    @property
    def maximum_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_axial_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tip_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: Self, value: "float"):
        self.wrapped.NormalModule = float(value) if value is not None else 0.0

    @property
    def normal_module_maintain_transverse_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModuleMaintainTransverseProfile

        if temp is None:
            return 0.0

        return temp

    @normal_module_maintain_transverse_profile.setter
    @enforce_parameter_types
    def normal_module_maintain_transverse_profile(self: Self, value: "float"):
        self.wrapped.NormalModuleMaintainTransverseProfile = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_module_calculating_gear_teeth_numbers(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModuleCalculatingGearTeethNumbers

        if temp is None:
            return 0.0

        return temp

    @normal_module_calculating_gear_teeth_numbers.setter
    @enforce_parameter_types
    def normal_module_calculating_gear_teeth_numbers(self: Self, value: "float"):
        self.wrapped.NormalModuleCalculatingGearTeethNumbers = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_module_with_centre_distance_adjustment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModuleWithCentreDistanceAdjustment

        if temp is None:
            return 0.0

        return temp

    @normal_module_with_centre_distance_adjustment.setter
    @enforce_parameter_types
    def normal_module_with_centre_distance_adjustment(self: Self, value: "float"):
        self.wrapped.NormalModuleWithCentreDistanceAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_constant_base_pitch(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngleConstantBasePitch

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle_constant_base_pitch.setter
    @enforce_parameter_types
    def normal_pressure_angle_constant_base_pitch(self: Self, value: "float"):
        self.wrapped.NormalPressureAngleConstantBasePitch = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_pressure_angle_maintain_transverse_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngleMaintainTransverseProfile

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle_maintain_transverse_profile.setter
    @enforce_parameter_types
    def normal_pressure_angle_maintain_transverse_profile(self: Self, value: "float"):
        self.wrapped.NormalPressureAngleMaintainTransverseProfile = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_shift_distribution_rule(
        self: Self,
    ) -> "_998.AddendumModificationDistributionRule":
        """mastapy.gears.gear_designs.cylindrical.AddendumModificationDistributionRule"""
        temp = self.wrapped.ProfileShiftDistributionRule

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AddendumModificationDistributionRule",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._998",
            "AddendumModificationDistributionRule",
        )(value)

    @profile_shift_distribution_rule.setter
    @enforce_parameter_types
    def profile_shift_distribution_rule(
        self: Self, value: "_998.AddendumModificationDistributionRule"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AddendumModificationDistributionRule",
        )
        self.wrapped.ProfileShiftDistributionRule = value

    @property
    def root_gear_profile_shift_coefficient_maintain_tip_and_root_diameters(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.RootGearProfileShiftCoefficientMaintainTipAndRootDiameters

        if temp is None:
            return 0.0

        return temp

    @root_gear_profile_shift_coefficient_maintain_tip_and_root_diameters.setter
    @enforce_parameter_types
    def root_gear_profile_shift_coefficient_maintain_tip_and_root_diameters(
        self: Self, value: "float"
    ):
        self.wrapped.RootGearProfileShiftCoefficientMaintainTipAndRootDiameters = (
            float(value) if value is not None else 0.0
        )

    @property
    def tooth_numbers_are_good(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothNumbersAreGood

        if temp is None:
            return False

        return temp

    @property
    def transverse_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseModule

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def cylindrical_gear_micro_geometry_settings(
        self: Self,
    ) -> "_1022.CylindricalGearMicroGeometrySettingsItem":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_manufacturing_configuration(
        self: Self,
    ) -> "_625.CylindricalSetManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_micro_geometry(
        self: Self,
    ) -> "_1107.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ltca_settings(self: Self) -> "_1060.LTCASettings":
        """mastapy.gears.gear_designs.cylindrical.LTCASettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCASettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: Self) -> "_1029.CylindricalGearSetFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micropitting(self: Self) -> "_1063.Micropitting":
        """mastapy.gears.gear_designs.cylindrical.Micropitting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Micropitting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_settings(
        self: Self,
    ) -> "_454.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1029.CylindricalGearSetFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scuffing(self: Self) -> "_1070.Scuffing":
        """mastapy.gears.gear_designs.cylindrical.Scuffing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Scuffing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def usage(self: Self) -> "_1088.Usage":
        """mastapy.gears.gear_designs.cylindrical.Usage

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Usage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_1012.CylindricalGearDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign]

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
    def cylindrical_gears(self: Self) -> "List[_1012.CylindricalGearDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes(self: Self) -> "List[_1018.CylindricalGearMeshDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flanks(self: Self) -> "List[_1029.CylindricalGearSetFlankDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearSetFlankDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def both_flanks(self: Self) -> "_1029.CylindricalGearSetFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometries(self: Self) -> "List[_1107.CylindricalGearSetMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def manufacturing_configurations(
        self: Self,
    ) -> "List[_625.CylindricalSetManufacturingConfig]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def centre_distance_editor(self: Self):
        """Method does not return."""
        self.wrapped.CentreDistanceEditor()

    def fix_errors_and_warnings(self: Self):
        """Method does not return."""
        self.wrapped.FixErrorsAndWarnings()

    def set_helix_angle_for_axial_contact_ratio(self: Self):
        """Method does not return."""
        self.wrapped.SetHelixAngleForAxialContactRatio()

    @enforce_parameter_types
    def add_new_manufacturing_configuration(
        self: Self, new_config_name: "str" = "None"
    ) -> "_625.CylindricalSetManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Args:
            new_config_name (str, optional)
        """
        new_config_name = str(new_config_name)
        method_result = self.wrapped.AddNewManufacturingConfiguration(
            new_config_name if new_config_name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def add_new_micro_geometry(self: Self) -> "_1107.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry"""
        method_result = self.wrapped.AddNewMicroGeometry()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def add_new_micro_geometry_specifying_separate_micro_geometry_per_tooth(
        self: Self,
    ) -> "_1107.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry"""
        method_result = (
            self.wrapped.AddNewMicroGeometrySpecifyingSeparateMicroGeometryPerTooth()
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_new_micro_geometry_specifying_separate_micro_geometry_per_tooth_for(
        self: Self, gears: "List[_1012.CylindricalGearDesign]"
    ) -> "_1107.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Args:
            gears (List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign])
        """
        gears = conversion.mp_to_pn_objects_in_dotnet_list(gears)
        method_result = (
            self.wrapped.AddNewMicroGeometrySpecifyingSeparateMicroGeometryPerToothFor(
                gears
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_optimiser(
        self: Self, duty_cycle: "_463.CylindricalGearSetDutyCycleRating"
    ) -> "_1030.CylindricalGearSetMacroGeometryOptimiser":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetMacroGeometryOptimiser

        Args:
            duty_cycle (mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating)
        """
        method_result = self.wrapped.CreateOptimiser(
            duty_cycle.wrapped if duty_cycle else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def delete_manufacturing_configuration(
        self: Self, config: "_625.CylindricalSetManufacturingConfig"
    ):
        """Method does not return.

        Args:
            config (mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig)
        """
        self.wrapped.DeleteManufacturingConfiguration(
            config.wrapped if config else None
        )

    @enforce_parameter_types
    def delete_micro_geometry(
        self: Self, micro_geometry: "_1107.CylindricalGearSetMicroGeometry"
    ):
        """Method does not return.

        Args:
            micro_geometry (mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry)
        """
        self.wrapped.DeleteMicroGeometry(
            micro_geometry.wrapped if micro_geometry else None
        )

    def delete_unused_manufacturing_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteUnusedManufacturingConfigurations()

    def try_make_valid(self: Self):
        """Method does not return."""
        self.wrapped.TryMakeValid()

    @enforce_parameter_types
    def micro_geometry_named(
        self: Self, micro_geometry_name: "str"
    ) -> "_1107.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Args:
            micro_geometry_name (str)
        """
        micro_geometry_name = str(micro_geometry_name)
        method_result = self.wrapped.MicroGeometryNamed(
            micro_geometry_name if micro_geometry_name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_active_manufacturing_configuration(
        self: Self, value: "_625.CylindricalSetManufacturingConfig"
    ):
        """Method does not return.

        Args:
            value (mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig)
        """
        self.wrapped.SetActiveManufacturingConfiguration(
            value.wrapped if value else None
        )

    @enforce_parameter_types
    def set_active_micro_geometry(
        self: Self, value: "_1107.CylindricalGearSetMicroGeometry"
    ):
        """Method does not return.

        Args:
            value (mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry)
        """
        self.wrapped.SetActiveMicroGeometry(value.wrapped if value else None)

    def clear_all_tooth_thickness_specifications(self: Self):
        """Method does not return."""
        self.wrapped.ClearAllToothThicknessSpecifications()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetDesign._Cast_CylindricalGearSetDesign":
        return self._Cast_CylindricalGearSetDesign(self)
