"""CVTCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CVTCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3806


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundStabilityAnalysis")


class CVTCompoundStabilityAnalysis(_3907.BeltDriveCompoundStabilityAnalysis):
    """CVTCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundStabilityAnalysis")

    class _Cast_CVTCompoundStabilityAnalysis:
        """Special nested class for casting CVTCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
            parent: "CVTCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_stability_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3907.BeltDriveCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3897,
            )

            return self._parent._cast(_3897.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
        ) -> "CVTCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_3806.CVTStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTStabilityAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_3806.CVTStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTStabilityAnalysis]

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
    ) -> "CVTCompoundStabilityAnalysis._Cast_CVTCompoundStabilityAnalysis":
        return self._Cast_CVTCompoundStabilityAnalysis(self)
