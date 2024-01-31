"""ParetoConicalRatingOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CONICAL_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoConicalRatingOptimisationStrategyDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParetoConicalRatingOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoConicalRatingOptimisationStrategyDatabase")


class ParetoConicalRatingOptimisationStrategyDatabase(
    _1552.ParetoOptimisationStrategyDatabase
):
    """ParetoConicalRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CONICAL_RATING_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoConicalRatingOptimisationStrategyDatabase"
    )

    class _Cast_ParetoConicalRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoConicalRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
            parent: "ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            return self._parent._cast(_1552.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(
                _933.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
        ) -> "ParetoConicalRatingOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoConicalRatingOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase":
        return self._Cast_ParetoConicalRatingOptimisationStrategyDatabase(self)
