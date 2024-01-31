"""BevelGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5381
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearMultibodyDynamicsAnalysis")


class BevelGearMultibodyDynamicsAnalysis(
    _5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
):
    """BevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMultibodyDynamicsAnalysis")

    class _Cast_BevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
            parent: "BevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(
                _5392.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(
                _5393.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(
                _5502.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(
                _5503.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(_5521.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
        ) -> "BevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearMultibodyDynamicsAnalysis._Cast_BevelGearMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearMultibodyDynamicsAnalysis(self)
