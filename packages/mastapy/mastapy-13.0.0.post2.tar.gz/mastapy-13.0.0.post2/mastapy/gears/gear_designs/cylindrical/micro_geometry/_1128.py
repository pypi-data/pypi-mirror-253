"""ReliefWithDeviation"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "ReliefWithDeviation"
)


__docformat__ = "restructuredtext en"
__all__ = ("ReliefWithDeviation",)


Self = TypeVar("Self", bound="ReliefWithDeviation")


class ReliefWithDeviation(_0.APIBase):
    """ReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ReliefWithDeviation")

    class _Cast_ReliefWithDeviation:
        """Special nested class for casting ReliefWithDeviation to subclasses."""

        def __init__(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
            parent: "ReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def lead_form_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.LeadFormReliefWithDeviation)

        @property
        def lead_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1115

            return self._parent._cast(_1115.LeadReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1116

            return self._parent._cast(_1116.LeadSlopeReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1125

            return self._parent._cast(_1125.ProfileFormReliefWithDeviation)

        @property
        def profile_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1126

            return self._parent._cast(_1126.ProfileReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1127

            return self._parent._cast(_1127.ProfileSlopeReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1130

            return self._parent._cast(_1130.TotalLeadReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1131

            return self._parent._cast(_1131.TotalProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "ReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lower_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Relief

        if temp is None:
            return 0.0

        return temp

    @property
    def section(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Section

        if temp is None:
            return ""

        return temp

    @property
    def upper_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ReliefWithDeviation._Cast_ReliefWithDeviation":
        return self._Cast_ReliefWithDeviation(self)
