"""ConicalGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConicalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.system_deflections import _2725


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetModalAnalysis")


class ConicalGearSetModalAnalysis(_4637.GearSetModalAnalysis):
    """ConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetModalAnalysis")

    class _Cast_ConicalGearSetModalAnalysis:
        """Special nested class for casting ConicalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
            parent: "ConicalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BevelGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(
                _4651.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.ZerolBevelGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
        ) -> "ConicalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2725.ConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection

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
    ) -> "ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis":
        return self._Cast_ConicalGearSetModalAnalysis(self)
