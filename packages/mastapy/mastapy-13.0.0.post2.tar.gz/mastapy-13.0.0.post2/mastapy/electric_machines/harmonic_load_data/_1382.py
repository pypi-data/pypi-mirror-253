"""SpeedDependentHarmonicLoadData"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.electric_machines.harmonic_load_data import _1379
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_DEPENDENT_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "SpeedDependentHarmonicLoadData"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpeedDependentHarmonicLoadData",)


Self = TypeVar("Self", bound="SpeedDependentHarmonicLoadData")


class SpeedDependentHarmonicLoadData(_1379.HarmonicLoadDataBase):
    """SpeedDependentHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _SPEED_DEPENDENT_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedDependentHarmonicLoadData")

    class _Cast_SpeedDependentHarmonicLoadData:
        """Special nested class for casting SpeedDependentHarmonicLoadData to subclasses."""

        def __init__(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
            parent: "SpeedDependentHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_base(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.electric_machines.results import _1320

            return self._parent._cast(_1320.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1377

            return self._parent._cast(_1377.ElectricMachineHarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(
                _6877.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def point_load_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PointLoadHarmonicLoadData)

        @property
        def unbalanced_mass_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.UnbalancedMassHarmonicLoadData)

        @property
        def speed_dependent_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "SpeedDependentHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedDependentHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_speed(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_float":
        """ListWithSelectedItem[float]"""
        temp = self.wrapped.SelectedSpeed

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_float",
        )(temp)

    @selected_speed.setter
    @enforce_parameter_types
    def selected_speed(self: Self, value: "float"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0
        )
        self.wrapped.SelectedSpeed = value

    @property
    def show_all_speeds(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllSpeeds

        if temp is None:
            return False

        return temp

    @show_all_speeds.setter
    @enforce_parameter_types
    def show_all_speeds(self: Self, value: "bool"):
        self.wrapped.ShowAllSpeeds = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData":
        return self._Cast_SpeedDependentHarmonicLoadData(self)
