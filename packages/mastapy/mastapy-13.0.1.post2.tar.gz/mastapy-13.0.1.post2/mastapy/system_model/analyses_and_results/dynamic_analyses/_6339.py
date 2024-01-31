"""GearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="GearSetDynamicAnalysis")


class GearSetDynamicAnalysis(_6377.SpecialisedAssemblyDynamicAnalysis):
    """GearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDynamicAnalysis")

    class _Cast_GearSetDynamicAnalysis:
        """Special nested class for casting GearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
            parent: "GearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearSetDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearSetDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PlanetaryGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearSetDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "GearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2532.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis":
        return self._Cast_GearSetDynamicAnalysis(self)
