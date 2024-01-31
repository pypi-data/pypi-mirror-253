"""DesignEntityModalAnalysisGroupResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_MODAL_ANALYSIS_GROUP_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "DesignEntityModalAnalysisGroupResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntityModalAnalysisGroupResults",)


Self = TypeVar("Self", bound="DesignEntityModalAnalysisGroupResults")


class DesignEntityModalAnalysisGroupResults(_0.APIBase):
    """DesignEntityModalAnalysisGroupResults

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_MODAL_ANALYSIS_GROUP_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DesignEntityModalAnalysisGroupResults"
    )

    class _Cast_DesignEntityModalAnalysisGroupResults:
        """Special nested class for casting DesignEntityModalAnalysisGroupResults to subclasses."""

        def __init__(
            self: "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults",
            parent: "DesignEntityModalAnalysisGroupResults",
        ):
            self._parent = parent

        @property
        def single_excitation_results_modal_analysis(
            self: "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4725,
            )

            return self._parent._cast(_4725.SingleExcitationResultsModalAnalysis)

        @property
        def single_mode_results(
            self: "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4726,
            )

            return self._parent._cast(_4726.SingleModeResults)

        @property
        def design_entity_modal_analysis_group_results(
            self: "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults",
        ) -> "DesignEntityModalAnalysisGroupResults":
            return self._parent

        def __getattr__(
            self: "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults",
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
        self: Self, instance_to_wrap: "DesignEntityModalAnalysisGroupResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults":
        return self._Cast_DesignEntityModalAnalysisGroupResults(self)
