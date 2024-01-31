"""LobattoIIICTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOBATTO_IIIC_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "LobattoIIICTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("LobattoIIICTransientSolver",)


Self = TypeVar("Self", bound="LobattoIIICTransientSolver")


class LobattoIIICTransientSolver(_116.StepHalvingTransientSolver):
    """LobattoIIICTransientSolver

    This is a mastapy class.
    """

    TYPE = _LOBATTO_IIIC_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LobattoIIICTransientSolver")

    class _Cast_LobattoIIICTransientSolver:
        """Special nested class for casting LobattoIIICTransientSolver to subclasses."""

        def __init__(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
            parent: "LobattoIIICTransientSolver",
        ):
            self._parent = parent

        @property
        def step_halving_transient_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ):
            return self._parent._cast(_116.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver"):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def lobatto_iiic_transient_solver(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
        ) -> "LobattoIIICTransientSolver":
            return self._parent

        def __getattr__(
            self: "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LobattoIIICTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LobattoIIICTransientSolver._Cast_LobattoIIICTransientSolver":
        return self._Cast_LobattoIIICTransientSolver(self)
