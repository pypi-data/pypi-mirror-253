"""PlanetaryConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PlanetaryConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.system_deflections import _2789


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryConnectionParametricStudyTool")


class PlanetaryConnectionParametricStudyTool(
    _4410.ShaftToMountableComponentConnectionParametricStudyTool
):
    """PlanetaryConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionParametricStudyTool"
    )

    class _Cast_PlanetaryConnectionParametricStudyTool:
        """Special nested class for casting PlanetaryConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
            parent: "PlanetaryConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            return self._parent._cast(
                _4410.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(
                _4298.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_parametric_study_tool(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
        ) -> "PlanetaryConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6932.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "List[_2789.PlanetaryConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection]

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
    ) -> "PlanetaryConnectionParametricStudyTool._Cast_PlanetaryConnectionParametricStudyTool":
        return self._Cast_PlanetaryConnectionParametricStudyTool(self)
