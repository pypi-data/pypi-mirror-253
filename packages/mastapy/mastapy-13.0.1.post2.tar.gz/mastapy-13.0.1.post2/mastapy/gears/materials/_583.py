"""AGMACylindricalGearMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.materials import _591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_CYLINDRICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "AGMACylindricalGearMaterial"
)

if TYPE_CHECKING:
    from mastapy.materials import _242, _240, _241


__docformat__ = "restructuredtext en"
__all__ = ("AGMACylindricalGearMaterial",)


Self = TypeVar("Self", bound="AGMACylindricalGearMaterial")


class AGMACylindricalGearMaterial(_591.CylindricalGearMaterial):
    """AGMACylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE = _AGMA_CYLINDRICAL_GEAR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMACylindricalGearMaterial")

    class _Cast_AGMACylindricalGearMaterial:
        """Special nested class for casting AGMACylindricalGearMaterial to subclasses."""

        def __init__(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
            parent: "AGMACylindricalGearMaterial",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
        ):
            return self._parent._cast(_591.CylindricalGearMaterial)

        @property
        def gear_material(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
        ):
            from mastapy.gears.materials import _594

            return self._parent._cast(_594.GearMaterial)

        @property
        def material(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
        ):
            from mastapy.materials import _269

            return self._parent._cast(_269.Material)

        @property
        def named_database_item(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
        ):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def agma_cylindrical_gear_material(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
        ) -> "AGMACylindricalGearMaterial":
            return self._parent

        def __getattr__(
            self: "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMACylindricalGearMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_bending.setter
    @enforce_parameter_types
    def allowable_stress_number_bending(self: Self, value: "float"):
        self.wrapped.AllowableStressNumberBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def grade(self: Self) -> "_242.AGMAMaterialGrade":
        """mastapy.materials.AGMAMaterialGrade"""
        temp = self.wrapped.Grade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.AGMAMaterialGrade"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._242", "AGMAMaterialGrade"
        )(value)

    @grade.setter
    @enforce_parameter_types
    def grade(self: Self, value: "_242.AGMAMaterialGrade"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.AGMAMaterialGrade"
        )
        self.wrapped.Grade = value

    @property
    def material_application(self: Self) -> "_240.AGMAMaterialApplications":
        """mastapy.materials.AGMAMaterialApplications"""
        temp = self.wrapped.MaterialApplication

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.AGMAMaterialApplications"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._240", "AGMAMaterialApplications"
        )(value)

    @material_application.setter
    @enforce_parameter_types
    def material_application(self: Self, value: "_240.AGMAMaterialApplications"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.AGMAMaterialApplications"
        )
        self.wrapped.MaterialApplication = value

    @property
    def material_class(self: Self) -> "_241.AGMAMaterialClasses":
        """mastapy.materials.AGMAMaterialClasses"""
        temp = self.wrapped.MaterialClass

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.AGMAMaterialClasses"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._241", "AGMAMaterialClasses"
        )(value)

    @material_class.setter
    @enforce_parameter_types
    def material_class(self: Self, value: "_241.AGMAMaterialClasses"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.AGMAMaterialClasses"
        )
        self.wrapped.MaterialClass = value

    @property
    def stress_cycle_factor_at_1e10_cycles_bending(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StressCycleFactorAt1E10CyclesBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @stress_cycle_factor_at_1e10_cycles_bending.setter
    @enforce_parameter_types
    def stress_cycle_factor_at_1e10_cycles_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StressCycleFactorAt1E10CyclesBending = value

    @property
    def stress_cycle_factor_at_1e10_cycles_contact(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StressCycleFactorAt1E10CyclesContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @stress_cycle_factor_at_1e10_cycles_contact.setter
    @enforce_parameter_types
    def stress_cycle_factor_at_1e10_cycles_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StressCycleFactorAt1E10CyclesContact = value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial":
        return self._Cast_AGMACylindricalGearMaterial(self)
