"""VirtualComponentCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "VirtualComponentCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5515


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundMultibodyDynamicsAnalysis")


class VirtualComponentCompoundMultibodyDynamicsAnalysis(
    _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """VirtualComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting VirtualComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
            parent: "VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "VirtualComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "VirtualComponentCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5515.VirtualComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.VirtualComponentMultibodyDynamicsAnalysis]

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
    ) -> "List[_5515.VirtualComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.VirtualComponentMultibodyDynamicsAnalysis]

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
    ) -> "VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis":
        return self._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis(self)
