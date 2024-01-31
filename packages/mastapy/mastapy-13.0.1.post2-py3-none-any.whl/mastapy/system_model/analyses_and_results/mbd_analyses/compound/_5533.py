"""AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5381


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(
    _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(self)
