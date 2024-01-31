"""UnbalancedMassCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4019
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "UnbalancedMassCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.stability_analyses import _3889


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundStabilityAnalysis")


class UnbalancedMassCompoundStabilityAnalysis(
    _4019.VirtualComponentCompoundStabilityAnalysis
):
    """UnbalancedMassCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundStabilityAnalysis"
    )

    class _Cast_UnbalancedMassCompoundStabilityAnalysis:
        """Special nested class for casting UnbalancedMassCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
            parent: "UnbalancedMassCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_stability_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_4019.VirtualComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
        ) -> "UnbalancedMassCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_3889.UnbalancedMassStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.UnbalancedMassStabilityAnalysis]

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
    ) -> "List[_3889.UnbalancedMassStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.UnbalancedMassStabilityAnalysis]

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
    ) -> "UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis":
        return self._Cast_UnbalancedMassCompoundStabilityAnalysis(self)
