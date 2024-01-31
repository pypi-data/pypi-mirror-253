"""AbstractShaftCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5376


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundMultibodyDynamicsAnalysis")


class AbstractShaftCompoundMultibodyDynamicsAnalysis(
    _5530.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5530.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(
                _5573.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(_5623.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5376.AbstractShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis]

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
    ) -> "List[_5376.AbstractShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis]

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
    ) -> "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis(self)
