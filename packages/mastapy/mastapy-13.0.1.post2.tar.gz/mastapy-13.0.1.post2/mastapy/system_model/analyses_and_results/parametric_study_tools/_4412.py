"""SpecialisedAssemblyParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpecialisedAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyParametricStudyTool")


class SpecialisedAssemblyParametricStudyTool(_4296.AbstractAssemblyParametricStudyTool):
    """SpecialisedAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
            parent: "SpecialisedAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            return self._parent._cast(_4296.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(
                _4302.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def belt_drive_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(
                _4371.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(
                _4374.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(
                _4377.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.RollingRingAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.ZerolBevelGearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "SpecialisedAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2476.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool":
        return self._Cast_SpecialisedAssemblyParametricStudyTool(self)
