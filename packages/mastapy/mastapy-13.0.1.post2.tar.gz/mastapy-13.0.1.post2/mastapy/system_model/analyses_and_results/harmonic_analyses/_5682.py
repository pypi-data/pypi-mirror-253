"""AbstractShaftToMountableComponentConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2265
    from mastapy.system_model.analyses_and_results.system_deflections import _2688


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionHarmonicAnalysis"
)


class AbstractShaftToMountableComponentConnectionHarmonicAnalysis(
    _5715.ConnectionHarmonicAnalysis
):
    """AbstractShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(
                _5724.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(
                _5726.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(
                _5808.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2265.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2688.AbstractShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftToMountableComponentConnectionSystemDeflection

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
    ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis(
            self
        )
