"""PlanetCarrierCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PlanetCarrierCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5473


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundMultibodyDynamicsAnalysis")


class PlanetCarrierCompoundMultibodyDynamicsAnalysis(
    _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """PlanetCarrierCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetCarrierCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
            parent: "PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
        ) -> "PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PlanetCarrierCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5473.PlanetCarrierMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetCarrierMultibodyDynamicsAnalysis]

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
    ) -> "List[_5473.PlanetCarrierMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetCarrierMultibodyDynamicsAnalysis]

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
    ) -> "PlanetCarrierCompoundMultibodyDynamicsAnalysis._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PlanetCarrierCompoundMultibodyDynamicsAnalysis(self)
