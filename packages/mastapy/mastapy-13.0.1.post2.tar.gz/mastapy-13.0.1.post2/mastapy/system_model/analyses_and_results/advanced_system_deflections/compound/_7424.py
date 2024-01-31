"""BevelGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7412,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7291,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSetCompoundAdvancedSystemDeflection")


class BevelGearSetCompoundAdvancedSystemDeflection(
    _7412.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
):
    """BevelGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
            parent: "BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7412.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "BevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7291.BevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7291.BevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearSetAdvancedSystemDeflection]

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
    ) -> "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_BevelGearSetCompoundAdvancedSystemDeflection(self)
