"""KlingelnbergCycloPalloidConicalGearMaterial"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.materials import _594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "KlingelnbergCycloPalloidConicalGearMaterial"
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMaterial",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMaterial")


class KlingelnbergCycloPalloidConicalGearMaterial(_594.GearMaterial):
    """KlingelnbergCycloPalloidConicalGearMaterial

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MATERIAL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearMaterial"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMaterial:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMaterial to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
            parent: "KlingelnbergCycloPalloidConicalGearMaterial",
        ):
            self._parent = parent

        @property
        def gear_material(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
        ):
            return self._parent._cast(_594.GearMaterial)

        @property
        def material(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
        ):
            from mastapy.materials import _269

            return self._parent._cast(_269.Material)

        @property
        def named_database_item(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
        ):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
        ) -> "KlingelnbergCycloPalloidConicalGearMaterial":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMaterial.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def specify_allowable_stress_numbers(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumbers

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_numbers.setter
    @enforce_parameter_types
    def specify_allowable_stress_numbers(self: Self, value: "bool"):
        self.wrapped.SpecifyAllowableStressNumbers = (
            bool(value) if value is not None else False
        )

    @property
    def stress_number_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressNumberBending

        if temp is None:
            return 0.0

        return temp

    @stress_number_bending.setter
    @enforce_parameter_types
    def stress_number_bending(self: Self, value: "float"):
        self.wrapped.StressNumberBending = float(value) if value is not None else 0.0

    @property
    def stress_number_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressNumberContact

        if temp is None:
            return 0.0

        return temp

    @stress_number_contact.setter
    @enforce_parameter_types
    def stress_number_contact(self: Self, value: "float"):
        self.wrapped.StressNumberContact = float(value) if value is not None else 0.0

    @property
    def stress_number_static_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressNumberStaticBending

        if temp is None:
            return 0.0

        return temp

    @stress_number_static_bending.setter
    @enforce_parameter_types
    def stress_number_static_bending(self: Self, value: "float"):
        self.wrapped.StressNumberStaticBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def stress_number_static_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressNumberStaticContact

        if temp is None:
            return 0.0

        return temp

    @stress_number_static_contact.setter
    @enforce_parameter_types
    def stress_number_static_contact(self: Self, value: "float"):
        self.wrapped.StressNumberStaticContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMaterial(self)
