"""MeasurementComponentCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4565,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "MeasurementComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4379


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundParametricStudyTool")


class MeasurementComponentCompoundParametricStudyTool(
    _4565.VirtualComponentCompoundParametricStudyTool
):
    """MeasurementComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundParametricStudyTool"
    )

    class _Cast_MeasurementComponentCompoundParametricStudyTool:
        """Special nested class for casting MeasurementComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
            parent: "MeasurementComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4565.VirtualComponentCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
        ) -> "MeasurementComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool",
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
        instance_to_wrap: "MeasurementComponentCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6923.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4379.MeasurementComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MeasurementComponentParametricStudyTool]

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
    ) -> "List[_4379.MeasurementComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MeasurementComponentParametricStudyTool]

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
    ) -> "MeasurementComponentCompoundParametricStudyTool._Cast_MeasurementComponentCompoundParametricStudyTool":
        return self._Cast_MeasurementComponentCompoundParametricStudyTool(self)
