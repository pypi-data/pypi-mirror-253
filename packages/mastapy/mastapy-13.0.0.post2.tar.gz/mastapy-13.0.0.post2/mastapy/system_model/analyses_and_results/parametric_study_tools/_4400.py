"""PowerLoadParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PowerLoadParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.system_deflections import _2792


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadParametricStudyTool",)


Self = TypeVar("Self", bound="PowerLoadParametricStudyTool")


class PowerLoadParametricStudyTool(_4435.VirtualComponentParametricStudyTool):
    """PowerLoadParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadParametricStudyTool")

    class _Cast_PowerLoadParametricStudyTool:
        """Special nested class for casting PowerLoadParametricStudyTool to subclasses."""

        def __init__(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
            parent: "PowerLoadParametricStudyTool",
        ):
            self._parent = parent

        @property
        def virtual_component_parametric_study_tool(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            return self._parent._cast(_4435.VirtualComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_parametric_study_tool(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
        ) -> "PowerLoadParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2792.PowerLoadSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "PowerLoadParametricStudyTool._Cast_PowerLoadParametricStudyTool":
        return self._Cast_PowerLoadParametricStudyTool(self)
