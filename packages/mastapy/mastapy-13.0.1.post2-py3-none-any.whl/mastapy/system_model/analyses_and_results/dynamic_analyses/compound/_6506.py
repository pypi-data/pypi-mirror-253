"""SpecialisedAssemblyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpecialisedAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundDynamicAnalysis")


class SpecialisedAssemblyCompoundDynamicAnalysis(
    _6408.AbstractAssemblyCompoundDynamicAnalysis
):
    """SpecialisedAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
            parent: "SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(_6418.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(
                _6488.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(_6510.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "SpecialisedAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6377.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "List[_6377.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundDynamicAnalysis(self)
