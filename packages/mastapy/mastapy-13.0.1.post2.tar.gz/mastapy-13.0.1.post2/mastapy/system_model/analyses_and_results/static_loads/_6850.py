"""ConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.static_loads import _6805, _6806


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionLoadCase",)


Self = TypeVar("Self", bound="ConnectionLoadCase")


class ConnectionLoadCase(_2649.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionLoadCase")

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
            parent: "ConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_analysis(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6810

            return self._parent._cast(
                _6810.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(
                _6859.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(
                _6861.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(
                _6920.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "ConnectionLoadCase":
            return self._parent

        def __getattr__(self: "ConnectionLoadCase._Cast_ConnectionLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def static_load_case(self: Self) -> "_6805.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6806.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionLoadCase._Cast_ConnectionLoadCase":
        return self._Cast_ConnectionLoadCase(self)
