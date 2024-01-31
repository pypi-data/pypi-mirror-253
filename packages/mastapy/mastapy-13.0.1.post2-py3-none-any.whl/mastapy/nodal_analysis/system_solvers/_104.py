"""InternalTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERNAL_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "InternalTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("InternalTransientSolver",)


Self = TypeVar("Self", bound="InternalTransientSolver")


class InternalTransientSolver(_118.TransientSolver):
    """InternalTransientSolver

    This is a mastapy class.
    """

    TYPE = _INTERNAL_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InternalTransientSolver")

    class _Cast_InternalTransientSolver:
        """Special nested class for casting InternalTransientSolver to subclasses."""

        def __init__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
            parent: "InternalTransientSolver",
        ):
            self._parent = parent

        @property
        def transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self: "InternalTransientSolver._Cast_InternalTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _100

            return self._parent._cast(
                _100.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def backward_euler_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _101

            return self._parent._cast(_101.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.NewmarkTransientSolver)

        @property
        def semi_implicit_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.SemiImplicitTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(
                _110.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _111

            return self._parent._cast(
                _111.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.WilsonThetaTransientSolver)

        @property
        def internal_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "InternalTransientSolver":
            return self._parent

        def __getattr__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InternalTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InternalTransientSolver._Cast_InternalTransientSolver":
        return self._Cast_InternalTransientSolver(self)
