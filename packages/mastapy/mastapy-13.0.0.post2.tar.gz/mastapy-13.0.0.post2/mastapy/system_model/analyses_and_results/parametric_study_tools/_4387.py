"""ParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6804, _6805
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4388


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyTool",)


Self = TypeVar("Self", bound="ParametricStudyTool")


class ParametricStudyTool(_7534.AnalysisCase):
    """ParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyTool")

    class _Cast_ParametricStudyTool:
        """Special nested class for casting ParametricStudyTool to subclasses."""

        def __init__(
            self: "ParametricStudyTool._Cast_ParametricStudyTool",
            parent: "ParametricStudyTool",
        ):
            self._parent = parent

        @property
        def analysis_case(self: "ParametricStudyTool._Cast_ParametricStudyTool"):
            return self._parent._cast(_7534.AnalysisCase)

        @property
        def context(self: "ParametricStudyTool._Cast_ParametricStudyTool"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def parametric_study_tool(
            self: "ParametricStudyTool._Cast_ParametricStudyTool",
        ) -> "ParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ParametricStudyTool._Cast_ParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self: Self) -> "_6804.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_analysis_options(self: Self) -> "_4388.ParametricStudyToolOptions":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6805.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ParametricStudyTool._Cast_ParametricStudyTool":
        return self._Cast_ParametricStudyTool(self)
