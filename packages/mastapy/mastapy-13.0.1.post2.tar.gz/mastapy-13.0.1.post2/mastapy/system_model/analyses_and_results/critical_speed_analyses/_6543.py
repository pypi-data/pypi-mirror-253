"""AbstractAssemblyCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AbstractAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCriticalSpeedAnalysis")


class AbstractAssemblyCriticalSpeedAnalysis(_6625.PartCriticalSpeedAnalysis):
    """AbstractAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_AbstractAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting AbstractAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
            parent: "AbstractAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(
                _6549.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.AssemblyCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(_6553.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(_6563.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(_6581.CouplingCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.CVTCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.FaceGearSetCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(
                _6627.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.RootAssemblyCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.SpringDamperCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.SynchroniserCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.TorqueConverterCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "AbstractAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis":
        return self._Cast_AbstractAssemblyCriticalSpeedAnalysis(self)
