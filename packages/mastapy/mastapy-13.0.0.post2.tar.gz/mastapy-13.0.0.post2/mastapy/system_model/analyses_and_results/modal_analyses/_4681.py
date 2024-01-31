"""SpecialisedAssemblyModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4571
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpecialisedAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.system_deflections import _2806


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysis")


class SpecialisedAssemblyModalAnalysis(_4571.AbstractAssemblyModalAnalysis):
    """SpecialisedAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysis")

    class _Cast_SpecialisedAssemblyModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            parent: "SpecialisedAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            return self._parent._cast(_4571.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RollingRingAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.ZerolBevelGearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "SpecialisedAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2806.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

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
    ) -> "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis":
        return self._Cast_SpecialisedAssemblyModalAnalysis(self)
