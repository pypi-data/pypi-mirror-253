"""FractionMeasurementBase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRACTION_MEASUREMENT_BASE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "FractionMeasurementBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("FractionMeasurementBase",)


Self = TypeVar("Self", bound="FractionMeasurementBase")


class FractionMeasurementBase(_1605.MeasurementBase):
    """FractionMeasurementBase

    This is a mastapy class.
    """

    TYPE = _FRACTION_MEASUREMENT_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FractionMeasurementBase")

    class _Cast_FractionMeasurementBase:
        """Special nested class for casting FractionMeasurementBase to subclasses."""

        def __init__(
            self: "FractionMeasurementBase._Cast_FractionMeasurementBase",
            parent: "FractionMeasurementBase",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "FractionMeasurementBase._Cast_FractionMeasurementBase",
        ):
            return self._parent._cast(_1605.MeasurementBase)

        @property
        def damage(self: "FractionMeasurementBase._Cast_FractionMeasurementBase"):
            from mastapy.utility.units_and_measurements.measurements import _1628

            return self._parent._cast(_1628.Damage)

        @property
        def percentage(self: "FractionMeasurementBase._Cast_FractionMeasurementBase"):
            from mastapy.utility.units_and_measurements.measurements import _1689

            return self._parent._cast(_1689.Percentage)

        @property
        def fraction_measurement_base(
            self: "FractionMeasurementBase._Cast_FractionMeasurementBase",
        ) -> "FractionMeasurementBase":
            return self._parent

        def __getattr__(
            self: "FractionMeasurementBase._Cast_FractionMeasurementBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FractionMeasurementBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FractionMeasurementBase._Cast_FractionMeasurementBase":
        return self._Cast_FractionMeasurementBase(self)
