"""StraightBevelDiffGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "StraightBevelDiffGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.modal_analyses import _4690, _4689


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetModalAnalysis")


class StraightBevelDiffGearSetModalAnalysis(_4590.BevelGearSetModalAnalysis):
    """StraightBevelDiffGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetModalAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
            parent: "StraightBevelDiffGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            return self._parent._cast(_4590.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ) -> "StraightBevelDiffGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6962.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2814.StraightBevelDiffGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_modal_analysis(
        self: Self,
    ) -> "List[_4690.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4689.StraightBevelDiffGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis":
        return self._Cast_StraightBevelDiffGearSetModalAnalysis(self)
