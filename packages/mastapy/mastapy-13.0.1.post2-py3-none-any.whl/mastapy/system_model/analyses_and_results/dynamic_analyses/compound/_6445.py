"""CouplingCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CouplingCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundDynamicAnalysis")


class CouplingCompoundDynamicAnalysis(_6506.SpecialisedAssemblyCompoundDynamicAnalysis):
    """CouplingCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundDynamicAnalysis")

    class _Cast_CouplingCompoundDynamicAnalysis:
        """Special nested class for casting CouplingCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
            parent: "CouplingCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(
                _6488.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(_6510.SpringDamperCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.TorqueConverterCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
        ) -> "CouplingCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_6315.CouplingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6315.CouplingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis":
        return self._Cast_CouplingCompoundDynamicAnalysis(self)
