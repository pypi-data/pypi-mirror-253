"""CouplingCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4540,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CouplingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4334


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingCompoundParametricStudyTool")


class CouplingCompoundParametricStudyTool(
    _4540.SpecialisedAssemblyCompoundParametricStudyTool
):
    """CouplingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundParametricStudyTool")

    class _Cast_CouplingCompoundParametricStudyTool:
        """Special nested class for casting CouplingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
            parent: "CouplingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4540.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4442,
            )

            return self._parent._cast(_4442.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ConceptCouplingCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(_4544.SpringDamperCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(_4559.TorqueConverterCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
        ) -> "CouplingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CouplingCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4334.CouplingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingParametricStudyTool]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4334.CouplingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> (
        "CouplingCompoundParametricStudyTool._Cast_CouplingCompoundParametricStudyTool"
    ):
        return self._Cast_CouplingCompoundParametricStudyTool(self)
