"""ConnectorParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4380
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConnectorParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorParametricStudyTool",)


Self = TypeVar("Self", bound="ConnectorParametricStudyTool")


class ConnectorParametricStudyTool(_4380.MountableComponentParametricStudyTool):
    """ConnectorParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorParametricStudyTool")

    class _Cast_ConnectorParametricStudyTool:
        """Special nested class for casting ConnectorParametricStudyTool to subclasses."""

        def __init__(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
            parent: "ConnectorParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.BearingParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.OilSealParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.ShaftHubConnectionParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
        ) -> "ConnectorParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorParametricStudyTool._Cast_ConnectorParametricStudyTool":
        return self._Cast_ConnectorParametricStudyTool(self)
