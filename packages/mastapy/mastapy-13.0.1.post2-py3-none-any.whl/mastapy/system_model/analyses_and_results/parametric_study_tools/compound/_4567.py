"""WormGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4502,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "WormGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4437


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="WormGearMeshCompoundParametricStudyTool")


class WormGearMeshCompoundParametricStudyTool(
    _4502.GearMeshCompoundParametricStudyTool
):
    """WormGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshCompoundParametricStudyTool"
    )

    class _Cast_WormGearMeshCompoundParametricStudyTool:
        """Special nested class for casting WormGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
            parent: "WormGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4502.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
        ) -> "WormGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2329.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2329.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4437.WormGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4437.WormGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshCompoundParametricStudyTool._Cast_WormGearMeshCompoundParametricStudyTool":
        return self._Cast_WormGearMeshCompoundParametricStudyTool(self)
