"""BeltDriveCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5344,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "BeltDriveCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5126,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BeltDriveCompoundModalAnalysisAtASpeed")


class BeltDriveCompoundModalAnalysisAtASpeed(
    _5344.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
):
    """BeltDriveCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveCompoundModalAnalysisAtASpeed"
    )

    class _Cast_BeltDriveCompoundModalAnalysisAtASpeed:
        """Special nested class for casting BeltDriveCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
            parent: "BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5344.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5246,
            )

            return self._parent._cast(
                _5246.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.CVTCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
        ) -> "BeltDriveCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5126.BeltDriveModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BeltDriveModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5126.BeltDriveModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BeltDriveModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveCompoundModalAnalysisAtASpeed._Cast_BeltDriveCompoundModalAnalysisAtASpeed":
        return self._Cast_BeltDriveCompoundModalAnalysisAtASpeed(self)
