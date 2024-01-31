"""CouplingConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6740,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundCriticalSpeedAnalysis")


class CouplingConnectionCompoundCriticalSpeedAnalysis(
    _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """CouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
            parent: "CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(
                _6756.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "CouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CouplingConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6580.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6580.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis(self)
