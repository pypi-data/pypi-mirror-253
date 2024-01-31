"""ConicalGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConicalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.system_deflections import _2726


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearModalAnalysis")


class ConicalGearModalAnalysis(_4636.GearModalAnalysis):
    """ConicalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearModalAnalysis")

    class _Cast_ConicalGearModalAnalysis:
        """Special nested class for casting ConicalGearModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
            parent: "ConicalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelGearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelSunGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.ZerolBevelGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis",
        ) -> "ConicalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2726.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

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
    ) -> "ConicalGearModalAnalysis._Cast_ConicalGearModalAnalysis":
        return self._Cast_ConicalGearModalAnalysis(self)
