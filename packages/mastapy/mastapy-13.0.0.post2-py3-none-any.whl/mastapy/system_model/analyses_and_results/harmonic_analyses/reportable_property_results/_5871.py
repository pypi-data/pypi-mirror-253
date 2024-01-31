"""ResultsForOrderIncludingSurfaces"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER_INCLUDING_SURFACES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForOrderIncludingSurfaces",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5863,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForOrderIncludingSurfaces",)


Self = TypeVar("Self", bound="ResultsForOrderIncludingSurfaces")


class ResultsForOrderIncludingSurfaces(_5870.ResultsForOrderIncludingNodes):
    """ResultsForOrderIncludingSurfaces

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER_INCLUDING_SURFACES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForOrderIncludingSurfaces")

    class _Cast_ResultsForOrderIncludingSurfaces:
        """Special nested class for casting ResultsForOrderIncludingSurfaces to subclasses."""

        def __init__(
            self: "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces",
            parent: "ResultsForOrderIncludingSurfaces",
        ):
            self._parent = parent

        @property
        def results_for_order_including_nodes(
            self: "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces",
        ):
            return self._parent._cast(_5870.ResultsForOrderIncludingNodes)

        @property
        def results_for_order(
            self: "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5868,
            )

            return self._parent._cast(_5868.ResultsForOrder)

        @property
        def results_for_order_including_surfaces(
            self: "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces",
        ) -> "ResultsForOrderIncludingSurfaces":
            return self._parent

        def __getattr__(
            self: "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultsForOrderIncludingSurfaces.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_surfaces(
        self: Self,
    ) -> "List[_5863.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESurfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces":
        return self._Cast_ResultsForOrderIncludingSurfaces(self)
