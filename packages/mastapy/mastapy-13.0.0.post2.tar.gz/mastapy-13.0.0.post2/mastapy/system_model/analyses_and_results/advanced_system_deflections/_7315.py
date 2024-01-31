"""CVTPulleyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CVTPulleyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleyAdvancedSystemDeflection")


class CVTPulleyAdvancedSystemDeflection(_7363.PulleyAdvancedSystemDeflection):
    """CVTPulleyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyAdvancedSystemDeflection")

    class _Cast_CVTPulleyAdvancedSystemDeflection:
        """Special nested class for casting CVTPulleyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
            parent: "CVTPulleyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7363.PulleyAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "CVTPulleyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTPulleyAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection":
        return self._Cast_CVTPulleyAdvancedSystemDeflection(self)
