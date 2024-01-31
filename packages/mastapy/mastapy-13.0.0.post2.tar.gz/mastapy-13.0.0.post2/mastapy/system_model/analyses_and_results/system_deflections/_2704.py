"""BevelDifferentialPlanetGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialPlanetGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.power_flows import _4046


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearSystemDeflection")


class BevelDifferentialPlanetGearSystemDeflection(
    _2703.BevelDifferentialGearSystemDeflection
):
    """BevelDifferentialPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearSystemDeflection"
    )

    class _Cast_BevelDifferentialPlanetGearSystemDeflection:
        """Special nested class for casting BevelDifferentialPlanetGearSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
            parent: "BevelDifferentialPlanetGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            return self._parent._cast(_2703.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2691,
            )

            return self._parent._cast(_2691.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
        ) -> "BevelDifferentialPlanetGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4046.BevelDifferentialPlanetGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection":
        return self._Cast_BevelDifferentialPlanetGearSystemDeflection(self)
