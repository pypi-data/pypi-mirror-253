"""AbstractShaftToMountableComponentConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftToMountableComponentConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2265
    from mastapy.system_model.analyses_and_results.system_deflections import _2688


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnectionModalAnalysis")


class AbstractShaftToMountableComponentConnectionModalAnalysis(
    _4607.ConnectionModalAnalysis
):
    """AbstractShaftToMountableComponentConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionModalAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            return self._parent._cast(_4607.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.CoaxialConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(
                _4617.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(
                _4619.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PlanetaryConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(
                _4681.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionModalAnalysis.TYPE",
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
    ) -> "AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis(self)
