"""WormGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "WormGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3893,
        _3891,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="WormGearSetStabilityAnalysis")


class WormGearSetStabilityAnalysis(_3824.GearSetStabilityAnalysis):
    """WormGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetStabilityAnalysis")

    class _Cast_WormGearSetStabilityAnalysis:
        """Special nested class for casting WormGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
            parent: "WormGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3824.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "WormGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2552.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6984.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears_stability_analysis(
        self: Self,
    ) -> "List[_3893.WormGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3891.WormGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis":
        return self._Cast_WormGearSetStabilityAnalysis(self)
