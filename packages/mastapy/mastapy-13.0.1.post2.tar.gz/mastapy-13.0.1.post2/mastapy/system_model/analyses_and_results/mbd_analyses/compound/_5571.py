"""CVTPulleyCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CVTPulleyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5421


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundMultibodyDynamicsAnalysis")


class CVTPulleyCompoundMultibodyDynamicsAnalysis(
    _5617.PulleyCompoundMultibodyDynamicsAnalysis
):
    """CVTPulleyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTPulleyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
            parent: "CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5617.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
        ) -> "CVTPulleyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5421.CVTPulleyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTPulleyMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5421.CVTPulleyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTPulleyMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis(self)
