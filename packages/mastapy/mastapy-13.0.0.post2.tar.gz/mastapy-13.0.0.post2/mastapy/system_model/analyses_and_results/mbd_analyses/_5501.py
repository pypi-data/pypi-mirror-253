"""StraightBevelPlanetGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5496
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelPlanetGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearMultibodyDynamicsAnalysis")


class StraightBevelPlanetGearMultibodyDynamicsAnalysis(
    _5496.StraightBevelDiffGearMultibodyDynamicsAnalysis
):
    """StraightBevelPlanetGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelPlanetGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
            parent: "StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5496.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
        ) -> "StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelPlanetGearMultibodyDynamicsAnalysis(self)
