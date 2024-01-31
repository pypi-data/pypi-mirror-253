"""PowerLoadCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PowerLoadCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.modal_analyses import _4669


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCompoundModalAnalysis")


class PowerLoadCompoundModalAnalysis(_4849.VirtualComponentCompoundModalAnalysis):
    """PowerLoadCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCompoundModalAnalysis")

    class _Cast_PowerLoadCompoundModalAnalysis:
        """Special nested class for casting PowerLoadCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
            parent: "PowerLoadCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            return self._parent._cast(_4849.VirtualComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
        ) -> "PowerLoadCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4669.PowerLoadModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4669.PowerLoadModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PowerLoadCompoundModalAnalysis._Cast_PowerLoadCompoundModalAnalysis":
        return self._Cast_PowerLoadCompoundModalAnalysis(self)
