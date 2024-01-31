"""StraightBevelDiffGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7289
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelDiffGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.gears.rating.straight_bevel_diff import _399
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.system_deflections import _2815


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearAdvancedSystemDeflection")


class StraightBevelDiffGearAdvancedSystemDeflection(
    _7289.BevelGearAdvancedSystemDeflection
):
    """StraightBevelDiffGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
            parent: "StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7289.BevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(
                _7277.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(
                _7388.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
        ) -> "StraightBevelDiffGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "StraightBevelDiffGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_399.StraightBevelDiffGearRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2815.StraightBevelDiffGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearAdvancedSystemDeflection._Cast_StraightBevelDiffGearAdvancedSystemDeflection":
        return self._Cast_StraightBevelDiffGearAdvancedSystemDeflection(self)
