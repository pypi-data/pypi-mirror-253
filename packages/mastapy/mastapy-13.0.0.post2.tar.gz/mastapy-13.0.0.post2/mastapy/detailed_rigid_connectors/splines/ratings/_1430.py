"""SplineHalfRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "SplineHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("SplineHalfRating",)


Self = TypeVar("Self", bound="SplineHalfRating")


class SplineHalfRating(_0.APIBase):
    """SplineHalfRating

    This is a mastapy class.
    """

    TYPE = _SPLINE_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineHalfRating")

    class _Cast_SplineHalfRating:
        """Special nested class for casting SplineHalfRating to subclasses."""

        def __init__(
            self: "SplineHalfRating._Cast_SplineHalfRating", parent: "SplineHalfRating"
        ):
            self._parent = parent

        @property
        def agma6123_spline_half_rating(
            self: "SplineHalfRating._Cast_SplineHalfRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1422

            return self._parent._cast(_1422.AGMA6123SplineHalfRating)

        @property
        def din5466_spline_half_rating(self: "SplineHalfRating._Cast_SplineHalfRating"):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1424

            return self._parent._cast(_1424.DIN5466SplineHalfRating)

        @property
        def gbt17855_spline_half_rating(
            self: "SplineHalfRating._Cast_SplineHalfRating",
        ):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1426

            return self._parent._cast(_1426.GBT17855SplineHalfRating)

        @property
        def sae_spline_half_rating(self: "SplineHalfRating._Cast_SplineHalfRating"):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1428

            return self._parent._cast(_1428.SAESplineHalfRating)

        @property
        def spline_half_rating(
            self: "SplineHalfRating._Cast_SplineHalfRating",
        ) -> "SplineHalfRating":
            return self._parent

        def __getattr__(self: "SplineHalfRating._Cast_SplineHalfRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineHalfRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_bursting_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "SplineHalfRating._Cast_SplineHalfRating":
        return self._Cast_SplineHalfRating(self)
