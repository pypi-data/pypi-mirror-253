"""CVTCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6684,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CVTCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundCriticalSpeedAnalysis")


class CVTCompoundCriticalSpeedAnalysis(_6684.BeltDriveCompoundCriticalSpeedAnalysis):
    """CVTCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundCriticalSpeedAnalysis")

    class _Cast_CVTCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CVTCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
            parent: "CVTCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6684.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6674,
            )

            return self._parent._cast(
                _6674.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "CVTCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6586.CVTCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTCriticalSpeedAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_6586.CVTCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTCriticalSpeedAnalysis]

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
    ) -> "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis":
        return self._Cast_CVTCompoundCriticalSpeedAnalysis(self)
