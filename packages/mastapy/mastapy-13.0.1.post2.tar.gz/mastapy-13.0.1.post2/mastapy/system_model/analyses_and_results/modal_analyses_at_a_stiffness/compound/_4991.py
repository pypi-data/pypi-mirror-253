"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4860,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
    _5023.ConnectionCompoundModalAnalysisAtAStiffness
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(
                _5032.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(
                _5034.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(
                _5071.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
