"""StraightBevelGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundDynamicAnalysis")


class StraightBevelGearCompoundDynamicAnalysis(_6424.BevelGearCompoundDynamicAnalysis):
    """StraightBevelGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearCompoundDynamicAnalysis"
    )

    class _Cast_StraightBevelGearCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
            parent: "StraightBevelGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
        ) -> "StraightBevelGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6387.StraightBevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6387.StraightBevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearCompoundDynamicAnalysis._Cast_StraightBevelGearCompoundDynamicAnalysis":
        return self._Cast_StraightBevelGearCompoundDynamicAnalysis(self)
