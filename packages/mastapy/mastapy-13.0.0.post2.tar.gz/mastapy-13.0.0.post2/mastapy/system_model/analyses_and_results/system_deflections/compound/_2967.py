"""SynchroniserHalfCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2968
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SynchroniserHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.system_deflections import _2821


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundSystemDeflection")


class SynchroniserHalfCompoundSystemDeflection(
    _2968.SynchroniserPartCompoundSystemDeflection
):
    """SynchroniserHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundSystemDeflection"
    )

    class _Cast_SynchroniserHalfCompoundSystemDeflection:
        """Special nested class for casting SynchroniserHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
            parent: "SynchroniserHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            return self._parent._cast(_2968.SynchroniserPartCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
        ) -> "SynchroniserHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_2821.SynchroniserHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection]

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
    ) -> "List[_2821.SynchroniserHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection]

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
    ) -> "SynchroniserHalfCompoundSystemDeflection._Cast_SynchroniserHalfCompoundSystemDeflection":
        return self._Cast_SynchroniserHalfCompoundSystemDeflection(self)
