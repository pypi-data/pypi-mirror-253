"""CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.system_deflections import _2750


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"
)


class CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation(
    _7057.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
):
    """CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7057.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2750.CylindricalPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
