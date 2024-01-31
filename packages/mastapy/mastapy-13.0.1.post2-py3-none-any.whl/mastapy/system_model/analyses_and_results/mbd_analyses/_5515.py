"""VirtualComponentMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "VirtualComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentMultibodyDynamicsAnalysis")


class VirtualComponentMultibodyDynamicsAnalysis(
    _5464.MountableComponentMultibodyDynamicsAnalysis
):
    """VirtualComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentMultibodyDynamicsAnalysis"
    )

    class _Cast_VirtualComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting VirtualComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
            parent: "VirtualComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(_5459.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(
                _5463.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def point_load_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "VirtualComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis":
        return self._Cast_VirtualComponentMultibodyDynamicsAnalysis(self)
