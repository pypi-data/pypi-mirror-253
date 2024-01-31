"""CylindricalPlanetGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CylindricalPlanetGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundDynamicAnalysis")


class CylindricalPlanetGearCompoundDynamicAnalysis(
    _6454.CylindricalGearCompoundDynamicAnalysis
):
    """CylindricalPlanetGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundDynamicAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundDynamicAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
            parent: "CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6454.CylindricalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
        ) -> "CylindricalPlanetGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6326.CylindricalPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis]

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
    ) -> "List[_6326.CylindricalPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis]

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
    ) -> "CylindricalPlanetGearCompoundDynamicAnalysis._Cast_CylindricalPlanetGearCompoundDynamicAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundDynamicAnalysis(self)
