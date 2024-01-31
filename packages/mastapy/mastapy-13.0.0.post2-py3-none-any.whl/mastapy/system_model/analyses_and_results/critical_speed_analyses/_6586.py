"""CVTCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CVTCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586


__docformat__ = "restructuredtext en"
__all__ = ("CVTCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTCriticalSpeedAnalysis")


class CVTCriticalSpeedAnalysis(_6552.BeltDriveCriticalSpeedAnalysis):
    """CVTCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCriticalSpeedAnalysis")

    class _Cast_CVTCriticalSpeedAnalysis:
        """Special nested class for casting CVTCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
            parent: "CVTCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_critical_speed_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6552.BeltDriveCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(_6542.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis",
        ) -> "CVTCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTCriticalSpeedAnalysis._Cast_CVTCriticalSpeedAnalysis":
        return self._Cast_CVTCriticalSpeedAnalysis(self)
