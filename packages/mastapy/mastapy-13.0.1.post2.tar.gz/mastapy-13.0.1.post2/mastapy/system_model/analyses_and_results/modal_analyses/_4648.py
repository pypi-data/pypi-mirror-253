"""KlingelnbergCycloPalloidHypoidGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4645
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2772
    from mastapy.system_model.analyses_and_results.modal_analyses import _4647, _4646


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetModalAnalysis")


class KlingelnbergCycloPalloidHypoidGearSetModalAnalysis(
    _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

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
    ) -> "_2772.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_modal_analysis(
        self: Self,
    ) -> "List[_4647.KlingelnbergCycloPalloidHypoidGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4646.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetModalAnalysis(self)
