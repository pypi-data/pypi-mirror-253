"""ZerolBevelGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6693,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6674
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6801,
        _6802,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundCriticalSpeedAnalysis")


class ZerolBevelGearSetCompoundCriticalSpeedAnalysis(
    _6693.BevelGearSetCompoundCriticalSpeedAnalysis
):
    """ZerolBevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ZerolBevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6693.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

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
    ) -> "List[_6674.ZerolBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ZerolBevelGearSetCriticalSpeedAnalysis]

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
    def zerol_bevel_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6801.ZerolBevelGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ZerolBevelGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6802.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6674.ZerolBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ZerolBevelGearSetCriticalSpeedAnalysis]

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
    ) -> "ZerolBevelGearSetCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_ZerolBevelGearSetCompoundCriticalSpeedAnalysis(self)
