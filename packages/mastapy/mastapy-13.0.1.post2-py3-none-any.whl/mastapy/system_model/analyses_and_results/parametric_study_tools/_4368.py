"""InterMountableComponentConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "InterMountableComponentConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionParametricStudyTool")


class InterMountableComponentConnectionParametricStudyTool(
    _4331.ConnectionParametricStudyTool
):
    """InterMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionParametricStudyTool"
    )

    class _Cast_InterMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting InterMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
            parent: "InterMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            return self._parent._cast(_4331.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(
                _4300.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def belt_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(
                _4307.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ClutchConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(
                _4322.ConceptCouplingConnectionParametricStudyTool
            )

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConicalGearMeshParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.CVTBeltConnectionParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.HypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.PartToPartShearCouplingConnectionParametricStudyTool
            )

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.RollingRingConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(
                _4419.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(
                _4431.TorqueConverterConnectionParametricStudyTool
            )

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.ZerolBevelGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
        ) -> "InterMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "InterMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2281.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool":
        return self._Cast_InterMountableComponentConnectionParametricStudyTool(self)
