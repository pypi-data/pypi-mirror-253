"""CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5034,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4906,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundModalAnalysisAtAStiffness")


class CylindricalPlanetGearCompoundModalAnalysisAtAStiffness(
    _5034.CylindricalGearCompoundModalAnalysisAtAStiffness
):
    """CylindricalPlanetGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalPlanetGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
            parent: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5034.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(_5045.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4906.CylindricalPlanetGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalPlanetGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4906.CylindricalPlanetGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalPlanetGearModalAnalysisAtAStiffness]

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
    ) -> "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_CylindricalPlanetGearCompoundModalAnalysisAtAStiffness(self)
