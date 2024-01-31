"""BeltDriveHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BeltDriveHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BeltDriveHarmonicAnalysisOfSingleExcitation")


class BeltDriveHarmonicAnalysisOfSingleExcitation(
    _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """BeltDriveHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BeltDriveHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltDriveHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
            parent: "BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
        ) -> "BeltDriveHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "BeltDriveHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation(self)
