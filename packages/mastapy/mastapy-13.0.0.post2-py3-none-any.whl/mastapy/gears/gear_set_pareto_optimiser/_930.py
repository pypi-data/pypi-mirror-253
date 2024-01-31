"""ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_HYPOID_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase")


class ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase(
    _923.ParetoConicalRatingOptimisationStrategyDatabase
):
    """ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_HYPOID_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            return self._parent._cast(
                _923.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
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
        self: Self,
        instance_to_wrap: "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
        return self._Cast_ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase(self)
