"""LoadedBearingTemperatureChart"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1756
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_TEMPERATURE_CHART = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingTemperatureChart"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBearingTemperatureChart",)


Self = TypeVar("Self", bound="LoadedBearingTemperatureChart")


class LoadedBearingTemperatureChart(_1756.CustomReportChart):
    """LoadedBearingTemperatureChart

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_TEMPERATURE_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBearingTemperatureChart")

    class _Cast_LoadedBearingTemperatureChart:
        """Special nested class for casting LoadedBearingTemperatureChart to subclasses."""

        def __init__(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
            parent: "LoadedBearingTemperatureChart",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ):
            return self._parent._cast(_1756.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ):
            pass

            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ):
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ):
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ):
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def loaded_bearing_temperature_chart(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
        ) -> "LoadedBearingTemperatureChart":
            return self._parent

        def __getattr__(
            self: "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBearingTemperatureChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumTemperature

        if temp is None:
            return 0.0

        return temp

    @maximum_temperature.setter
    @enforce_parameter_types
    def maximum_temperature(self: Self, value: "float"):
        self.wrapped.MaximumTemperature = float(value) if value is not None else 0.0

    @property
    def minimum_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTemperature

        if temp is None:
            return 0.0

        return temp

    @minimum_temperature.setter
    @enforce_parameter_types
    def minimum_temperature(self: Self, value: "float"):
        self.wrapped.MinimumTemperature = float(value) if value is not None else 0.0

    @property
    def number_of_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSteps

        if temp is None:
            return 0

        return temp

    @number_of_steps.setter
    @enforce_parameter_types
    def number_of_steps(self: Self, value: "int"):
        self.wrapped.NumberOfSteps = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart":
        return self._Cast_LoadedBearingTemperatureChart(self)
