"""KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4891,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness(
    _4891.ConicalGearSetModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4891.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(
                _4929.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness(
                self
            )
        )
