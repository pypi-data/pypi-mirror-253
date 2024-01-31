"""GearMeshImplementationAnalysisDutyCycle"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationAnalysisDutyCycle"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationAnalysisDutyCycle",)


Self = TypeVar("Self", bound="GearMeshImplementationAnalysisDutyCycle")


class GearMeshImplementationAnalysisDutyCycle(_1222.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshImplementationAnalysisDutyCycle"
    )

    class _Cast_GearMeshImplementationAnalysisDutyCycle:
        """Special nested class for casting GearMeshImplementationAnalysisDutyCycle to subclasses."""

        def __init__(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
            parent: "GearMeshImplementationAnalysisDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
        ):
            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
        ):
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
        ) -> "GearMeshImplementationAnalysisDutyCycle":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle",
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
        self: Self, instance_to_wrap: "GearMeshImplementationAnalysisDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle":
        return self._Cast_GearMeshImplementationAnalysisDutyCycle(self)
