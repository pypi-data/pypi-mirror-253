"""KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7438,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7341,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection(
    _7438.ConicalGearCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7341.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7341.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection(
            self
        )
