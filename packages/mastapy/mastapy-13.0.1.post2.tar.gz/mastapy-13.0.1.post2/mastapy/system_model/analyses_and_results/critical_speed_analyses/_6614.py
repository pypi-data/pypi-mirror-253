"""KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
    _6577.ConicalGearSetCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6577.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
            self
        )
