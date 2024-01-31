"""CompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("CompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CompoundAdvancedTimeSteppingAnalysisForModulation")


class CompoundAdvancedTimeSteppingAnalysisForModulation(_2619.CompoundAnalysis):
    """CompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_CompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(_2619.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_time_stepping_analysis_for_modulation(
            self: "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation(self)
