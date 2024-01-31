"""CVTParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CVTParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586


__docformat__ = "restructuredtext en"
__all__ = ("CVTParametricStudyTool",)


Self = TypeVar("Self", bound="CVTParametricStudyTool")


class CVTParametricStudyTool(_4305.BeltDriveParametricStudyTool):
    """CVTParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTParametricStudyTool")

    class _Cast_CVTParametricStudyTool:
        """Special nested class for casting CVTParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
            parent: "CVTParametricStudyTool",
        ):
            self._parent = parent

        @property
        def belt_drive_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            return self._parent._cast(_4305.BeltDriveParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_parametric_study_tool(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool",
        ) -> "CVTParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTParametricStudyTool._Cast_CVTParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTParametricStudyTool.TYPE"):
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
    def cast_to(self: Self) -> "CVTParametricStudyTool._Cast_CVTParametricStudyTool":
        return self._Cast_CVTParametricStudyTool(self)
