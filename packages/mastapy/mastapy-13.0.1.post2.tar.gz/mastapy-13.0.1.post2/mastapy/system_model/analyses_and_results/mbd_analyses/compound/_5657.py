"""ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5522
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5655,
        _5656,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis")


class ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis(
    _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
):
    """ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "List[_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearSetMultibodyDynamicsAnalysis]

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
    def zerol_bevel_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5655.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5656.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearSetMultibodyDynamicsAnalysis]

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
    ) -> "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis(self)
