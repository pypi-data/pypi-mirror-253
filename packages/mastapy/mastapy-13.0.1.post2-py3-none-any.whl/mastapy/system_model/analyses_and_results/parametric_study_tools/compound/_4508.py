"""InterMountableComponentConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4478,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "InterMountableComponentConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundParametricStudyTool"
)


class InterMountableComponentConnectionCompoundParametricStudyTool(
    _4478.ConnectionCompoundParametricStudyTool
):
    """InterMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
    )

    class _Cast_InterMountableComponentConnectionCompoundParametricStudyTool:
        """Special nested class for casting InterMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
            parent: "InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4448,
            )

            return self._parent._cast(
                _4448.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(_4460.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ClutchConnectionCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(
                _4481.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(
                _4483.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(
                _4491.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(_4506.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(
                _4524.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.RingPinsToDiscConnectionCompoundParametricStudyTool
            )

        @property
        def rolling_ring_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.RollingRingConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(_4567.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4368.InterMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool]

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
    ) -> "List[_4368.InterMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool]

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
    ) -> "InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool":
        return self._Cast_InterMountableComponentConnectionCompoundParametricStudyTool(
            self
        )
