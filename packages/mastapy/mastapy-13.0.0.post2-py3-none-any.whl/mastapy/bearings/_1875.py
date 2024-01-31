"""BearingLoadCaseResultsLightweight"""
from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingLoadCaseResultsLightweight"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCaseResultsLightweight",)


Self = TypeVar("Self", bound="BearingLoadCaseResultsLightweight")


class BearingLoadCaseResultsLightweight(_0.APIBase):
    """BearingLoadCaseResultsLightweight

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCaseResultsLightweight")

    class _Cast_BearingLoadCaseResultsLightweight:
        """Special nested class for casting BearingLoadCaseResultsLightweight to subclasses."""

        def __init__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            parent: "BearingLoadCaseResultsLightweight",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_for_pst(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings import _1874

            return self._parent._cast(_1874.BearingLoadCaseResultsForPST)

        @property
        def loaded_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _1983

            return self._parent._cast(_1983.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _1986

            return self._parent._cast(
                _1986.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _1989

            return self._parent._cast(
                _1989.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _1997

            return self._parent._cast(_1997.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2002

            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(_2005.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(_2012.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2036

            return self._parent._cast(_2036.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2119

            return self._parent._cast(_2119.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2120

            return self._parent._cast(_2120.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2121

            return self._parent._cast(_2121.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2122

            return self._parent._cast(_2122.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2124

            return self._parent._cast(_2124.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2128

            return self._parent._cast(_2128.LoadedTiltingPadThrustBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "BearingLoadCaseResultsLightweight":
            return self._parent

        def __getattr__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
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
        self: Self, instance_to_wrap: "BearingLoadCaseResultsLightweight.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight":
        return self._Cast_BearingLoadCaseResultsLightweight(self)
