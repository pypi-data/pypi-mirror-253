"""PlanetaryGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7454,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7359,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundAdvancedSystemDeflection")


class PlanetaryGearSetCompoundAdvancedSystemDeflection(
    _7454.CylindricalGearSetCompoundAdvancedSystemDeflection
):
    """PlanetaryGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting PlanetaryGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
            parent: "PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7454.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7405,
            )

            return self._parent._cast(
                _7405.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(_7484.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
        ) -> "PlanetaryGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "PlanetaryGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7359.PlanetaryGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PlanetaryGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7359.PlanetaryGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PlanetaryGearSetAdvancedSystemDeflection]

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
    ) -> "PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection(self)
