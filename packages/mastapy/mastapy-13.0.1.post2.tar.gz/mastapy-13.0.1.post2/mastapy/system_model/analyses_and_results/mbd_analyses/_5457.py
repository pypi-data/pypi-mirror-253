"""KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import _6919


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis(
    _5451.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6919.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis(
                self
            )
        )
