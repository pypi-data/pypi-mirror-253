"""BackwardEulerAccelerationStepHalvingTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BACKWARD_EULER_ACCELERATION_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers",
    "BackwardEulerAccelerationStepHalvingTransientSolver",
)


__docformat__ = "restructuredtext en"
__all__ = ("BackwardEulerAccelerationStepHalvingTransientSolver",)


Self = TypeVar("Self", bound="BackwardEulerAccelerationStepHalvingTransientSolver")


class BackwardEulerAccelerationStepHalvingTransientSolver(
    _110.SimpleAccelerationBasedStepHalvingTransientSolver
):
    """BackwardEulerAccelerationStepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _BACKWARD_EULER_ACCELERATION_STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BackwardEulerAccelerationStepHalvingTransientSolver"
    )

    class _Cast_BackwardEulerAccelerationStepHalvingTransientSolver:
        """Special nested class for casting BackwardEulerAccelerationStepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
            parent: "BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            return self._parent._cast(
                _110.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
        ) -> "BackwardEulerAccelerationStepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver",
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
        instance_to_wrap: "BackwardEulerAccelerationStepHalvingTransientSolver.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BackwardEulerAccelerationStepHalvingTransientSolver._Cast_BackwardEulerAccelerationStepHalvingTransientSolver":
        return self._Cast_BackwardEulerAccelerationStepHalvingTransientSolver(self)
