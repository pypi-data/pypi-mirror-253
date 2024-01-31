"""OptimizationStrategyBase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "OptimizationStrategyBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationStrategyBase",)


Self = TypeVar("Self", bound="OptimizationStrategyBase")


class OptimizationStrategyBase(_1829.NamedDatabaseItem):
    """OptimizationStrategyBase

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STRATEGY_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationStrategyBase")

    class _Cast_OptimizationStrategyBase:
        """Special nested class for casting OptimizationStrategyBase to subclasses."""

        def __init__(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
            parent: "OptimizationStrategyBase",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
        ):
            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
        ):
            from mastapy.system_model.optimization import _2226

            return self._parent._cast(_2226.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
        ):
            from mastapy.system_model.optimization import _2229

            return self._parent._cast(_2229.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
        ):
            from mastapy.system_model.optimization import _2234

            return self._parent._cast(_2234.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase",
        ) -> "OptimizationStrategyBase":
            return self._parent

        def __getattr__(
            self: "OptimizationStrategyBase._Cast_OptimizationStrategyBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationStrategyBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "OptimizationStrategyBase._Cast_OptimizationStrategyBase":
        return self._Cast_OptimizationStrategyBase(self)
