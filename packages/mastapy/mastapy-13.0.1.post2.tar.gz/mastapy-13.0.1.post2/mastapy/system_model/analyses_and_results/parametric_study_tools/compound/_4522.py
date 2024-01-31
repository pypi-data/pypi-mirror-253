"""PartCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PartCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1850
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PartCompoundParametricStudyTool")


class PartCompoundParametricStudyTool(_7546.PartCompoundAnalysis):
    """PartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundParametricStudyTool")

    class _Cast_PartCompoundParametricStudyTool:
        """Special nested class for casting PartCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
            parent: "PartCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4444,
            )

            return self._parent._cast(_4444.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(
                _4449.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(_4450.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(_4453.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(_4466.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(
                _4471.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(_4479.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(
                _4486.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(_4488.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(
                _4492.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(
                _4493.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(
                _4500.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(_4532.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(_4535.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(
                _4539.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(_4542.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(_4547.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(_4557.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(_4558.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4569,
            )

            return self._parent._cast(_4569.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ) -> "PartCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_logger(self: Self) -> "_1850.DataLoggerWithCharts":
        """mastapy.utility_gui.DataLoggerWithCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4393.PartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4393.PartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool":
        return self._Cast_PartCompoundParametricStudyTool(self)
