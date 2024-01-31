"""LoadedRollerStripLoadResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerStripLoadResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerStripLoadResults",)


Self = TypeVar("Self", bound="LoadedRollerStripLoadResults")


class LoadedRollerStripLoadResults(_0.APIBase):
    """LoadedRollerStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerStripLoadResults")

    class _Cast_LoadedRollerStripLoadResults:
        """Special nested class for casting LoadedRollerStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            parent: "LoadedRollerStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1981

            return self._parent._cast(
                _1981.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1991

            return self._parent._cast(
                _1991.LoadedAsymmetricSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2026

            return self._parent._cast(
                _2026.LoadedNonBarrelRollerBearingStripLoadResults
            )

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(
                _2042.LoadedSphericalRollerRadialBearingStripLoadResults
            )

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "LoadedRollerStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerStripLoadResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults":
        return self._Cast_LoadedRollerStripLoadResults(self)
