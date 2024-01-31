"""BeltDriveCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BeltDriveCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BeltDriveCriticalSpeedAnalysis")


class BeltDriveCriticalSpeedAnalysis(_6644.SpecialisedAssemblyCriticalSpeedAnalysis):
    """BeltDriveCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveCriticalSpeedAnalysis")

    class _Cast_BeltDriveCriticalSpeedAnalysis:
        """Special nested class for casting BeltDriveCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
            parent: "BeltDriveCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.CVTCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
        ) -> "BeltDriveCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveCriticalSpeedAnalysis._Cast_BeltDriveCriticalSpeedAnalysis":
        return self._Cast_BeltDriveCriticalSpeedAnalysis(self)
