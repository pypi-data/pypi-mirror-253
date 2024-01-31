"""CVTCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4453,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CVTCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6856
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CVTCompoundParametricStudyTool")


class CVTCompoundParametricStudyTool(_4453.BeltDriveCompoundParametricStudyTool):
    """CVTCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundParametricStudyTool")

    class _Cast_CVTCompoundParametricStudyTool:
        """Special nested class for casting CVTCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
            parent: "CVTCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4453.BeltDriveCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_parametric_study_tool(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
        ) -> "CVTCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6856.CVTLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4337.CVTParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4337.CVTParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTCompoundParametricStudyTool._Cast_CVTCompoundParametricStudyTool":
        return self._Cast_CVTCompoundParametricStudyTool(self)
