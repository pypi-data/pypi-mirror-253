"""LoadedToroidalRollerBearingStripLoadResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2042
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedToroidalRollerBearingStripLoadResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedToroidalRollerBearingStripLoadResults",)


Self = TypeVar("Self", bound="LoadedToroidalRollerBearingStripLoadResults")


class LoadedToroidalRollerBearingStripLoadResults(
    _2042.LoadedSphericalRollerRadialBearingStripLoadResults
):
    """LoadedToroidalRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedToroidalRollerBearingStripLoadResults"
    )

    class _Cast_LoadedToroidalRollerBearingStripLoadResults:
        """Special nested class for casting LoadedToroidalRollerBearingStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
            parent: "LoadedToroidalRollerBearingStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
        ):
            return self._parent._cast(
                _2042.LoadedSphericalRollerRadialBearingStripLoadResults
            )

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1981

            return self._parent._cast(
                _1981.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollerStripLoadResults)

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
        ) -> "LoadedToroidalRollerBearingStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults",
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
        self: Self, instance_to_wrap: "LoadedToroidalRollerBearingStripLoadResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedToroidalRollerBearingStripLoadResults._Cast_LoadedToroidalRollerBearingStripLoadResults":
        return self._Cast_LoadedToroidalRollerBearingStripLoadResults(self)
