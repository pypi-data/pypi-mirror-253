"""SpecialisedAssemblyCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCriticalSpeedAnalysis")


class SpecialisedAssemblyCriticalSpeedAnalysis(
    _6542.AbstractAssemblyCriticalSpeedAnalysis
):
    """SpecialisedAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_SpecialisedAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting SpecialisedAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
            parent: "SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6542.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6548,
            )

            return self._parent._cast(
                _6548.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def belt_drive_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(_6552.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(
                _6555.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.CouplingCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.CVTCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.FaceGearSetCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.GearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(
                _6616.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(
                _6626.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.SpringDamperCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(
                _6652.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.TorqueConverterCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6673,
            )

            return self._parent._cast(_6673.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCriticalSpeedAnalysis.TYPE"
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
    ) -> "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis":
        return self._Cast_SpecialisedAssemblyCriticalSpeedAnalysis(self)
