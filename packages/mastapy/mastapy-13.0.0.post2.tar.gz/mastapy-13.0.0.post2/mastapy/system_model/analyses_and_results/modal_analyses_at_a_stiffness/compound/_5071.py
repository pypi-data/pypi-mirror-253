"""PlanetaryGearSetCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4942,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundModalAnalysisAtAStiffness")


class PlanetaryGearSetCompoundModalAnalysisAtAStiffness(
    _5036.CylindricalGearSetCompoundModalAnalysisAtAStiffness
):
    """PlanetaryGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetaryGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
            parent: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5036.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4987,
            )

            return self._parent._cast(
                _4987.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PlanetaryGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4942.PlanetaryGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PlanetaryGearSetModalAnalysisAtAStiffness]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4942.PlanetaryGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PlanetaryGearSetModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundModalAnalysisAtAStiffness._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_PlanetaryGearSetCompoundModalAnalysisAtAStiffness(self)
