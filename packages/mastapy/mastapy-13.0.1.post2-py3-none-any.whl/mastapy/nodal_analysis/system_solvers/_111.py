"""SimpleVelocityBasedStepHalvingTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_VELOCITY_BASED_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers",
    "SimpleVelocityBasedStepHalvingTransientSolver",
)


__docformat__ = "restructuredtext en"
__all__ = ("SimpleVelocityBasedStepHalvingTransientSolver",)


Self = TypeVar("Self", bound="SimpleVelocityBasedStepHalvingTransientSolver")


class SimpleVelocityBasedStepHalvingTransientSolver(_116.StepHalvingTransientSolver):
    """SimpleVelocityBasedStepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _SIMPLE_VELOCITY_BASED_STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SimpleVelocityBasedStepHalvingTransientSolver"
    )

    class _Cast_SimpleVelocityBasedStepHalvingTransientSolver:
        """Special nested class for casting SimpleVelocityBasedStepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
            parent: "SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def step_halving_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def backward_euler_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _101

            return self._parent._cast(_101.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.LobattoIIIATransientSolver)

        @property
        def newmark_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
        ) -> "SimpleVelocityBasedStepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver",
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
        instance_to_wrap: "SimpleVelocityBasedStepHalvingTransientSolver.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver":
        return self._Cast_SimpleVelocityBasedStepHalvingTransientSolver(self)
