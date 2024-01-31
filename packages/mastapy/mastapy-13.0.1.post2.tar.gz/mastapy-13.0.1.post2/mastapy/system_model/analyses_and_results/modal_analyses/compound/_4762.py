"""ConicalGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConicalGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4606


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundModalAnalysis")


class ConicalGearSetCompoundModalAnalysis(_4788.GearSetCompoundModalAnalysis):
    """ConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCompoundModalAnalysis")

    class _Cast_ConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting ConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
            parent: "ConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
        ) -> "ConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4606.ConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4606.ConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearSetCompoundModalAnalysis._Cast_ConicalGearSetCompoundModalAnalysis"
    ):
        return self._Cast_ConicalGearSetCompoundModalAnalysis(self)
