"""LoadedAxialThrustNeedleRollerBearingElement"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _1993
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustNeedleRollerBearingElement",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustNeedleRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedAxialThrustNeedleRollerBearingElement")


class LoadedAxialThrustNeedleRollerBearingElement(
    _1993.LoadedAxialThrustCylindricalRollerBearingElement
):
    """LoadedAxialThrustNeedleRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustNeedleRollerBearingElement"
    )

    class _Cast_LoadedAxialThrustNeedleRollerBearingElement:
        """Special nested class for casting LoadedAxialThrustNeedleRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
            parent: "LoadedAxialThrustNeedleRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
        ):
            return self._parent._cast(
                _1993.LoadedAxialThrustCylindricalRollerBearingElement
            )

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
        ) -> "LoadedAxialThrustNeedleRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedAxialThrustNeedleRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement":
        return self._Cast_LoadedAxialThrustNeedleRollerBearingElement(self)
