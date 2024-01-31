"""DesignSpaceSearchStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "DesignSpaceSearchStrategyDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="DesignSpaceSearchStrategyDatabase")


class DesignSpaceSearchStrategyDatabase(
    _1828.NamedDatabase["_1549.ParetoOptimisationStrategy"]
):
    """DesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignSpaceSearchStrategyDatabase")

    class _Cast_DesignSpaceSearchStrategyDatabase:
        """Special nested class for casting DesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
            parent: "DesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _920

            return self._parent._cast(
                _920.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _923

            return self._parent._cast(
                _923.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(_929.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(
                _933.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1541

            return self._parent._cast(
                _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "DesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
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
        self: Self, instance_to_wrap: "DesignSpaceSearchStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase":
        return self._Cast_DesignSpaceSearchStrategyDatabase(self)
