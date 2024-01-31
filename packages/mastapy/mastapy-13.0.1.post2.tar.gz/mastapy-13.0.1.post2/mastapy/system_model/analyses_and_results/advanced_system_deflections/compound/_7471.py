"""InterMountableComponentConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7441,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7340,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundAdvancedSystemDeflection"
)


class InterMountableComponentConnectionCompoundAdvancedSystemDeflection(
    _7441.ConnectionCompoundAdvancedSystemDeflection
):
    """InterMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(
                _7444.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(
                _7446.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(
                _7487.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7340.InterMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.InterMountableComponentConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7340.InterMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.InterMountableComponentConnectionAdvancedSystemDeflection]

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
    ) -> "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection(
            self
        )
