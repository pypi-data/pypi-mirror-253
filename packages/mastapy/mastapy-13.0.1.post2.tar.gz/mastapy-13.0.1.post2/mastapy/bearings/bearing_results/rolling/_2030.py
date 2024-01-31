"""LoadedRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2029, _1970


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedRollerBearingRow")


class LoadedRollerBearingRow(_2034.LoadedRollingBearingRow):
    """LoadedRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerBearingRow")

    class _Cast_LoadedRollerBearingRow:
        """Special nested class for casting LoadedRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
            parent: "LoadedRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            return self._parent._cast(_2034.LoadedRollingBearingRow)

        @property
        def loaded_asymmetric_spherical_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1990

            return self._parent._cast(_1990.LoadedAsymmetricSphericalRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1995

            return self._parent._cast(
                _1995.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1998

            return self._parent._cast(_1998.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(_2006.LoadedCrossedRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedNeedleRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedSphericalRollerRadialBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedSphericalRollerThrustBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedTaperRollerBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedToroidalRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow",
        ) -> "LoadedRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth_of_maximum_shear_stress_chart_inner(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumShearStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def depth_of_maximum_shear_stress_chart_outer(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumShearStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def hertzian_contact_width_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_profile_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceProfileWarning

        if temp is None:
            return ""

        return temp

    @property
    def maximum_normal_edge_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_race_profile_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceProfileWarning

        if temp is None:
            return ""

        return temp

    @property
    def roller_profile_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollerProfileWarning

        if temp is None:
            return ""

        return temp

    @property
    def shear_stress_chart_inner(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def shear_stress_chart_outer(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_bearing(self: Self) -> "_2029.LoadedRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lamina_dynamic_equivalent_loads(
        self: Self,
    ) -> "List[_1970.ForceAtLaminaGroupReportable]":
        """List[mastapy.bearings.bearing_results.rolling.ForceAtLaminaGroupReportable]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LaminaDynamicEquivalentLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "LoadedRollerBearingRow._Cast_LoadedRollerBearingRow":
        return self._Cast_LoadedRollerBearingRow(self)
