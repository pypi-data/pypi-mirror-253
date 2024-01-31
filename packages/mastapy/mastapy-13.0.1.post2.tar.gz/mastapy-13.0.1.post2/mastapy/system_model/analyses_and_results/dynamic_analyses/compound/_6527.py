"""TorqueConverterPumpCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "TorqueConverterPumpCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundDynamicAnalysis")


class TorqueConverterPumpCompoundDynamicAnalysis(
    _6447.CouplingHalfCompoundDynamicAnalysis
):
    """TorqueConverterPumpCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundDynamicAnalysis"
    )

    class _Cast_TorqueConverterPumpCompoundDynamicAnalysis:
        """Special nested class for casting TorqueConverterPumpCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
            parent: "TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6447.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
        ) -> "TorqueConverterPumpCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpCompoundDynamicAnalysis.TYPE"
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
    ) -> "List[_6398.TorqueConverterPumpDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis]

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
    ) -> "List[_6398.TorqueConverterPumpDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis]

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
    ) -> "TorqueConverterPumpCompoundDynamicAnalysis._Cast_TorqueConverterPumpCompoundDynamicAnalysis":
        return self._Cast_TorqueConverterPumpCompoundDynamicAnalysis(self)
