"""AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5378


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis")


class AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(
    _5554.ComponentCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(_5624.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5378.AbstractShaftOrHousingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis]

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
    ) -> "List[_5378.AbstractShaftOrHousingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(self)
