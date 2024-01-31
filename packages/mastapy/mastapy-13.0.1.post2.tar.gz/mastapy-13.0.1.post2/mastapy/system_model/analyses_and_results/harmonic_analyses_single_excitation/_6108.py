"""SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6008,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation")


class SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation(
    _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
):
    """SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(_6018.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(_6031.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(
                _6094.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
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
    ) -> "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation(self)
