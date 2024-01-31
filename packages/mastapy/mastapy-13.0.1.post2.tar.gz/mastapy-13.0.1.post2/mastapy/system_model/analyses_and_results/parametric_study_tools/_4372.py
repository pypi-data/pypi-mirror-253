"""KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.system_deflections import _2771


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"
)


class KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool(
    _4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(
                _4368.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "_6917.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "List[_2771.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool(
            self
        )
