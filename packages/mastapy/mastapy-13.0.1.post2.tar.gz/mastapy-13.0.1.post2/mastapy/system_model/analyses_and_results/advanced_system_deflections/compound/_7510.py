"""SpringDamperHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7445,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7380,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundAdvancedSystemDeflection")


class SpringDamperHalfCompoundAdvancedSystemDeflection(
    _7445.CouplingHalfCompoundAdvancedSystemDeflection
):
    """SpringDamperHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpringDamperHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpringDamperHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
            parent: "SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7445.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "SpringDamperHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpringDamperHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7380.SpringDamperHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperHalfAdvancedSystemDeflection]

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
    ) -> "List[_7380.SpringDamperHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperHalfAdvancedSystemDeflection]

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
    ) -> "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection":
        return self._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection(self)
