"""BevelGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.system_deflections import _2708


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearModalAnalysis")


class BevelGearModalAnalysis(_4577.AGMAGleasonConicalGearModalAnalysis):
    """BevelGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearModalAnalysis")

    class _Cast_BevelGearModalAnalysis:
        """Special nested class for casting BevelGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
            parent: "BevelGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            return self._parent._cast(_4577.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialSunGearModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelSunGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.ZerolBevelGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "BevelGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2708.BevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis":
        return self._Cast_BevelGearModalAnalysis(self)
