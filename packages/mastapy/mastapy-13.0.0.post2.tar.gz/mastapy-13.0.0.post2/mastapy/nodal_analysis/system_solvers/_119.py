"""WilsonThetaTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WILSON_THETA_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "WilsonThetaTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("WilsonThetaTransientSolver",)


Self = TypeVar("Self", bound="WilsonThetaTransientSolver")


class WilsonThetaTransientSolver(_116.StepHalvingTransientSolver):
    """WilsonThetaTransientSolver

    This is a mastapy class.
    """

    TYPE = _WILSON_THETA_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WilsonThetaTransientSolver")

    class _Cast_WilsonThetaTransientSolver:
        """Special nested class for casting WilsonThetaTransientSolver to subclasses."""

        def __init__(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
            parent: "WilsonThetaTransientSolver",
        ):
            self._parent = parent

        @property
        def step_halving_transient_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ):
            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def wilson_theta_transient_solver(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
        ) -> "WilsonThetaTransientSolver":
            return self._parent

        def __getattr__(
            self: "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WilsonThetaTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WilsonThetaTransientSolver._Cast_WilsonThetaTransientSolver":
        return self._Cast_WilsonThetaTransientSolver(self)
