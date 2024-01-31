"""CVTBeltConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5418


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundMultibodyDynamicsAnalysis")


class CVTBeltConnectionCompoundMultibodyDynamicsAnalysis(
    _5537.BeltConnectionCompoundMultibodyDynamicsAnalysis
):
    """CVTBeltConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5537.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(_5563.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5418.CVTBeltConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTBeltConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5418.CVTBeltConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTBeltConnectionMultibodyDynamicsAnalysis]

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
    ) -> "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis(self)
