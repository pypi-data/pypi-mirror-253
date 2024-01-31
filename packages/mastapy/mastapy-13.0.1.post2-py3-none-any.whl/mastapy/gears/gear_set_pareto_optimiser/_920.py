"""MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="MicroGeometryGearSetDesignSpaceSearchStrategyDatabase")


class MicroGeometryGearSetDesignSpaceSearchStrategyDatabase(
    _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
):
    """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"
    )

    class _Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryGearSetDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
            parent: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            return self._parent._cast(
                _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
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
        instance_to_wrap: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
        return self._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase(self)
