"""VirtualComponentCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7483,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "VirtualComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7399,
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundAdvancedSystemDeflection")


class VirtualComponentCompoundAdvancedSystemDeflection(
    _7483.MountableComponentCompoundAdvancedSystemDeflection
):
    """VirtualComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
            parent: "VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "VirtualComponentCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7399.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    ) -> "List[_7399.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    ) -> "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection":
        return self._Cast_VirtualComponentCompoundAdvancedSystemDeflection(self)
