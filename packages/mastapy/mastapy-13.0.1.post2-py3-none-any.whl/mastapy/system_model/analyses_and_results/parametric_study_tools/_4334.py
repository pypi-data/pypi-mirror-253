"""CouplingHalfParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4381
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingHalfParametricStudyTool")


class CouplingHalfParametricStudyTool(_4381.MountableComponentParametricStudyTool):
    """CouplingHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfParametricStudyTool")

    class _Cast_CouplingHalfParametricStudyTool:
        """Special nested class for casting CouplingHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            parent: "CouplingHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptCouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CVTPulleyParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.PulleyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.RollingRingParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpringDamperHalfParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.TorqueConverterTurbineParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "CouplingHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool":
        return self._Cast_CouplingHalfParametricStudyTool(self)
