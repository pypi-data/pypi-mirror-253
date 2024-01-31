"""StepHalvingTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _104
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "StepHalvingTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("StepHalvingTransientSolver",)


Self = TypeVar("Self", bound="StepHalvingTransientSolver")


class StepHalvingTransientSolver(_104.InternalTransientSolver):
    """StepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StepHalvingTransientSolver")

    class _Cast_StepHalvingTransientSolver:
        """Special nested class for casting StepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            parent: "StepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def internal_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _100

            return self._parent._cast(
                _100.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def backward_euler_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _101

            return self._parent._cast(_101.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.NewmarkTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(
                _110.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _111

            return self._parent._cast(
                _111.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def wilson_theta_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.WilsonThetaTransientSolver)

        @property
        def step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "StepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StepHalvingTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver":
        return self._Cast_StepHalvingTransientSolver(self)
