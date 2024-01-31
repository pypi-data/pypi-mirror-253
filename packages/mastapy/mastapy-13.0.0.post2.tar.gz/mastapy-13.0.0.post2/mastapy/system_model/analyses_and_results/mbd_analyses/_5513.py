"""UnbalancedMassMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "UnbalancedMassMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.static_loads import _6980


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassMultibodyDynamicsAnalysis")


class UnbalancedMassMultibodyDynamicsAnalysis(
    _5514.VirtualComponentMultibodyDynamicsAnalysis
):
    """UnbalancedMassMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassMultibodyDynamicsAnalysis"
    )

    class _Cast_UnbalancedMassMultibodyDynamicsAnalysis:
        """Special nested class for casting UnbalancedMassMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
            parent: "UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5514.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
        ) -> "UnbalancedMassMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6980.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[UnbalancedMassMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.UnbalancedMassMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassMultibodyDynamicsAnalysis._Cast_UnbalancedMassMultibodyDynamicsAnalysis":
        return self._Cast_UnbalancedMassMultibodyDynamicsAnalysis(self)
