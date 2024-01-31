"""VirtualComponentCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5065,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4981,
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="VirtualComponentCompoundModalAnalysisAtAStiffness")


class VirtualComponentCompoundModalAnalysisAtAStiffness(
    _5065.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """VirtualComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_VirtualComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting VirtualComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
            parent: "VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(_5074.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
        ) -> "VirtualComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "VirtualComponentCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4981.VirtualComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.VirtualComponentModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4981.VirtualComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.VirtualComponentModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundModalAnalysisAtAStiffness._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_VirtualComponentCompoundModalAnalysisAtAStiffness(self)
