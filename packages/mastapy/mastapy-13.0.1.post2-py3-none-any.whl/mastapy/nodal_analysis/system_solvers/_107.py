"""NewmarkAccelerationTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWMARK_ACCELERATION_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewmarkAccelerationTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("NewmarkAccelerationTransientSolver",)


Self = TypeVar("Self", bound="NewmarkAccelerationTransientSolver")


class NewmarkAccelerationTransientSolver(
    _110.SimpleAccelerationBasedStepHalvingTransientSolver
):
    """NewmarkAccelerationTransientSolver

    This is a mastapy class.
    """

    TYPE = _NEWMARK_ACCELERATION_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewmarkAccelerationTransientSolver")

    class _Cast_NewmarkAccelerationTransientSolver:
        """Special nested class for casting NewmarkAccelerationTransientSolver to subclasses."""

        def __init__(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
            parent: "NewmarkAccelerationTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            return self._parent._cast(
                _110.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def newmark_acceleration_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "NewmarkAccelerationTransientSolver":
            return self._parent

        def __getattr__(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
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
        self: Self, instance_to_wrap: "NewmarkAccelerationTransientSolver.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver":
        return self._Cast_NewmarkAccelerationTransientSolver(self)
