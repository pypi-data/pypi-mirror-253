"""TorqueConverterTurbineMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterTurbineMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6975


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineMultibodyDynamicsAnalysis")


class TorqueConverterTurbineMultibodyDynamicsAnalysis(
    _5416.CouplingHalfMultibodyDynamicsAnalysis
):
    """TorqueConverterTurbineMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterTurbineMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
            parent: "TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5416.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterTurbineMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "TorqueConverterTurbineMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6975.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterTurbineMultibodyDynamicsAnalysis(self)
