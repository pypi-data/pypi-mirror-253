"""BoltedJointDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BoltedJointDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.static_loads import _6830


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointDynamicAnalysis",)


Self = TypeVar("Self", bound="BoltedJointDynamicAnalysis")


class BoltedJointDynamicAnalysis(_6376.SpecialisedAssemblyDynamicAnalysis):
    """BoltedJointDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointDynamicAnalysis")

    class _Cast_BoltedJointDynamicAnalysis:
        """Special nested class for casting BoltedJointDynamicAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
            parent: "BoltedJointDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            return self._parent._cast(_6376.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "BoltedJointDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2443.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6830.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis":
        return self._Cast_BoltedJointDynamicAnalysis(self)
