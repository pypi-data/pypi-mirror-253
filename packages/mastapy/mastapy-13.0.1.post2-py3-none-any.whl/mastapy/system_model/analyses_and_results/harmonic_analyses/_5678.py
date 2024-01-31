"""AbstractAssemblyHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434
    from mastapy.system_model.analyses_and_results.system_deflections import _2685


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyHarmonicAnalysis")


class AbstractAssemblyHarmonicAnalysis(_5788.PartHarmonicAnalysis):
    """AbstractAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyHarmonicAnalysis")

    class _Cast_AbstractAssemblyHarmonicAnalysis:
        """Special nested class for casting AbstractAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
            parent: "AbstractAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AssemblyHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BoltedJointHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.ConicalGearSetHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CVTHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CylindricalGearSetHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.FaceGearSetHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PlanetaryGearSetHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.RollingRingAssemblyHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.RootAssemblyHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.StraightBevelGearSetHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.SynchroniserHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.TorqueConverterHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
        ) -> "AbstractAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyHarmonicAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2685.AbstractAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyHarmonicAnalysis._Cast_AbstractAssemblyHarmonicAnalysis":
        return self._Cast_AbstractAssemblyHarmonicAnalysis(self)
