"""LoadedSphericalRadialRollerBearingElement"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2039
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_RADIAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRadialRollerBearingElement",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRadialRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedSphericalRadialRollerBearingElement")


class LoadedSphericalRadialRollerBearingElement(
    _2039.LoadedSphericalRollerBearingElement
):
    """LoadedSphericalRadialRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_RADIAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRadialRollerBearingElement"
    )

    class _Cast_LoadedSphericalRadialRollerBearingElement:
        """Special nested class for casting LoadedSphericalRadialRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
            parent: "LoadedSphericalRadialRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
        ):
            return self._parent._cast(_2039.LoadedSphericalRollerBearingElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
        ):
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
        ) -> "LoadedSphericalRadialRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedSphericalRadialRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRadialRollerBearingElement._Cast_LoadedSphericalRadialRollerBearingElement":
        return self._Cast_LoadedSphericalRadialRollerBearingElement(self)
