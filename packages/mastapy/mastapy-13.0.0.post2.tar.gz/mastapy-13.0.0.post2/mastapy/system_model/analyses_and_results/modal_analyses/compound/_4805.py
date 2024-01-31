"""OilSealCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "OilSealCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.modal_analyses import _4659


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundModalAnalysis",)


Self = TypeVar("Self", bound="OilSealCompoundModalAnalysis")


class OilSealCompoundModalAnalysis(_4763.ConnectorCompoundModalAnalysis):
    """OilSealCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundModalAnalysis")

    class _Cast_OilSealCompoundModalAnalysis:
        """Special nested class for casting OilSealCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
            parent: "OilSealCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_modal_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            return self._parent._cast(_4763.ConnectorCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
        ) -> "OilSealCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

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
    ) -> "List[_4659.OilSealModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4659.OilSealModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis]

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
    ) -> "OilSealCompoundModalAnalysis._Cast_OilSealCompoundModalAnalysis":
        return self._Cast_OilSealCompoundModalAnalysis(self)
