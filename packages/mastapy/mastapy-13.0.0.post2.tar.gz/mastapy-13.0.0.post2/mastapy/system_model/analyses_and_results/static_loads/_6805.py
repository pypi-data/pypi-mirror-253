"""TimeSeriesLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TimeSeriesLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results import _2639, _2620
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5460
    from mastapy.system_model.analyses_and_results.load_case_groups import _5670
    from mastapy.system_model.analyses_and_results.static_loads import _6817


__docformat__ = "restructuredtext en"
__all__ = ("TimeSeriesLoadCase",)


Self = TypeVar("Self", bound="TimeSeriesLoadCase")


class TimeSeriesLoadCase(_6803.LoadCase):
    """TimeSeriesLoadCase

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeSeriesLoadCase")

    class _Cast_TimeSeriesLoadCase:
        """Special nested class for casting TimeSeriesLoadCase to subclasses."""

        def __init__(
            self: "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase",
            parent: "TimeSeriesLoadCase",
        ):
            self._parent = parent

        @property
        def load_case(self: "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase"):
            return self._parent._cast(_6803.LoadCase)

        @property
        def context(self: "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def time_series_load_case(
            self: "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase",
        ) -> "TimeSeriesLoadCase":
            return self._parent

        def __getattr__(self: "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeSeriesLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def multibody_dynamics_analysis(self: Self) -> "_2639.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def duration_for_rating(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DurationForRating

        if temp is None:
            return 0.0

        return temp

    @duration_for_rating.setter
    @enforce_parameter_types
    def duration_for_rating(self: Self, value: "float"):
        self.wrapped.DurationForRating = float(value) if value is not None else 0.0

    @property
    def driva_analysis_options(self: Self) -> "_5460.MBDAnalysisOptions":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MBDAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DRIVAAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case_group(self: Self) -> "_5670.TimeSeriesLoadCaseGroup":
        """mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCaseGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_of(
        self: Self, analysis_type: "_6817.AnalysisType"
    ) -> "_2620.SingleAnalysis":
        """mastapy.system_model.analyses_and_results.SingleAnalysis

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate(
        self: Self,
        new_load_case_group: "_5670.TimeSeriesLoadCaseGroup",
        name: "str" = "None",
    ) -> "TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Args:
            new_load_case_group (mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup)
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.Duplicate(
            new_load_case_group.wrapped if new_load_case_group else None,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "TimeSeriesLoadCase._Cast_TimeSeriesLoadCase":
        return self._Cast_TimeSeriesLoadCase(self)
