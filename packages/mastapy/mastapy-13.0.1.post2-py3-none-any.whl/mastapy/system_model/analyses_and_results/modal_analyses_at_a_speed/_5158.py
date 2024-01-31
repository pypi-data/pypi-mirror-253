"""CVTModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CVTModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtASpeed")


class CVTModalAnalysisAtASpeed(_5127.BeltDriveModalAnalysisAtASpeed):
    """CVTModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtASpeed")

    class _Cast_CVTModalAnalysisAtASpeed:
        """Special nested class for casting CVTModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
            parent: "CVTModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5127.BeltDriveModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "CVTModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed":
        return self._Cast_CVTModalAnalysisAtASpeed(self)
