"""GearManufacturingConfigurationViewModel"""
from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "GearManufacturingConfigurationViewModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearManufacturingConfigurationViewModel",)


Self = TypeVar("Self", bound="GearManufacturingConfigurationViewModel")


class GearManufacturingConfigurationViewModel(_0.APIBase):
    """GearManufacturingConfigurationViewModel

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearManufacturingConfigurationViewModel"
    )

    class _Cast_GearManufacturingConfigurationViewModel:
        """Special nested class for casting GearManufacturingConfigurationViewModel to subclasses."""

        def __init__(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
            parent: "GearManufacturingConfigurationViewModel",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model_placeholder(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(
                _629.GearManufacturingConfigurationViewModelPlaceholder
            )

        @property
        def hobbing_process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _674,
            )

            return self._parent._cast(_674.HobbingProcessSimulationViewModel)

        @property
        def process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _687,
            )

            return self._parent._cast(_687.ProcessSimulationViewModel)

        @property
        def worm_grinding_process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _701,
            )

            return self._parent._cast(_701.WormGrindingProcessSimulationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _754,
            )

            return self._parent._cast(_754.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _760,
            )

            return self._parent._cast(_760.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _770,
            )

            return self._parent._cast(_770.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _771,
            )

            return self._parent._cast(_771.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "GearManufacturingConfigurationViewModel":
            return self._parent

        def __getattr__(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
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
        self: Self, instance_to_wrap: "GearManufacturingConfigurationViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel":
        return self._Cast_GearManufacturingConfigurationViewModel(self)
