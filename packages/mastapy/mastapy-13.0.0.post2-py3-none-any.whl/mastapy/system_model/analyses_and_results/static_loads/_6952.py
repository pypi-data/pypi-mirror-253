"""SpecialisedAssemblyLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyLoadCase",)


Self = TypeVar("Self", bound="SpecialisedAssemblyLoadCase")


class SpecialisedAssemblyLoadCase(_6806.AbstractAssemblyLoadCase):
    """SpecialisedAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyLoadCase")

    class _Cast_SpecialisedAssemblyLoadCase:
        """Special nested class for casting SpecialisedAssemblyLoadCase to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            parent: "SpecialisedAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AGMAGleasonConicalGearSetLoadCase)

        @property
        def belt_drive_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(
                _6920.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RollingRingAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.ZerolBevelGearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "SpecialisedAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyLoadCase.TYPE"):
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
    ) -> "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase":
        return self._Cast_SpecialisedAssemblyLoadCase(self)
