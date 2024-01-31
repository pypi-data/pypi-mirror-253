"""StraightBevelSunGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7511,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7388,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundAdvancedSystemDeflection")


class StraightBevelSunGearCompoundAdvancedSystemDeflection(
    _7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection
):
    """StraightBevelSunGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelSunGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
            parent: "StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelSunGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelSunGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7388.StraightBevelSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelSunGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7388.StraightBevelSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelSunGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection(self)
