"""SemiImplicitTransientSolver"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _104
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SEMI_IMPLICIT_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "SemiImplicitTransientSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("SemiImplicitTransientSolver",)


Self = TypeVar("Self", bound="SemiImplicitTransientSolver")


class SemiImplicitTransientSolver(_104.InternalTransientSolver):
    """SemiImplicitTransientSolver

    This is a mastapy class.
    """

    TYPE = _SEMI_IMPLICIT_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SemiImplicitTransientSolver")

    class _Cast_SemiImplicitTransientSolver:
        """Special nested class for casting SemiImplicitTransientSolver to subclasses."""

        def __init__(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
            parent: "SemiImplicitTransientSolver",
        ):
            self._parent = parent

        @property
        def internal_transient_solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ):
            return self._parent._cast(_104.InternalTransientSolver)

        @property
        def transient_solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.TransientSolver)

        @property
        def dynamic_solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.DynamicSolver)

        @property
        def stiffness_solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StiffnessSolver)

        @property
        def solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ):
            from mastapy.nodal_analysis.system_solvers import _115

            return self._parent._cast(_115.Solver)

        @property
        def semi_implicit_transient_solver(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
        ) -> "SemiImplicitTransientSolver":
            return self._parent

        def __getattr__(
            self: "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SemiImplicitTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver":
        return self._Cast_SemiImplicitTransientSolver(self)
