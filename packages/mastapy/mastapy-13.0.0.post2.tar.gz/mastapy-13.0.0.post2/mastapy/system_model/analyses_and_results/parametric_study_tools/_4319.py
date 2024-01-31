"""CoaxialConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CoaxialConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.static_loads import _6836
    from mastapy.system_model.analyses_and_results.system_deflections import _2714


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="CoaxialConnectionParametricStudyTool")


class CoaxialConnectionParametricStudyTool(
    _4410.ShaftToMountableComponentConnectionParametricStudyTool
):
    """CoaxialConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionParametricStudyTool")

    class _Cast_CoaxialConnectionParametricStudyTool:
        """Special nested class for casting CoaxialConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
            parent: "CoaxialConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            return self._parent._cast(
                _4410.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(
                _4298.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(
                _4339.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def coaxial_connection_parametric_study_tool(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
        ) -> "CoaxialConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "CoaxialConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6836.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2714.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionParametricStudyTool._Cast_CoaxialConnectionParametricStudyTool":
        return self._Cast_CoaxialConnectionParametricStudyTool(self)
