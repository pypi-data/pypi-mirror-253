"""MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_GEAR_SET_DUTY_CYCLE_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = (
    python_net_import(
        "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
        "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    )
)


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",)


Self = TypeVar(
    "Self", bound="MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"
)


class MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase(
    _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
):
    """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DUTY_CYCLE_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    )

    class _Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
            parent: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            return self._parent._cast(
                _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def design_space_search_strategy_database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
        ) -> "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
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
        instance_to_wrap: "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
        return (
            self._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase(
                self
            )
        )
