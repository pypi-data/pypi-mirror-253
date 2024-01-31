"""SpringDamperCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7443,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpringDamperCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7378,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperCompoundAdvancedSystemDeflection")


class SpringDamperCompoundAdvancedSystemDeflection(
    _7443.CouplingCompoundAdvancedSystemDeflection
):
    """SpringDamperCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpringDamperCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpringDamperCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
            parent: "SpringDamperCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_advanced_system_deflection(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7443.CouplingCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
        ) -> "SpringDamperCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpringDamperCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

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
    ) -> "List[_7378.SpringDamperAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperAdvancedSystemDeflection]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7378.SpringDamperAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperAdvancedSystemDeflection]

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
    ) -> "SpringDamperCompoundAdvancedSystemDeflection._Cast_SpringDamperCompoundAdvancedSystemDeflection":
        return self._Cast_SpringDamperCompoundAdvancedSystemDeflection(self)
