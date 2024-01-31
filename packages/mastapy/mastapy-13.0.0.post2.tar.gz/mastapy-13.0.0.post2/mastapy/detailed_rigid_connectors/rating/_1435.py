"""ShaftHubConnectionRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Rating", "ShaftHubConnectionRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1386


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionRating",)


Self = TypeVar("Self", bound="ShaftHubConnectionRating")


class ShaftHubConnectionRating(_0.APIBase):
    """ShaftHubConnectionRating

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionRating")

    class _Cast_ShaftHubConnectionRating:
        """Special nested class for casting ShaftHubConnectionRating to subclasses."""

        def __init__(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
            parent: "ShaftHubConnectionRating",
        ):
            self._parent = parent

        @property
        def agma6123_spline_joint_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1423

            return self._parent._cast(_1423.AGMA6123SplineJointRating)

        @property
        def din5466_spline_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1425

            return self._parent._cast(_1425.DIN5466SplineRating)

        @property
        def gbt17855_spline_joint_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1427

            return self._parent._cast(_1427.GBT17855SplineJointRating)

        @property
        def sae_spline_joint_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1429

            return self._parent._cast(_1429.SAESplineJointRating)

        @property
        def spline_joint_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1431

            return self._parent._cast(_1431.SplineJointRating)

        @property
        def keyway_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1441

            return self._parent._cast(_1441.KeywayRating)

        @property
        def interference_fit_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ):
            from mastapy.detailed_rigid_connectors.interference_fits.rating import _1448

            return self._parent._cast(_1448.InterferenceFitRating)

        @property
        def shaft_hub_connection_rating(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating",
        ) -> "ShaftHubConnectionRating":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHubConnectionRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_rating_information(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AdditionalRatingInformation

        if temp is None:
            return ""

        return temp

    @additional_rating_information.setter
    @enforce_parameter_types
    def additional_rating_information(self: Self, value: "str"):
        self.wrapped.AdditionalRatingInformation = (
            str(value) if value is not None else ""
        )

    @property
    def joint_design(self: Self) -> "_1386.DetailedRigidConnectorDesign":
        """mastapy.detailed_rigid_connectors.DetailedRigidConnectorDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "ShaftHubConnectionRating._Cast_ShaftHubConnectionRating":
        return self._Cast_ShaftHubConnectionRating(self)
