"""FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6268
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_DETAIL_LEVEL_AND_PIN_FATIGUE_ONE_TOOTH_PASS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
)


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass")


class FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass(
    _6268.FlexiblePinAnalysis
):
    """FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_DETAIL_LEVEL_AND_PIN_FATIGUE_ONE_TOOTH_PASS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    )

    class _Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass:
        """Special nested class for casting FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
            parent: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
        ):
            return self._parent._cast(_6268.FlexiblePinAnalysis)

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
        ):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6267,
            )

            return self._parent._cast(_6267.CombinationAnalysis)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(
            self: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
        ) -> "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
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
        instance_to_wrap: "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass":
        return self._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass(self)
