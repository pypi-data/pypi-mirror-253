"""KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.modal_analyses import _4648
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4797,
        _4798,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis(
    _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4797.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4798.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis(
            self
        )
