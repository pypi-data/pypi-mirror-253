"""SynchroniserSleeveCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6790,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6662


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundCriticalSpeedAnalysis")


class SynchroniserSleeveCompoundCriticalSpeedAnalysis(
    _6790.SynchroniserPartCompoundCriticalSpeedAnalysis
):
    """SynchroniserSleeveCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
            parent: "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6790.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
        ) -> "SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SynchroniserSleeveCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_6662.SynchroniserSleeveCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserSleeveCriticalSpeedAnalysis]

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
    ) -> "List[_6662.SynchroniserSleeveCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserSleeveCriticalSpeedAnalysis]

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
    ) -> "SynchroniserSleeveCompoundCriticalSpeedAnalysis._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis":
        return self._Cast_SynchroniserSleeveCompoundCriticalSpeedAnalysis(self)
