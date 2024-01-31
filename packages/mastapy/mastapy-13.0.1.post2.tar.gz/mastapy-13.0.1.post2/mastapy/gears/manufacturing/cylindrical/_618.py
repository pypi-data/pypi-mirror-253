"""CylindricalManufacturedGearMeshDutyCycle"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearMeshDutyCycle",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearMeshDutyCycle",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearMeshDutyCycle")


class CylindricalManufacturedGearMeshDutyCycle(
    _1224.GearMeshImplementationAnalysisDutyCycle
):
    """CylindricalManufacturedGearMeshDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalManufacturedGearMeshDutyCycle"
    )

    class _Cast_CylindricalManufacturedGearMeshDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearMeshDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
            parent: "CylindricalManufacturedGearMeshDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
        ):
            return self._parent._cast(_1224.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
        ) -> "CylindricalManufacturedGearMeshDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearMeshDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle":
        return self._Cast_CylindricalManufacturedGearMeshDutyCycle(self)
