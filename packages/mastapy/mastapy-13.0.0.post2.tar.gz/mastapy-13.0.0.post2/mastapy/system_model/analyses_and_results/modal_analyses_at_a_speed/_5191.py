"""MassDiscModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6921


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="MassDiscModalAnalysisAtASpeed")


class MassDiscModalAnalysisAtASpeed(_5239.VirtualComponentModalAnalysisAtASpeed):
    """MassDiscModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscModalAnalysisAtASpeed")

    class _Cast_MassDiscModalAnalysisAtASpeed:
        """Special nested class for casting MassDiscModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
            parent: "MassDiscModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5239.VirtualComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
        ) -> "MassDiscModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6921.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.MassDiscModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "MassDiscModalAnalysisAtASpeed._Cast_MassDiscModalAnalysisAtASpeed":
        return self._Cast_MassDiscModalAnalysisAtASpeed(self)
