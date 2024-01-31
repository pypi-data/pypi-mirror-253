"""LoadedAxialThrustCylindricalRollerBearingElement"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2027
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustCylindricalRollerBearingElement",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustCylindricalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedAxialThrustCylindricalRollerBearingElement")


class LoadedAxialThrustCylindricalRollerBearingElement(
    _2027.LoadedNonBarrelRollerElement
):
    """LoadedAxialThrustCylindricalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustCylindricalRollerBearingElement"
    )

    class _Cast_LoadedAxialThrustCylindricalRollerBearingElement:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
            parent: "LoadedAxialThrustCylindricalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
        ):
            return self._parent._cast(_2027.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(_1996.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
        ) -> "LoadedAxialThrustCylindricalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement",
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
        instance_to_wrap: "LoadedAxialThrustCylindricalRollerBearingElement.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustCylindricalRollerBearingElement._Cast_LoadedAxialThrustCylindricalRollerBearingElement":
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingElement(self)
