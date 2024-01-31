"""CouplingHalfModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingHalfModalAnalysisAtASpeed")


class CouplingHalfModalAnalysisAtASpeed(_5195.MountableComponentModalAnalysisAtASpeed):
    """CouplingHalfModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfModalAnalysisAtASpeed")

    class _Cast_CouplingHalfModalAnalysisAtASpeed:
        """Special nested class for casting CouplingHalfModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
            parent: "CouplingHalfModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ClutchHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CVTPulleyModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(
                _5199.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.PulleyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(_5211.RollingRingModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(_5231.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
        ) -> "CouplingHalfModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingHalfModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfModalAnalysisAtASpeed._Cast_CouplingHalfModalAnalysisAtASpeed":
        return self._Cast_CouplingHalfModalAnalysisAtASpeed(self)
