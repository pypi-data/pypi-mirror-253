"""ReportingOptimizationInput"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REPORTING_OPTIMIZATION_INPUT = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ReportingOptimizationInput"
)


__docformat__ = "restructuredtext en"
__all__ = ("ReportingOptimizationInput",)


Self = TypeVar("Self", bound="ReportingOptimizationInput")


class ReportingOptimizationInput(_1544.OptimizationInput):
    """ReportingOptimizationInput

    This is a mastapy class.
    """

    TYPE = _REPORTING_OPTIMIZATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ReportingOptimizationInput")

    class _Cast_ReportingOptimizationInput:
        """Special nested class for casting ReportingOptimizationInput to subclasses."""

        def __init__(
            self: "ReportingOptimizationInput._Cast_ReportingOptimizationInput",
            parent: "ReportingOptimizationInput",
        ):
            self._parent = parent

        @property
        def optimization_input(
            self: "ReportingOptimizationInput._Cast_ReportingOptimizationInput",
        ):
            return self._parent._cast(_1544.OptimizationInput)

        @property
        def optimization_variable(
            self: "ReportingOptimizationInput._Cast_ReportingOptimizationInput",
        ):
            from mastapy.math_utility.optimisation import _1545

            return self._parent._cast(_1545.OptimizationVariable)

        @property
        def reporting_optimization_input(
            self: "ReportingOptimizationInput._Cast_ReportingOptimizationInput",
        ) -> "ReportingOptimizationInput":
            return self._parent

        def __getattr__(
            self: "ReportingOptimizationInput._Cast_ReportingOptimizationInput",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ReportingOptimizationInput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ReportingOptimizationInput._Cast_ReportingOptimizationInput":
        return self._Cast_ReportingOptimizationInput(self)
