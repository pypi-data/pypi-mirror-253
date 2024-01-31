"""SynchroniserHalfModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4699
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.system_deflections import _2821


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfModalAnalysis")


class SynchroniserHalfModalAnalysis(_4699.SynchroniserPartModalAnalysis):
    """SynchroniserHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfModalAnalysis")

    class _Cast_SynchroniserHalfModalAnalysis:
        """Special nested class for casting SynchroniserHalfModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
            parent: "SynchroniserHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            return self._parent._cast(_4699.SynchroniserPartModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "SynchroniserHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6968.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

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
    ) -> "_2821.SynchroniserHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection

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
    ) -> "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis":
        return self._Cast_SynchroniserHalfModalAnalysis(self)
