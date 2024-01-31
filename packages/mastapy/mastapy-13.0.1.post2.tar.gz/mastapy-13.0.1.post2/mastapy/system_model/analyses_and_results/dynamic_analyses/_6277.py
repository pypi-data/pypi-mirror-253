"""AbstractAssemblyDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyDynamicAnalysis")


class AbstractAssemblyDynamicAnalysis(_6358.PartDynamicAnalysis):
    """AbstractAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyDynamicAnalysis")

    class _Cast_AbstractAssemblyDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            parent: "AbstractAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.AssemblyDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RollingRingAssemblyDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.RootAssemblyDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "AbstractAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis":
        return self._Cast_AbstractAssemblyDynamicAnalysis(self)
