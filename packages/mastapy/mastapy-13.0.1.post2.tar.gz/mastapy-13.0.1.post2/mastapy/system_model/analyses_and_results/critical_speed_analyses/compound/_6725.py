"""CylindricalPlanetGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6722,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6596


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundCriticalSpeedAnalysis")


class CylindricalPlanetGearCompoundCriticalSpeedAnalysis(
    _6722.CylindricalGearCompoundCriticalSpeedAnalysis
):
    """CylindricalPlanetGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
            parent: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6722.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6596.CylindricalPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CylindricalPlanetGearCriticalSpeedAnalysis]

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
    ) -> "List[_6596.CylindricalPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CylindricalPlanetGearCriticalSpeedAnalysis]

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
    ) -> "CylindricalPlanetGearCompoundCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundCriticalSpeedAnalysis(self)
