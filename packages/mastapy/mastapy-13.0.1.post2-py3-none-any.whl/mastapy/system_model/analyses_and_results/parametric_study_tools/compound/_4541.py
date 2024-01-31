"""SpecialisedAssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4443,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpecialisedAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4412


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundParametricStudyTool")


class SpecialisedAssemblyCompoundParametricStudyTool(
    _4443.AbstractAssemblyCompoundParametricStudyTool
):
    """SpecialisedAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyCompoundParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
            parent: "SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(
                _4449.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(_4453.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConicalGearSetCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CouplingCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CVTCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(
                _4486.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(
                _4492.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.FaceGearSetCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(
                _4500.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.SpringDamperCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.SynchroniserCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.TorqueConverterCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "SpecialisedAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4412.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4412.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool":
        return self._Cast_SpecialisedAssemblyCompoundParametricStudyTool(self)
