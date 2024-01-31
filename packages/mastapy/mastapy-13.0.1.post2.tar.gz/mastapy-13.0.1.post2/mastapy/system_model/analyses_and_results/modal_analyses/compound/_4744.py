"""BevelGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4732
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4589


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundModalAnalysis")


class BevelGearCompoundModalAnalysis(_4732.AGMAGleasonConicalGearCompoundModalAnalysis):
    """BevelGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundModalAnalysis")

    class _Cast_BevelGearCompoundModalAnalysis:
        """Special nested class for casting BevelGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
            parent: "BevelGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            return self._parent._cast(_4732.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(_4739.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(_4854.ZerolBevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
        ) -> "BevelGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4589.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

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
    ) -> "List[_4589.BevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis]

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
    ) -> "BevelGearCompoundModalAnalysis._Cast_BevelGearCompoundModalAnalysis":
        return self._Cast_BevelGearCompoundModalAnalysis(self)
