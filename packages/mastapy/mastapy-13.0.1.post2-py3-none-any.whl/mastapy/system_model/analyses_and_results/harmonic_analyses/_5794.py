"""PlanetaryGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PlanetaryGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetHarmonicAnalysis")


class PlanetaryGearSetHarmonicAnalysis(_5729.CylindricalGearSetHarmonicAnalysis):
    """PlanetaryGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetHarmonicAnalysis")

    class _Cast_PlanetaryGearSetHarmonicAnalysis:
        """Special nested class for casting PlanetaryGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
            parent: "PlanetaryGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5729.CylindricalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ) -> "PlanetaryGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis":
        return self._Cast_PlanetaryGearSetHarmonicAnalysis(self)
