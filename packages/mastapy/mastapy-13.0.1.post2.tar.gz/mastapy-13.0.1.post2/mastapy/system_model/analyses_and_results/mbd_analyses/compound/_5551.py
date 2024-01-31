"""ClutchConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ClutchConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5399


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ClutchConnectionCompoundMultibodyDynamicsAnalysis")


class ClutchConnectionCompoundMultibodyDynamicsAnalysis(
    _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
):
    """ClutchConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ClutchConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(_5564.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ClutchConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5399.ClutchConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchConnectionMultibodyDynamicsAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5399.ClutchConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchConnectionMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ClutchConnectionCompoundMultibodyDynamicsAnalysis._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ClutchConnectionCompoundMultibodyDynamicsAnalysis(self)
