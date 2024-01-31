"""SpiralBevelGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpiralBevelGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.modal_analyses import _4685
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4827,
        _4828,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundModalAnalysis")


class SpiralBevelGearSetCompoundModalAnalysis(_4746.BevelGearSetCompoundModalAnalysis):
    """SpiralBevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundModalAnalysis"
    )

    class _Cast_SpiralBevelGearSetCompoundModalAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
            parent: "SpiralBevelGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4746.BevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
        ) -> "SpiralBevelGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

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
    ) -> "List[_4685.SpiralBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis]

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
    def spiral_bevel_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4827.SpiralBevelGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4828.SpiralBevelGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4685.SpiralBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis]

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
    ) -> "SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis":
        return self._Cast_SpiralBevelGearSetCompoundModalAnalysis(self)
