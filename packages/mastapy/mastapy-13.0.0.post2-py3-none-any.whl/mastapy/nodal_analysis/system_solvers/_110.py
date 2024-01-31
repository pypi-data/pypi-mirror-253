"""SimpleAccelerationBasedStepHalvingTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_ACCELERATION_BASED_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers",
    "SimpleAccelerationBasedStepHalvingTransientSolver",
)


__docformat__ = "restructuredtext en"
__all__ = ("SimpleAccelerationBasedStepHalvingTransientSolver",)


Self = TypeVar("Self", bound="SimpleAccelerationBasedStepHalvingTransientSolver")


class SimpleAccelerationBasedStepHalvingTransientSolver(
    _116.StepHalvingTransientSolver
):
    """SimpleAccelerationBasedStepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _SIMPLE_ACCELERATION_BASED_STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SimpleAccelerationBasedStepHalvingTransientSolver"
    )

    class _Cast_SimpleAccelerationBasedStepHalvingTransientSolver:
        """Special nested class for casting SimpleAccelerationBasedStepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
            parent: "SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _100

            return self._parent._cast(
                _100.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def newmark_acceleration_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.NewmarkAccelerationTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "SimpleAccelerationBasedStepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
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
        instance_to_wrap: "SimpleAccelerationBasedStepHalvingTransientSolver.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver":
        return self._Cast_SimpleAccelerationBasedStepHalvingTransientSolver(self)
