"""CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2737


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"
)


class CycloidalDiscPlanetaryBearingConnectionParametricStudyTool(
    _4298.AbstractShaftToMountableComponentConnectionParametricStudyTool
):
    """CycloidalDiscPlanetaryBearingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
            parent: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            return self._parent._cast(
                _4298.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
        ) -> "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6860.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "List[_2737.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionParametricStudyTool(
            self
        )
