"""PartToPartShearCouplingHalfParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartToPartShearCouplingHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6930
    from mastapy.system_model.analyses_and_results.system_deflections import _2787


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfParametricStudyTool",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfParametricStudyTool")


class PartToPartShearCouplingHalfParametricStudyTool(
    _4333.CouplingHalfParametricStudyTool
):
    """PartToPartShearCouplingHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfParametricStudyTool"
    )

    class _Cast_PartToPartShearCouplingHalfParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
            parent: "PartToPartShearCouplingHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            return self._parent._cast(_4333.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
        ) -> "PartToPartShearCouplingHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool",
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
        instance_to_wrap: "PartToPartShearCouplingHalfParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6930.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "List[_2787.PartToPartShearCouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection]

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
    ) -> "PartToPartShearCouplingHalfParametricStudyTool._Cast_PartToPartShearCouplingHalfParametricStudyTool":
        return self._Cast_PartToPartShearCouplingHalfParametricStudyTool(self)
