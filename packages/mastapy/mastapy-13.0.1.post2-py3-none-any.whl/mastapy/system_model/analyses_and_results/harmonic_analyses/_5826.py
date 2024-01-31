"""StraightBevelSunGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5819
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelSunGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.system_deflections import _2820


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearHarmonicAnalysis")


class StraightBevelSunGearHarmonicAnalysis(_5819.StraightBevelDiffGearHarmonicAnalysis):
    """StraightBevelSunGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearHarmonicAnalysis")

    class _Cast_StraightBevelSunGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelSunGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
            parent: "StraightBevelSunGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5819.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "StraightBevelSunGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2820.StraightBevelSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis":
        return self._Cast_StraightBevelSunGearHarmonicAnalysis(self)
