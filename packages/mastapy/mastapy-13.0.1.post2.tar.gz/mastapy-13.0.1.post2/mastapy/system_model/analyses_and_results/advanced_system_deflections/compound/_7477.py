"""KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7474,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7346,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7475,
        _7476,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection(
    _7474.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2539.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> (
        "List[_7475.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundAdvancedSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7476.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundAdvancedSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection(
            self
        )
