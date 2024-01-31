"""TorqueConverterTurbineCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "TorqueConverterTurbineCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundDynamicAnalysis")


class TorqueConverterTurbineCompoundDynamicAnalysis(
    _6446.CouplingHalfCompoundDynamicAnalysis
):
    """TorqueConverterTurbineCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundDynamicAnalysis"
    )

    class _Cast_TorqueConverterTurbineCompoundDynamicAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
            parent: "TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6446.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
        ) -> "TorqueConverterTurbineCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_6398.TorqueConverterTurbineDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis]

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
    ) -> "List[_6398.TorqueConverterTurbineDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis]

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
    ) -> "TorqueConverterTurbineCompoundDynamicAnalysis._Cast_TorqueConverterTurbineCompoundDynamicAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundDynamicAnalysis(self)
