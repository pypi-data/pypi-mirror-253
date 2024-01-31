"""BevelDifferentialSunGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3778


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundStabilityAnalysis")


class BevelDifferentialSunGearCompoundStabilityAnalysis(
    _3908.BevelDifferentialGearCompoundStabilityAnalysis
):
    """BevelDifferentialSunGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundStabilityAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
            parent: "BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3908.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "BevelDifferentialSunGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3778.BevelDifferentialSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialSunGearStabilityAnalysis]

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
    ) -> "List[_3778.BevelDifferentialSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialSunGearStabilityAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis(self)
