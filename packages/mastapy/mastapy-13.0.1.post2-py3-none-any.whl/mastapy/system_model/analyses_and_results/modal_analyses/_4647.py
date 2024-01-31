"""KlingelnbergCycloPalloidHypoidGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.system_deflections import _2773


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearModalAnalysis")


class KlingelnbergCycloPalloidHypoidGearModalAnalysis(
    _4644.KlingelnbergCycloPalloidConicalGearModalAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6916.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2773.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidHypoidGearModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearModalAnalysis(self)
