"""TorqueConverterPumpModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "TorqueConverterPumpModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6974
    from mastapy.system_model.analyses_and_results.system_deflections import _2829


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpModalAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterPumpModalAnalysis")


class TorqueConverterPumpModalAnalysis(_4610.CouplingHalfModalAnalysis):
    """TorqueConverterPumpModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpModalAnalysis")

    class _Cast_TorqueConverterPumpModalAnalysis:
        """Special nested class for casting TorqueConverterPumpModalAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
            parent: "TorqueConverterPumpModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            return self._parent._cast(_4610.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
        ) -> "TorqueConverterPumpModalAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6974.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "_2829.TorqueConverterPumpSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection

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
    ) -> "TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis":
        return self._Cast_TorqueConverterPumpModalAnalysis(self)
