"""AGMAGleasonConicalGearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2299


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshParametricStudyTool")


class AGMAGleasonConicalGearMeshParametricStudyTool(
    _4328.ConicalGearMeshParametricStudyTool
):
    """AGMAGleasonConicalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearMeshParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
            parent: "AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            return self._parent._cast(_4328.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(
                _4368.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(
                _4307.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BevelGearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.HypoidGearMeshParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpiralBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(
                _4419.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.ZerolBevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "AGMAGleasonConicalGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearMeshParametricStudyTool(self)
