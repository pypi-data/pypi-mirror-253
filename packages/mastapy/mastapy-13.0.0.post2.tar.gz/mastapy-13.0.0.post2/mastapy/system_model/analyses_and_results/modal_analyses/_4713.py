"""ZerolBevelGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4588
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ZerolBevelGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.system_deflections import _2841


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearModalAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearModalAnalysis")


class ZerolBevelGearModalAnalysis(_4588.BevelGearModalAnalysis):
    """ZerolBevelGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearModalAnalysis")

    class _Cast_ZerolBevelGearModalAnalysis:
        """Special nested class for casting ZerolBevelGearModalAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
            parent: "ZerolBevelGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            return self._parent._cast(_4588.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
        ) -> "ZerolBevelGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6985.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2841.ZerolBevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection

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
    ) -> "ZerolBevelGearModalAnalysis._Cast_ZerolBevelGearModalAnalysis":
        return self._Cast_ZerolBevelGearModalAnalysis(self)
