"""BevelGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4448,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BevelGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4312


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundParametricStudyTool")


class BevelGearMeshCompoundParametricStudyTool(
    _4448.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
):
    """BevelGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundParametricStudyTool"
    )

    class _Cast_BevelGearMeshCompoundParametricStudyTool:
        """Special nested class for casting BevelGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
            parent: "BevelGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4448.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
        ) -> "BevelGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4312.BevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4312.BevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundParametricStudyTool._Cast_BevelGearMeshCompoundParametricStudyTool":
        return self._Cast_BevelGearMeshCompoundParametricStudyTool(self)
