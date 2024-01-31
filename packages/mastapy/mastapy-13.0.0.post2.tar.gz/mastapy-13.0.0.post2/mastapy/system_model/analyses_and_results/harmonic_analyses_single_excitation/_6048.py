"""CVTHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CVTHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586


__docformat__ = "restructuredtext en"
__all__ = ("CVTHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTHarmonicAnalysisOfSingleExcitation")


class CVTHarmonicAnalysisOfSingleExcitation(
    _6017.BeltDriveHarmonicAnalysisOfSingleExcitation
):
    """CVTHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
            parent: "CVTHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6017.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6007,
            )

            return self._parent._cast(
                _6007.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "CVTHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTHarmonicAnalysisOfSingleExcitation(self)
