"""ConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConnectionPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.power_flows import _4122
    from mastapy.system_model.analyses_and_results.system_deflections import _2727


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionPowerFlow",)


Self = TypeVar("Self", bound="ConnectionPowerFlow")


class ConnectionPowerFlow(_7541.ConnectionStaticLoadAnalysisCase):
    """ConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionPowerFlow")

    class _Cast_ConnectionPowerFlow:
        """Special nested class for casting ConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
            parent: "ConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(
                _4035.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchConnectionPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.CoaxialConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearMeshPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(
                _4076.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(
                _4077.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.HypoidGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(
                _4107.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(
                _4134.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.ZerolBevelGearMeshPowerFlow)

        @property
        def connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "ConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2272.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2272.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4122.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def torsional_system_deflection_analysis(
        self: Self,
    ) -> "_2727.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalSystemDeflectionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionPowerFlow._Cast_ConnectionPowerFlow":
        return self._Cast_ConnectionPowerFlow(self)
