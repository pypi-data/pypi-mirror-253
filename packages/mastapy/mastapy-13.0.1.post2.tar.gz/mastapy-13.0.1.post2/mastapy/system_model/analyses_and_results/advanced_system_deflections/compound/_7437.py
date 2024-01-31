"""ConceptGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7466,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7304,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7435,
        _7436,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundAdvancedSystemDeflection")


class ConceptGearSetCompoundAdvancedSystemDeflection(
    _7466.GearSetCompoundAdvancedSystemDeflection
):
    """ConceptGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConceptGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
            parent: "ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
        ) -> "ConceptGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_7304.ConceptGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearSetAdvancedSystemDeflection]

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
    def concept_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7435.ConceptGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7436.ConceptGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7304.ConceptGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearSetAdvancedSystemDeflection]

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
    ) -> "ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptGearSetCompoundAdvancedSystemDeflection(self)
