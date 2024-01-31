"""CylindricalPlanetaryGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1028
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalPlanetaryGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1867
    from mastapy.math_utility import _1512


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetaryGearSetDesign",)


Self = TypeVar("Self", bound="CylindricalPlanetaryGearSetDesign")


class CylindricalPlanetaryGearSetDesign(_1028.CylindricalGearSetDesign):
    """CylindricalPlanetaryGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetaryGearSetDesign")

    class _Cast_CylindricalPlanetaryGearSetDesign:
        """Special nested class for casting CylindricalPlanetaryGearSetDesign to subclasses."""

        def __init__(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
            parent: "CylindricalPlanetaryGearSetDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_design(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
        ):
            return self._parent._cast(_1028.CylindricalGearSetDesign)

        @property
        def gear_set_design(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearSetDesign)

        @property
        def gear_design_component(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
        ) -> "CylindricalPlanetaryGearSetDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign",
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
        self: Self, instance_to_wrap: "CylindricalPlanetaryGearSetDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equally_spaced_planets_are_assemblable(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquallySpacedPlanetsAreAssemblable

        if temp is None:
            return False

        return temp

    @property
    def least_mesh_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeastMeshAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_module_scale_planet_diameters(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModuleScalePlanetDiameters

        if temp is None:
            return 0.0

        return temp

    @normal_module_scale_planet_diameters.setter
    @enforce_parameter_types
    def normal_module_scale_planet_diameters(self: Self, value: "float"):
        self.wrapped.NormalModuleScalePlanetDiameters = (
            float(value) if value is not None else 0.0
        )

    @property
    def planet_gear_phasing_chart(self: Self) -> "_1867.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetGearPhasingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.ReferenceFixedGearForPlanetarySidebandFourierSeriesIsAnnulus

        if temp is None:
            return False

        return temp

    @reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus.setter
    @enforce_parameter_types
    def reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus(
        self: Self, value: "bool"
    ):
        self.wrapped.ReferenceFixedGearForPlanetarySidebandFourierSeriesIsAnnulus = (
            bool(value) if value is not None else False
        )

    @property
    def use_planet_passing_window_function_in_planetary_sideband_fourier_series(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UsePlanetPassingWindowFunctionInPlanetarySidebandFourierSeries
        )

        if temp is None:
            return False

        return temp

    @use_planet_passing_window_function_in_planetary_sideband_fourier_series.setter
    @enforce_parameter_types
    def use_planet_passing_window_function_in_planetary_sideband_fourier_series(
        self: Self, value: "bool"
    ):
        self.wrapped.UsePlanetPassingWindowFunctionInPlanetarySidebandFourierSeries = (
            bool(value) if value is not None else False
        )

    @property
    def planetary_sideband_fourier_series_for_rotating_planet_carrier(
        self: Self,
    ) -> "_1512.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetarySidebandFourierSeriesForRotatingPlanetCarrier

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_new_micro_geometry_using_planetary_duplicates(self: Self):
        """Method does not return."""
        self.wrapped.AddNewMicroGeometryUsingPlanetaryDuplicates()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign":
        return self._Cast_CylindricalPlanetaryGearSetDesign(self)
