"""CylindricalGearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CylindricalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7322,
    )
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.static_loads import _6864
    from mastapy.system_model.analyses_and_results.system_deflections import _2739


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshHarmonicAnalysis")


class CylindricalGearMeshHarmonicAnalysis(_5755.GearMeshHarmonicAnalysis):
    """CylindricalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshHarmonicAnalysis")

    class _Cast_CylindricalGearMeshHarmonicAnalysis:
        """Special nested class for casting CylindricalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
            parent: "CylindricalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(_5755.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
        ) -> "CylindricalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_results(
        self: Self,
    ) -> "_7322.CylindricalGearMeshAdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6864.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

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
    ) -> "_2739.CylindricalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearMeshHarmonicAnalysis._Cast_CylindricalGearMeshHarmonicAnalysis"
    ):
        return self._Cast_CylindricalGearMeshHarmonicAnalysis(self)
