"""CouplingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHarmonicAnalysisOfSingleExcitation")


class CouplingHarmonicAnalysisOfSingleExcitation(
    _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """CouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(_6031.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "CouplingHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHarmonicAnalysisOfSingleExcitation(self)
