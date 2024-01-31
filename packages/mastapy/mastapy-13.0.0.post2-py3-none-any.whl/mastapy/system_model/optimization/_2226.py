"""ConicalGearOptimisationStrategy"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.optimization import _2234
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "ConicalGearOptimisationStrategy"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearOptimisationStrategy",)


Self = TypeVar("Self", bound="ConicalGearOptimisationStrategy")


class ConicalGearOptimisationStrategy(
    _2234.OptimizationStrategy["_2227.ConicalGearOptimizationStep"]
):
    """ConicalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMISATION_STRATEGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearOptimisationStrategy")

    class _Cast_ConicalGearOptimisationStrategy:
        """Special nested class for casting ConicalGearOptimisationStrategy to subclasses."""

        def __init__(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
            parent: "ConicalGearOptimisationStrategy",
        ):
            self._parent = parent

        @property
        def optimization_strategy(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ):
            return self._parent._cast(_2234.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ):
            from mastapy.system_model.optimization import _2235

            return self._parent._cast(_2235.OptimizationStrategyBase)

        @property
        def named_database_item(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
        ) -> "ConicalGearOptimisationStrategy":
            return self._parent

        def __getattr__(
            self: "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearOptimisationStrategy.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy":
        return self._Cast_ConicalGearOptimisationStrategy(self)
