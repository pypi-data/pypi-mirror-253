"""StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6115,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation(
    _6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(_6024.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation(
            self
        )
