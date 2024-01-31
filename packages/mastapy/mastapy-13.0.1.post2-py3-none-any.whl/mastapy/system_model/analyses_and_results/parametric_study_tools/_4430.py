"""SynchroniserSleeveParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4429
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SynchroniserSleeveParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.system_deflections import _2823


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserSleeveParametricStudyTool")


class SynchroniserSleeveParametricStudyTool(_4429.SynchroniserPartParametricStudyTool):
    """SynchroniserSleeveParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveParametricStudyTool"
    )

    class _Cast_SynchroniserSleeveParametricStudyTool:
        """Special nested class for casting SynchroniserSleeveParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
            parent: "SynchroniserSleeveParametricStudyTool",
        ):
            self._parent = parent

        @property
        def synchroniser_part_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            return self._parent._cast(_4429.SynchroniserPartParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
        ) -> "SynchroniserSleeveParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "List[_2823.SynchroniserSleeveSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection]

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
    ) -> "SynchroniserSleeveParametricStudyTool._Cast_SynchroniserSleeveParametricStudyTool":
        return self._Cast_SynchroniserSleeveParametricStudyTool(self)
