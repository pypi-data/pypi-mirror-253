"""CouplingCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7311,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingCompoundAdvancedSystemDeflection")


class CouplingCompoundAdvancedSystemDeflection(
    _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """CouplingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
            parent: "CouplingCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ) -> "CouplingCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7311.CouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingAdvancedSystemDeflection]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7311.CouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingCompoundAdvancedSystemDeflection(self)
