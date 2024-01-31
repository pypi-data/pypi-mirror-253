"""SpecialisedAssemblyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SpecialisedAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyAdvancedSystemDeflection")


class SpecialisedAssemblyAdvancedSystemDeflection(
    _7270.AbstractAssemblyAdvancedSystemDeflection
):
    """SpecialisedAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(
                _7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def belt_drive_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(_7283.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(
                _7286.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(_7293.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConicalGearSetAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(_7311.CouplingAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CVTAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.FaceGearSetAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.GearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(
                _7356.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(_7378.SpringDamperAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(
                _7386.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.SynchroniserAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.TorqueConverterAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(_7405.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyAdvancedSystemDeflection.TYPE"
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
    ) -> "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyAdvancedSystemDeflection(self)
