"""MeasurementComponentCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "MeasurementComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundDynamicAnalysis")


class MeasurementComponentCompoundDynamicAnalysis(
    _6530.VirtualComponentCompoundDynamicAnalysis
):
    """MeasurementComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundDynamicAnalysis"
    )

    class _Cast_MeasurementComponentCompoundDynamicAnalysis:
        """Special nested class for casting MeasurementComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
            parent: "MeasurementComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6530.VirtualComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
        ) -> "MeasurementComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

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
    ) -> "List[_6355.MeasurementComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis]

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
    ) -> "List[_6355.MeasurementComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis]

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
    ) -> "MeasurementComponentCompoundDynamicAnalysis._Cast_MeasurementComponentCompoundDynamicAnalysis":
        return self._Cast_MeasurementComponentCompoundDynamicAnalysis(self)
