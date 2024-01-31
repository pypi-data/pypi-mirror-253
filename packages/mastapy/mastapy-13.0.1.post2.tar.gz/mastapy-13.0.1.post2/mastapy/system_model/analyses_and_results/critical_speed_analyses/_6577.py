"""ConicalGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCriticalSpeedAnalysis")


class ConicalGearSetCriticalSpeedAnalysis(_6606.GearSetCriticalSpeedAnalysis):
    """ConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCriticalSpeedAnalysis")

    class _Cast_ConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
            parent: "ConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(
                _6549.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BevelGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "ConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis"
    ):
        return self._Cast_ConicalGearSetCriticalSpeedAnalysis(self)
