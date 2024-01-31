"""CouplingHalfCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CouplingHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3801


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundStabilityAnalysis")


class CouplingHalfCompoundStabilityAnalysis(
    _3974.MountableComponentCompoundStabilityAnalysis
):
    """CouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundStabilityAnalysis"
    )

    class _Cast_CouplingHalfCompoundStabilityAnalysis:
        """Special nested class for casting CouplingHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
            parent: "CouplingHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(
                _3925.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CVTPulleyCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(_3985.PulleyCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.RollingRingCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(_4001.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(
                _4017.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "CouplingHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3801.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3801.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis":
        return self._Cast_CouplingHalfCompoundStabilityAnalysis(self)
