"""ElectricMachineHarmonicLoadData"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.harmonic_load_data import _1381, _1377
from mastapy.system_model.analyses_and_results.static_loads import _6976
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadData",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1512


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadData",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadData")


class ElectricMachineHarmonicLoadData(_1377.ElectricMachineHarmonicLoadDataBase):
    """ElectricMachineHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadData")

    class _Cast_ElectricMachineHarmonicLoadData:
        """Special nested class for casting ElectricMachineHarmonicLoadData to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
            parent: "ElectricMachineHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            return self._parent._cast(_1377.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1382

            return self._parent._cast(_1382.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1379

            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(
                _6877.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
        ) -> "ElectricMachineHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_to_all_data_types(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyToAllDataTypes

        if temp is None:
            return False

        return temp

    @apply_to_all_data_types.setter
    @enforce_parameter_types
    def apply_to_all_data_types(self: Self, value: "bool"):
        self.wrapped.ApplyToAllDataTypes = bool(value) if value is not None else False

    @property
    def apply_to_all_speeds_for_selected_data_type(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyToAllSpeedsForSelectedDataType

        if temp is None:
            return False

        return temp

    @apply_to_all_speeds_for_selected_data_type.setter
    @enforce_parameter_types
    def apply_to_all_speeds_for_selected_data_type(self: Self, value: "bool"):
        self.wrapped.ApplyToAllSpeedsForSelectedDataType = (
            bool(value) if value is not None else False
        )

    @property
    def constant_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConstantTorque

        if temp is None:
            return 0.0

        return temp

    @constant_torque.setter
    @enforce_parameter_types
    def constant_torque(self: Self, value: "float"):
        self.wrapped.ConstantTorque = float(value) if value is not None else 0.0

    @property
    def data_type_for_scaling(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType":
        """EnumWithSelectedValue[mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType]"""
        temp = self.wrapped.DataTypeForScaling

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @data_type_for_scaling.setter
    @enforce_parameter_types
    def data_type_for_scaling(self: Self, value: "_1381.HarmonicLoadDataType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForScaling = value

    @property
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: Self, value: "float"
    ):
        self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_x_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorXForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_x_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_x_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorXForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_y_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorYForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_y_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_y_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorYForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_z_force_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotorZForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_z_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_z_force_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.RotorZForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def scale(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    @enforce_parameter_types
    def scale(self: Self, value: "float"):
        self.wrapped.Scale = float(value) if value is not None else 0.0

    @property
    def torque_ripple_amplitude_cut_off(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueRippleAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @torque_ripple_amplitude_cut_off.setter
    @enforce_parameter_types
    def torque_ripple_amplitude_cut_off(self: Self, value: "float"):
        self.wrapped.TorqueRippleAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def torque_ripple_input_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.TorqueRippleInputType]"""
        temp = self.wrapped.TorqueRippleInputType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @torque_ripple_input_type.setter
    @enforce_parameter_types
    def torque_ripple_input_type(self: Self, value: "_6976.TorqueRippleInputType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueRippleInputType = value

    @property
    def use_stator_radius_from_masta_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseStatorRadiusFromMASTAModel

        if temp is None:
            return False

        return temp

    @use_stator_radius_from_masta_model.setter
    @enforce_parameter_types
    def use_stator_radius_from_masta_model(self: Self, value: "bool"):
        self.wrapped.UseStatorRadiusFromMASTAModel = (
            bool(value) if value is not None else False
        )

    @property
    def excitations(self: Self) -> "List[_1512.FourierSeries]":
        """List[mastapy.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData":
        return self._Cast_ElectricMachineHarmonicLoadData(self)
