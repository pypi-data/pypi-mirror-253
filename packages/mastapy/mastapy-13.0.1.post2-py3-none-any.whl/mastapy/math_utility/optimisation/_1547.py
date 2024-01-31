"""ParetoOptimisationInput"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.math_utility.optimisation import _1553
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_INPUT = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationInput"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1488
    from mastapy.math_utility.optimisation import _1557


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationInput",)


Self = TypeVar("Self", bound="ParetoOptimisationInput")


class ParetoOptimisationInput(_1553.ParetoOptimisationVariable):
    """ParetoOptimisationInput

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationInput")

    class _Cast_ParetoOptimisationInput:
        """Special nested class for casting ParetoOptimisationInput to subclasses."""

        def __init__(
            self: "ParetoOptimisationInput._Cast_ParetoOptimisationInput",
            parent: "ParetoOptimisationInput",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_variable(
            self: "ParetoOptimisationInput._Cast_ParetoOptimisationInput",
        ):
            return self._parent._cast(_1553.ParetoOptimisationVariable)

        @property
        def pareto_optimisation_variable_base(
            self: "ParetoOptimisationInput._Cast_ParetoOptimisationInput",
        ):
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_input(
            self: "ParetoOptimisationInput._Cast_ParetoOptimisationInput",
        ) -> "ParetoOptimisationInput":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationInput._Cast_ParetoOptimisationInput", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationInput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def range(self: Self) -> "_1488.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @range.setter
    @enforce_parameter_types
    def range(self: Self, value: "_1488.Range"):
        self.wrapped.Range = value.wrapped

    @property
    def specify_input_range_as(self: Self) -> "_1557.SpecifyOptimisationInputAs":
        """mastapy.math_utility.optimisation.SpecifyOptimisationInputAs"""
        temp = self.wrapped.SpecifyInputRangeAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.optimisation._1557", "SpecifyOptimisationInputAs"
        )(value)

    @specify_input_range_as.setter
    @enforce_parameter_types
    def specify_input_range_as(self: Self, value: "_1557.SpecifyOptimisationInputAs"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )
        self.wrapped.SpecifyInputRangeAs = value

    @property
    def cast_to(self: Self) -> "ParetoOptimisationInput._Cast_ParetoOptimisationInput":
        return self._Cast_ParetoOptimisationInput(self)
