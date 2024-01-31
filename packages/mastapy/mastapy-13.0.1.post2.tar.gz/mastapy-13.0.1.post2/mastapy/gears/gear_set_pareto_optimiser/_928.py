"""ParetoFaceGearSetOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoFaceGearSetOptimisationStrategyDatabase")


class ParetoFaceGearSetOptimisationStrategyDatabase(
    _929.ParetoFaceRatingOptimisationStrategyDatabase
):
    """ParetoFaceGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoFaceGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoFaceGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
            parent: "ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            return self._parent._cast(_929.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "ParetoFaceGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoFaceGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoFaceGearSetOptimisationStrategyDatabase(self)
