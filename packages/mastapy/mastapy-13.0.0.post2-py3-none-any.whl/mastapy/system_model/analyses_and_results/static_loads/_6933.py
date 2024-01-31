"""PlanetaryGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.utility import _1589
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetLoadCase",)


Self = TypeVar("Self", bound="PlanetaryGearSetLoadCase")


class PlanetaryGearSetLoadCase(_6865.CylindricalGearSetLoadCase):
    """PlanetaryGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetLoadCase")

    class _Cast_PlanetaryGearSetLoadCase:
        """Special nested class for casting PlanetaryGearSetLoadCase to subclasses."""

        def __init__(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
            parent: "PlanetaryGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            return self._parent._cast(_6865.CylindricalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_load_case(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase",
        ) -> "PlanetaryGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_gear_blank_elastic_distortion(
        self: Self,
    ) -> "_1589.LoadCaseOverrideOption":
        """mastapy.utility.LoadCaseOverrideOption"""
        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility._1589", "LoadCaseOverrideOption"
        )(value)

    @include_gear_blank_elastic_distortion.setter
    @enforce_parameter_types
    def include_gear_blank_elastic_distortion(
        self: Self, value: "_1589.LoadCaseOverrideOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )
        self.wrapped.IncludeGearBlankElasticDistortion = value

    @property
    def specify_separate_micro_geometry_for_each_planet_gear(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifySeparateMicroGeometryForEachPlanetGear

        if temp is None:
            return False

        return temp

    @specify_separate_micro_geometry_for_each_planet_gear.setter
    @enforce_parameter_types
    def specify_separate_micro_geometry_for_each_planet_gear(self: Self, value: "bool"):
        self.wrapped.SpecifySeparateMicroGeometryForEachPlanetGear = (
            bool(value) if value is not None else False
        )

    @property
    def assembly_design(self: Self) -> "_2542.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetLoadCase._Cast_PlanetaryGearSetLoadCase":
        return self._Cast_PlanetaryGearSetLoadCase(self)
