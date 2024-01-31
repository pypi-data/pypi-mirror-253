"""CouplingHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfMultibodyDynamicsAnalysis")


class CouplingHalfMultibodyDynamicsAnalysis(
    _5464.MountableComponentMultibodyDynamicsAnalysis
):
    """CouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
            parent: "CouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(
                _5406.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(
                _5469.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(_5476.PulleyMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(_5481.RollingRingMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(_5494.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfMultibodyDynamicsAnalysis(self)
