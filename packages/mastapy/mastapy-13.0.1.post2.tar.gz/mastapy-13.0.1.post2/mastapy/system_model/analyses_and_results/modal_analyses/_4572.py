"""AbstractAssemblyModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4662
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434
    from mastapy.system_model.analyses_and_results.modal_analyses import _4635, _4597
    from mastapy.system_model.analyses_and_results.system_deflections import _2685


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyModalAnalysis")


class AbstractAssemblyModalAnalysis(_4662.PartModalAnalysis):
    """AbstractAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyModalAnalysis")

    class _Cast_AbstractAssemblyModalAnalysis:
        """Special nested class for casting AbstractAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            parent: "AbstractAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.AssemblyModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(
                _4651.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.RollingRingAssemblyModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.RootAssemblyModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "AbstractAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyModalAnalysis.TYPE"):
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
    def gear_meshes(self: Self) -> "List[_4635.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(self: Self) -> "List[_4597.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis":
        return self._Cast_AbstractAssemblyModalAnalysis(self)
