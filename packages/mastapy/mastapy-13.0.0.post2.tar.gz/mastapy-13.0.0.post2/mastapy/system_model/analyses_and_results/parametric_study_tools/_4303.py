"""BearingParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BearingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2439
    from mastapy.system_model.analyses_and_results.static_loads import _6819
    from mastapy.bearings.bearing_results import _1948
    from mastapy.system_model.analyses_and_results.system_deflections import _2698


__docformat__ = "restructuredtext en"
__all__ = ("BearingParametricStudyTool",)


Self = TypeVar("Self", bound="BearingParametricStudyTool")


class BearingParametricStudyTool(_4331.ConnectorParametricStudyTool):
    """BearingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEARING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingParametricStudyTool")

    class _Cast_BearingParametricStudyTool:
        """Special nested class for casting BearingParametricStudyTool to subclasses."""

        def __init__(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
            parent: "BearingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connector_parametric_study_tool(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            return self._parent._cast(_4331.ConnectorParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_parametric_study_tool(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
        ) -> "BearingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BearingParametricStudyTool._Cast_BearingParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2439.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6819.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_duty_cycle_results(self: Self) -> "List[_1948.LoadedBearingDutyCycle]":
        """List[mastapy.bearings.bearing_results.LoadedBearingDutyCycle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingDutyCycleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2698.BearingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[BearingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingParametricStudyTool._Cast_BearingParametricStudyTool":
        return self._Cast_BearingParametricStudyTool(self)
