"""PlanetaryGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PlanetaryGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetDynamicAnalysis")


class PlanetaryGearSetDynamicAnalysis(_6325.CylindricalGearSetDynamicAnalysis):
    """PlanetaryGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetDynamicAnalysis")

    class _Cast_PlanetaryGearSetDynamicAnalysis:
        """Special nested class for casting PlanetaryGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
            parent: "PlanetaryGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6325.CylindricalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
        ) -> "PlanetaryGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis":
        return self._Cast_PlanetaryGearSetDynamicAnalysis(self)
