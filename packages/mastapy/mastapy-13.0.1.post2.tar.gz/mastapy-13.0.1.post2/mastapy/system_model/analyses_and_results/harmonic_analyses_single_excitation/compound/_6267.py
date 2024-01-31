"""ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6157,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6138,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6265,
        _6266,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"
)


class ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    def zerol_bevel_gears_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6265.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6266.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
