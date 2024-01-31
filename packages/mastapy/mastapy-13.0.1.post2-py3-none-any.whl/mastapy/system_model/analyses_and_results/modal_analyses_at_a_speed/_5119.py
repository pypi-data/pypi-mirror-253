"""AbstractShaftOrHousingModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysisAtASpeed")


class AbstractShaftOrHousingModalAnalysisAtASpeed(_5142.ComponentModalAnalysisAtASpeed):
    """AbstractShaftOrHousingModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysisAtASpeed"
    )

    class _Cast_AbstractShaftOrHousingModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
            parent: "AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(_5118.AbstractShaftModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.FEPartModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.ShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
        ) -> "AbstractShaftOrHousingModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftOrHousingModalAnalysisAtASpeed(self)
