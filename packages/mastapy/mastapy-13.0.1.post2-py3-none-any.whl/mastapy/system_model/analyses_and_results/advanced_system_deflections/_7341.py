"""KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection(
    _7305.ConicalGearAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7305.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(
                _7347.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection(
            self
        )
