"""CycloidalDiscAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CycloidalDiscAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6859
    from mastapy.system_model.analyses_and_results.system_deflections import _2738


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalDiscAdvancedSystemDeflection")


class CycloidalDiscAdvancedSystemDeflection(
    _7270.AbstractShaftAdvancedSystemDeflection
):
    """CycloidalDiscAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscAdvancedSystemDeflection"
    )

    class _Cast_CycloidalDiscAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
            parent: "CycloidalDiscAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7270.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(
                _7271.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def component_advanced_system_deflection(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
        ) -> "CycloidalDiscAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CycloidalDiscAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2738.CycloidalDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscAdvancedSystemDeflection._Cast_CycloidalDiscAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscAdvancedSystemDeflection(self)
