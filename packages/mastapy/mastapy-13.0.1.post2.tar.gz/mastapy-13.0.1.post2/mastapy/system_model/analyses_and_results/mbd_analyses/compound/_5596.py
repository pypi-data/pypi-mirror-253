"""KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5450


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis(
    _5562.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5562.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(_5564.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis(
            self
        )
