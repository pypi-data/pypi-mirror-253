"""KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6618,
        _6619,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis(
    _6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6921.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6618.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCriticalSpeedAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6619.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCriticalSpeedAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis(
                self
            )
        )
