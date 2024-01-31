"""ProcessCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "ProcessCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _685,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ProcessCalculation",)


Self = TypeVar("Self", bound="ProcessCalculation")


class ProcessCalculation(_0.APIBase):
    """ProcessCalculation

    This is a mastapy class.
    """

    TYPE = _PROCESS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProcessCalculation")

    class _Cast_ProcessCalculation:
        """Special nested class for casting ProcessCalculation to subclasses."""

        def __init__(
            self: "ProcessCalculation._Cast_ProcessCalculation",
            parent: "ProcessCalculation",
        ):
            self._parent = parent

        @property
        def hobbing_process_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _666,
            )

            return self._parent._cast(_666.HobbingProcessCalculation)

        @property
        def hobbing_process_gear_shape(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _667,
            )

            return self._parent._cast(_667.HobbingProcessGearShape)

        @property
        def hobbing_process_lead_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _668,
            )

            return self._parent._cast(_668.HobbingProcessLeadCalculation)

        @property
        def hobbing_process_mark_on_shaft(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _669,
            )

            return self._parent._cast(_669.HobbingProcessMarkOnShaft)

        @property
        def hobbing_process_pitch_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _670,
            )

            return self._parent._cast(_670.HobbingProcessPitchCalculation)

        @property
        def hobbing_process_profile_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _671,
            )

            return self._parent._cast(_671.HobbingProcessProfileCalculation)

        @property
        def hobbing_process_total_modification_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _675,
            )

            return self._parent._cast(_675.HobbingProcessTotalModificationCalculation)

        @property
        def worm_grinding_cutter_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _692,
            )

            return self._parent._cast(_692.WormGrindingCutterCalculation)

        @property
        def worm_grinding_lead_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _693,
            )

            return self._parent._cast(_693.WormGrindingLeadCalculation)

        @property
        def worm_grinding_process_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _694,
            )

            return self._parent._cast(_694.WormGrindingProcessCalculation)

        @property
        def worm_grinding_process_gear_shape(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _695,
            )

            return self._parent._cast(_695.WormGrindingProcessGearShape)

        @property
        def worm_grinding_process_mark_on_shaft(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _696,
            )

            return self._parent._cast(_696.WormGrindingProcessMarkOnShaft)

        @property
        def worm_grinding_process_pitch_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _697,
            )

            return self._parent._cast(_697.WormGrindingProcessPitchCalculation)

        @property
        def worm_grinding_process_profile_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _698,
            )

            return self._parent._cast(_698.WormGrindingProcessProfileCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _702,
            )

            return self._parent._cast(
                _702.WormGrindingProcessTotalModificationCalculation
            )

        @property
        def process_calculation(
            self: "ProcessCalculation._Cast_ProcessCalculation",
        ) -> "ProcessCalculation":
            return self._parent

        def __getattr__(self: "ProcessCalculation._Cast_ProcessCalculation", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProcessCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_distance_parabolic_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistanceParabolicParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_gear_rotation_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterGearRotationRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_minimum_effective_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterMinimumEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def idle_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IdleDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_allowable_neck_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumAllowableNeckWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def neck_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NeckWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def setting_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SettingAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_mark_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftMarkLength

        if temp is None:
            return 0.0

        return temp

    @property
    def inputs(self: Self) -> "_685.ProcessSimulationInput":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessSimulationInput

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Inputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def calculate_idle_distance(self: Self):
        """Method does not return."""
        self.wrapped.CalculateIdleDistance()

    def calculate_left_modifications(self: Self):
        """Method does not return."""
        self.wrapped.CalculateLeftModifications()

    def calculate_left_total_modifications(self: Self):
        """Method does not return."""
        self.wrapped.CalculateLeftTotalModifications()

    def calculate_maximum_shaft_mark_length(self: Self):
        """Method does not return."""
        self.wrapped.CalculateMaximumShaftMarkLength()

    def calculate_modifications(self: Self):
        """Method does not return."""
        self.wrapped.CalculateModifications()

    def calculate_right_modifications(self: Self):
        """Method does not return."""
        self.wrapped.CalculateRightModifications()

    def calculate_right_total_modifications(self: Self):
        """Method does not return."""
        self.wrapped.CalculateRightTotalModifications()

    def calculate_shaft_mark(self: Self):
        """Method does not return."""
        self.wrapped.CalculateShaftMark()

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
    def cast_to(self: Self) -> "ProcessCalculation._Cast_ProcessCalculation":
        return self._Cast_ProcessCalculation(self)
