"""CouplingHalfCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4805
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4611


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysis")


class CouplingHalfCompoundModalAnalysis(_4805.MountableComponentCompoundModalAnalysis):
    """CouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysis")

    class _Cast_CouplingHalfCompoundModalAnalysis:
        """Special nested class for casting CouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
            parent: "CouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.CVTPulleyCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.PulleyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.RollingRingCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.SpringDamperHalfCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "CouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4611.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4611.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis":
        return self._Cast_CouplingHalfCompoundModalAnalysis(self)
