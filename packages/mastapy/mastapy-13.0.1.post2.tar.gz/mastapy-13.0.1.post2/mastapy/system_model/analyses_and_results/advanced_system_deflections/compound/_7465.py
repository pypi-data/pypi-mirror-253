"""GearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7471,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "GearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7334,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GearMeshCompoundAdvancedSystemDeflection")


class GearMeshCompoundAdvancedSystemDeflection(
    _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """GearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_GearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting GearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
            parent: "GearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
        ) -> "GearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "GearMeshCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_separation_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7334.GearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7334.GearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_GearMeshCompoundAdvancedSystemDeflection(self)
