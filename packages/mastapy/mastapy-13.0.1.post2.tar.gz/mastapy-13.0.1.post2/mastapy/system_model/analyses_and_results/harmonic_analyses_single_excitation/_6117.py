"""StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6026,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6115,
        _6116,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation(
    _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6962.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6116.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation(
            self
        )
