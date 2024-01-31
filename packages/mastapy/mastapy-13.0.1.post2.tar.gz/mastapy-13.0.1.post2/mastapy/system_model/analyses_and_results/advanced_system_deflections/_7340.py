"""InterMountableComponentConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionAdvancedSystemDeflection"
)


class InterMountableComponentConnectionAdvancedSystemDeflection(
    _7308.ConnectionAdvancedSystemDeflection
):
    """InterMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(
                _7278.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(_7282.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(
                _7300.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2281.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
