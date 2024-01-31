"""NewmarkTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWMARK_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewmarkTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("NewmarkTransientSolver",)


Self = TypeVar("Self", bound="NewmarkTransientSolver")


class NewmarkTransientSolver(_111.SimpleVelocityBasedStepHalvingTransientSolver):
    """NewmarkTransientSolver

    This is a mastapy class.
    """

    TYPE = _NEWMARK_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewmarkTransientSolver")

    class _Cast_NewmarkTransientSolver:
        """Special nested class for casting NewmarkTransientSolver to subclasses."""

        def __init__(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
            parent: "NewmarkTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ):
            return self._parent._cast(
                _111.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def newmark_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "NewmarkTransientSolver":
            return self._parent

        def __getattr__(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NewmarkTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NewmarkTransientSolver._Cast_NewmarkTransientSolver":
        return self._Cast_NewmarkTransientSolver(self)
