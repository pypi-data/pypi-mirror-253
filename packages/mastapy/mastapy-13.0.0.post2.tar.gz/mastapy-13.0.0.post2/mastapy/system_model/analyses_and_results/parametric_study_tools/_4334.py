"""CouplingParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583


__docformat__ = "restructuredtext en"
__all__ = ("CouplingParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingParametricStudyTool")


class CouplingParametricStudyTool(_4411.SpecialisedAssemblyParametricStudyTool):
    """CouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingParametricStudyTool")

    class _Cast_CouplingParametricStudyTool:
        """Special nested class for casting CouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            parent: "CouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            return self._parent._cast(_4411.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptCouplingParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartToPartShearCouplingParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpringDamperParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.TorqueConverterParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "CouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool":
        return self._Cast_CouplingParametricStudyTool(self)
