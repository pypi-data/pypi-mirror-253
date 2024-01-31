"""AbstractAssemblyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6754,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundCriticalSpeedAnalysis")


class AbstractAssemblyCompoundCriticalSpeedAnalysis(
    _6754.PartCompoundCriticalSpeedAnalysis
):
    """AbstractAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
            parent: "AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(_6682.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(_6685.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6695,
            )

            return self._parent._cast(_6695.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(
                _6732.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(_6777.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(_6788.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6792,
            )

            return self._parent._cast(
                _6792.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6543.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    ) -> "List[_6543.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis(self)
