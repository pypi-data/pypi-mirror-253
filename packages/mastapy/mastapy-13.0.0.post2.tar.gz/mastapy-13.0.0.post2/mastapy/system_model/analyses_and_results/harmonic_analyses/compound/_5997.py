"""TorqueConverterPumpCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5832


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundHarmonicAnalysis")


class TorqueConverterPumpCompoundHarmonicAnalysis(
    _5917.CouplingHalfCompoundHarmonicAnalysis
):
    """TorqueConverterPumpCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundHarmonicAnalysis"
    )

    class _Cast_TorqueConverterPumpCompoundHarmonicAnalysis:
        """Special nested class for casting TorqueConverterPumpCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
            parent: "TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5917.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
        ) -> "TorqueConverterPumpCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

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
    ) -> "List[_5832.TorqueConverterPumpHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5832.TorqueConverterPumpHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis]

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
    ) -> "TorqueConverterPumpCompoundHarmonicAnalysis._Cast_TorqueConverterPumpCompoundHarmonicAnalysis":
        return self._Cast_TorqueConverterPumpCompoundHarmonicAnalysis(self)
