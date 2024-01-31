"""ConceptGearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConceptGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.system_deflections import _2720


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptGearMeshHarmonicAnalysis")


class ConceptGearMeshHarmonicAnalysis(_5755.GearMeshHarmonicAnalysis):
    """ConceptGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshHarmonicAnalysis")

    class _Cast_ConceptGearMeshHarmonicAnalysis:
        """Special nested class for casting ConceptGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
            parent: "ConceptGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(_5755.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
        ) -> "ConceptGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6843.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2720.ConceptGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection

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
    ) -> "ConceptGearMeshHarmonicAnalysis._Cast_ConceptGearMeshHarmonicAnalysis":
        return self._Cast_ConceptGearMeshHarmonicAnalysis(self)
