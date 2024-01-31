"""ZerolBevelGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5521


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundMultibodyDynamicsAnalysis")


class ZerolBevelGearCompoundMultibodyDynamicsAnalysis(
    _5545.BevelGearCompoundMultibodyDynamicsAnalysis
):
    """ZerolBevelGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ZerolBevelGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
            parent: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ZerolBevelGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_5521.ZerolBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5521.ZerolBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMultibodyDynamicsAnalysis]

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
    ) -> "ZerolBevelGearCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ZerolBevelGearCompoundMultibodyDynamicsAnalysis(self)
