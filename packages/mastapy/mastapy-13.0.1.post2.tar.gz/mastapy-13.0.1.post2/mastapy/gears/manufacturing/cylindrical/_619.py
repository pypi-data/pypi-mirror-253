"""CylindricalManufacturedGearMeshLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearMeshLoadCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearMeshLoadCase",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearMeshLoadCase")


class CylindricalManufacturedGearMeshLoadCase(_1223.GearMeshImplementationAnalysis):
    """CylindricalManufacturedGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalManufacturedGearMeshLoadCase"
    )

    class _Cast_CylindricalManufacturedGearMeshLoadCase:
        """Special nested class for casting CylindricalManufacturedGearMeshLoadCase to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
            parent: "CylindricalManufacturedGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
        ):
            return self._parent._cast(_1223.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
        ) -> "CylindricalManufacturedGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase":
        return self._Cast_CylindricalManufacturedGearMeshLoadCase(self)
