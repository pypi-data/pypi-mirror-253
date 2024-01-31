"""AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5382


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis"
)


class AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis(
    _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(
                _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5382.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis]

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
    ) -> "List[_5382.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis(
            self
        )
