"""GearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "GearSetModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.system_deflections import _2760


__docformat__ = "restructuredtext en"
__all__ = ("GearSetModalAnalysis",)


Self = TypeVar("Self", bound="GearSetModalAnalysis")


class GearSetModalAnalysis(_4682.SpecialisedAssemblyModalAnalysis):
    """GearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetModalAnalysis")

    class _Cast_GearSetModalAnalysis:
        """Special nested class for casting GearSetModalAnalysis to subclasses."""

        def __init__(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
            parent: "GearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BevelGearSetModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearSetModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.FaceGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(
                _4651.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def planetary_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PlanetaryGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.StraightBevelGearSetModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.ZerolBevelGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis",
        ) -> "GearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetModalAnalysis._Cast_GearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2532.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2760.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSetModalAnalysis._Cast_GearSetModalAnalysis":
        return self._Cast_GearSetModalAnalysis(self)
