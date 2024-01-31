"""ConceptCouplingModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConceptCouplingModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.system_deflections import _2719


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingModalAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingModalAnalysis")


class ConceptCouplingModalAnalysis(_4611.CouplingModalAnalysis):
    """ConceptCouplingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingModalAnalysis")

    class _Cast_ConceptCouplingModalAnalysis:
        """Special nested class for casting ConceptCouplingModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
            parent: "ConceptCouplingModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            return self._parent._cast(_4611.CouplingModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4571

            return self._parent._cast(_4571.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
        ) -> "ConceptCouplingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6840.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

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
    ) -> "_2719.ConceptCouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection

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
    ) -> "ConceptCouplingModalAnalysis._Cast_ConceptCouplingModalAnalysis":
        return self._Cast_ConceptCouplingModalAnalysis(self)
