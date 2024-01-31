"""AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7440,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7279,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"
)


class AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
    _7440.ConicalGearSetCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7440.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(
                _7424.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
            self
        )
