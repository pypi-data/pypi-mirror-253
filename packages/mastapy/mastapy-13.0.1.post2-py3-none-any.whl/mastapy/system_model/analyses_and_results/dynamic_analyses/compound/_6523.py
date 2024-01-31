"""SynchroniserPartCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SynchroniserPartCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundDynamicAnalysis")


class SynchroniserPartCompoundDynamicAnalysis(
    _6447.CouplingHalfCompoundDynamicAnalysis
):
    """SynchroniserPartCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundDynamicAnalysis"
    )

    class _Cast_SynchroniserPartCompoundDynamicAnalysis:
        """Special nested class for casting SynchroniserPartCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
            parent: "SynchroniserPartCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6447.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "SynchroniserPartCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6394.SynchroniserPartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis]

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
    ) -> "List[_6394.SynchroniserPartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis]

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
    ) -> "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis":
        return self._Cast_SynchroniserPartCompoundDynamicAnalysis(self)
