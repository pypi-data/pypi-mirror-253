"""CylindricalPlanetGearFromCAD"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.import_from_cad import _2499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "CylindricalPlanetGearFromCAD"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearFromCAD",)


Self = TypeVar("Self", bound="CylindricalPlanetGearFromCAD")


class CylindricalPlanetGearFromCAD(_2499.CylindricalGearInPlanetarySetFromCAD):
    """CylindricalPlanetGearFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearFromCAD")

    class _Cast_CylindricalPlanetGearFromCAD:
        """Special nested class for casting CylindricalPlanetGearFromCAD to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
            parent: "CylindricalPlanetGearFromCAD",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
        ):
            return self._parent._cast(_2499.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_gear_from_cad(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2498

            return self._parent._cast(_2498.CylindricalGearFromCAD)

        @property
        def mountable_component_from_cad(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2504

            return self._parent._cast(_2504.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2495

            return self._parent._cast(_2495.ComponentFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
        ) -> "CylindricalPlanetGearFromCAD":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalPlanetGearFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearFromCAD._Cast_CylindricalPlanetGearFromCAD":
        return self._Cast_CylindricalPlanetGearFromCAD(self)
