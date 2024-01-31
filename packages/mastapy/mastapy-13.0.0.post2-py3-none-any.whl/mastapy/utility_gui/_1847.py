"""ColumnInputOptions"""
from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.file_access_helpers import _1817
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements import _1610
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "ColumnInputOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("ColumnInputOptions",)


Self = TypeVar("Self", bound="ColumnInputOptions")


class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE = _COLUMN_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ColumnInputOptions")

    class _Cast_ColumnInputOptions:
        """Special nested class for casting ColumnInputOptions to subclasses."""

        def __init__(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
            parent: "ColumnInputOptions",
        ):
            self._parent = parent

        @property
        def boost_pressure_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2555,
            )

            return self._parent._cast(_2555.BoostPressureInputOptions)

        @property
        def input_power_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2556,
            )

            return self._parent._cast(_2556.InputPowerInputOptions)

        @property
        def pressure_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2557,
            )

            return self._parent._cast(_2557.PressureRatioInputOptions)

        @property
        def rotor_speed_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2560,
            )

            return self._parent._cast(_2560.RotorSpeedInputOptions)

        @property
        def boost_pressure_load_case_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6989,
            )

            return self._parent._cast(_6989.BoostPressureLoadCaseInputOptions)

        @property
        def design_state_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6990,
            )

            return self._parent._cast(_6990.DesignStateOptions)

        @property
        def force_input_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6992,
            )

            return self._parent._cast(_6992.ForceInputOptions)

        @property
        def gear_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6993,
            )

            return self._parent._cast(_6993.GearRatioInputOptions)

        @property
        def load_case_name_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6994,
            )

            return self._parent._cast(_6994.LoadCaseNameOptions)

        @property
        def moment_input_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6995,
            )

            return self._parent._cast(_6995.MomentInputOptions)

        @property
        def point_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6997,
            )

            return self._parent._cast(_6997.PointLoadInputOptions)

        @property
        def power_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6998,
            )

            return self._parent._cast(_6998.PowerLoadInputOptions)

        @property
        def ramp_or_steady_state_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6999,
            )

            return self._parent._cast(_6999.RampOrSteadyStateInputOptions)

        @property
        def speed_input_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7000,
            )

            return self._parent._cast(_7000.SpeedInputOptions)

        @property
        def time_step_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7002,
            )

            return self._parent._cast(_7002.TimeStepInputOptions)

        @property
        def torque_input_options(self: "ColumnInputOptions._Cast_ColumnInputOptions"):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7003,
            )

            return self._parent._cast(_7003.TorqueInputOptions)

        @property
        def column_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "ColumnInputOptions":
            return self._parent

        def __getattr__(self: "ColumnInputOptions._Cast_ColumnInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ColumnInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ColumnTitle":
        """ListWithSelectedItem[mastapy.utility.file_access_helpers.ColumnTitle]"""
        temp = self.wrapped.Column

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ColumnTitle",
        )(temp)

    @column.setter
    @enforce_parameter_types
    def column(self: Self, value: "_1817.ColumnTitle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Column = value

    @property
    def unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.Unit

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @unit.setter
    @enforce_parameter_types
    def unit(self: Self, value: "_1610.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Unit = value

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
    def cast_to(self: Self) -> "ColumnInputOptions._Cast_ColumnInputOptions":
        return self._Cast_ColumnInputOptions(self)
