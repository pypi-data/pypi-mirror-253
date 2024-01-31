"""ConicalGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConicalGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5150,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearCompoundModalAnalysisAtASpeed")


class ConicalGearCompoundModalAnalysisAtASpeed(_5305.GearCompoundModalAnalysisAtASpeed):
    """ConicalGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConicalGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConicalGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
            parent: "ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5305.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(
                _5251.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(
                _5261.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(
                _5262.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(
                _5313.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(
                _5316.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(_5373.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "ConicalGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.ConicalGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5150.ConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearModalAnalysisAtASpeed]

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
    ) -> "List[_5150.ConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearModalAnalysisAtASpeed]

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
    ) -> "ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed":
        return self._Cast_ConicalGearCompoundModalAnalysisAtASpeed(self)
