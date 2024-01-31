"""StraightBevelSunGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5503


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundMultibodyDynamicsAnalysis")


class StraightBevelSunGearCompoundMultibodyDynamicsAnalysis(
    _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
):
    """StraightBevelSunGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
            parent: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5503.StraightBevelSunGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelSunGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5503.StraightBevelSunGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelSunGearMultibodyDynamicsAnalysis]

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
    ) -> "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelSunGearCompoundMultibodyDynamicsAnalysis(self)
