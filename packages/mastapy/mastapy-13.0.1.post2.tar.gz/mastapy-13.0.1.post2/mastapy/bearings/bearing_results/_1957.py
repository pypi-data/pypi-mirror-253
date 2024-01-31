"""LoadedNonLinearBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _302, _303


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingResults")


class LoadedNonLinearBearingResults(_1949.LoadedBearingResults):
    """LoadedNonLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonLinearBearingResults")

    class _Cast_LoadedNonLinearBearingResults:
        """Special nested class for casting LoadedNonLinearBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            parent: "LoadedNonLinearBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1983

            return self._parent._cast(_1983.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1986

            return self._parent._cast(
                _1986.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1989

            return self._parent._cast(
                _1989.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1997

            return self._parent._cast(_1997.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2002

            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(_2005.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(_2012.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2036

            return self._parent._cast(_2036.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2119

            return self._parent._cast(_2119.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2120

            return self._parent._cast(_2120.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2121

            return self._parent._cast(_2121.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2122

            return self._parent._cast(_2122.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2124

            return self._parent._cast(_2124.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2128

            return self._parent._cast(_2128.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "LoadedNonLinearBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonLinearBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self: Self) -> "_302.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_303.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults":
        return self._Cast_LoadedNonLinearBearingResults(self)
