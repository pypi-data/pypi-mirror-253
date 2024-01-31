"""VirtualComponentCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "VirtualComponentCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5837


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundHarmonicAnalysis")


class VirtualComponentCompoundHarmonicAnalysis(
    _5956.MountableComponentCompoundHarmonicAnalysis
):
    """VirtualComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundHarmonicAnalysis"
    )

    class _Cast_VirtualComponentCompoundHarmonicAnalysis:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
            parent: "VirtualComponentCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def point_load_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PowerLoadCompoundHarmonicAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "VirtualComponentCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5837.VirtualComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis]

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
    ) -> "List[_5837.VirtualComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis]

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
    ) -> "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis":
        return self._Cast_VirtualComponentCompoundHarmonicAnalysis(self)
