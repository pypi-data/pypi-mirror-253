"""CylindricalPlanetGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CylindricalPlanetGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearDynamicAnalysis")


class CylindricalPlanetGearDynamicAnalysis(_6323.CylindricalGearDynamicAnalysis):
    """CylindricalPlanetGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearDynamicAnalysis")

    class _Cast_CylindricalPlanetGearDynamicAnalysis:
        """Special nested class for casting CylindricalPlanetGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
            parent: "CylindricalPlanetGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            return self._parent._cast(_6323.CylindricalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "CylindricalPlanetGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearDynamicAnalysis.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis":
        return self._Cast_CylindricalPlanetGearDynamicAnalysis(self)
