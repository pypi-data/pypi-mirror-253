"""CycloidalDiscParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalDiscParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6859
    from mastapy.system_model.analyses_and_results.system_deflections import _2738


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalDiscParametricStudyTool")


class CycloidalDiscParametricStudyTool(_4297.AbstractShaftParametricStudyTool):
    """CycloidalDiscParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscParametricStudyTool")

    class _Cast_CycloidalDiscParametricStudyTool:
        """Special nested class for casting CycloidalDiscParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
            parent: "CycloidalDiscParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            return self._parent._cast(_4297.AbstractShaftParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
        ) -> "CycloidalDiscParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "List[_2738.CycloidalDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection]

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
    ) -> "CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool":
        return self._Cast_CycloidalDiscParametricStudyTool(self)
