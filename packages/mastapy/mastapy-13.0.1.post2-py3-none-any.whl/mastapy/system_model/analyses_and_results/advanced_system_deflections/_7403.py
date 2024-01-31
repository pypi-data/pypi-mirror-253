"""ZerolBevelGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7289
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ZerolBevelGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.gears.rating.zerol_bevel import _370
    from mastapy.system_model.analyses_and_results.static_loads import _6986
    from mastapy.system_model.analyses_and_results.system_deflections import _2841


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearAdvancedSystemDeflection")


class ZerolBevelGearAdvancedSystemDeflection(_7289.BevelGearAdvancedSystemDeflection):
    """ZerolBevelGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearAdvancedSystemDeflection"
    )

    class _Cast_ZerolBevelGearAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
            parent: "ZerolBevelGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7289.BevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(
                _7277.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
        ) -> "ZerolBevelGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_370.ZerolBevelGearRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6986.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "List[_2841.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    ) -> "ZerolBevelGearAdvancedSystemDeflection._Cast_ZerolBevelGearAdvancedSystemDeflection":
        return self._Cast_ZerolBevelGearAdvancedSystemDeflection(self)
