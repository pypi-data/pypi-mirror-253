"""ConnectionAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionAnalysisCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionAnalysisCase",)


Self = TypeVar("Self", bound="ConnectionAnalysisCase")


class ConnectionAnalysisCase(_2649.ConnectionAnalysis):
    """ConnectionAnalysisCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionAnalysisCase")

    class _Cast_ConnectionAnalysisCase:
        """Special nested class for casting ConnectionAnalysisCase to subclasses."""

        def __init__(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
            parent: "ConnectionAnalysisCase",
        ):
            self._parent = parent

        @property
        def connection_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(
                _2688.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearMeshSystemDeflection)

        @property
        def connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(
                _2736.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(
                _2737.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(
                _2786.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(
                _2805.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearMeshSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(
                _2987.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(
                _3015.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(
                _3020.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3027,
            )

            return self._parent._cast(
                _3027.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(
                _3030.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(
                _3050.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(
                _3067.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(
                _3086.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(_3110.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(
                _3113.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3289,
            )

            return self._parent._cast(
                _3289.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.FaceGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.WormGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(
                _3548.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(
                _3766.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(_3774.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(
                _3808.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(
                _3809.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(
                _3831.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(
                _3845.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(
                _3862.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(
                _4035.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchConnectionPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.CoaxialConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearMeshPowerFlow)

        @property
        def connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(
                _4076.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(
                _4077.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.HypoidGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(
                _4107.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(
                _4134.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.ZerolBevelGearMeshPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4299,
            )

            return self._parent._cast(
                _4299.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(
                _4300.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def belt_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(
                _4307.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ClutchConnectionParametricStudyTool)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.CoaxialConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(
                _4322.ConceptCouplingConnectionParametricStudyTool
            )

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConicalGearMeshParametricStudyTool)

        @property
        def connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConnectionParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.CVTBeltConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(
                _4340.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(
                _4342.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.HypoidGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(
                _4368.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.PartToPartShearCouplingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PlanetaryConnectionParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.RollingRingConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(
                _4411.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(
                _4419.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(
                _4431.TorqueConverterConnectionParametricStudyTool
            )

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.ZerolBevelGearMeshParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(
                _4575.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(
                _4617.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(
                _4619.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(
                _4649.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(
                _4663.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(
                _4681.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.ZerolBevelGearMeshModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4860,
            )

            return self._parent._cast(
                _4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4861,
            )

            return self._parent._cast(
                _4861.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(_4866.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4873,
            )

            return self._parent._cast(_4873.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(
                _4883.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(
                _4901.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(
                _4903.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4904,
            )

            return self._parent._cast(
                _4904.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(_4911.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(_4920.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4923,
            )

            return self._parent._cast(
                _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(
                _4930.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(
                _4939.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(
                _4942.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(
                _4951.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(
                _4956.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4976,
            )

            return self._parent._cast(
                _4976.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(
                _5120.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5121,
            )

            return self._parent._cast(
                _5121.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5126,
            )

            return self._parent._cast(_5126.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(
                _5143.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.ConnectionModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(
                _5161.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(
                _5163.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(_5179.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(
                _5189.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(
                _5198.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(
                _5215.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(
                _5223.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(
                _5235.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(_5387.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(
                _5405.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(
                _5423.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(
                _5456.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(
                _5468.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(
                _5480.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(
                _5490.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(
                _5496.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(
                _5682.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5684,
            )

            return self._parent._cast(_5684.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.ClutchConnectionHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.CoaxialConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ConicalGearMeshHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(
                _5724.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(
                _5726.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.HypoidGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(
                _5789.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PlanetaryConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(_5801.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.RollingRingConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(
                _5808.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6013,
            )

            return self._parent._cast(
                _6013.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6017,
            )

            return self._parent._cast(
                _6017.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(
                _6020.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6025,
            )

            return self._parent._cast(
                _6025.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(
                _6041.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(_6067.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(
                _6093.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(
                _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(
                _6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(
                _6323.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(
                _6359.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6546,
            )

            return self._parent._cast(
                _6546.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6548,
            )

            return self._parent._cast(
                _6548.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def belt_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(_6552.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(
                _6555.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(
                _6569.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConnectionCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(
                _6590.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(
                _6592.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(
                _6616.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(
                _6626.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(
                _6636.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(
                _6643.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(
                _6652.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(
                _6663.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6673,
            )

            return self._parent._cast(_6673.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7009,
            )

            return self._parent._cast(
                _7009.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7015,
            )

            return self._parent._cast(
                _7015.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7075,
            )

            return self._parent._cast(
                _7075.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7105,
            )

            return self._parent._cast(
                _7105.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(
                _7273.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(
                _7278.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(_7282.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ClutchConnectionAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(
                _7300.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(
                _7319.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(
                _7320.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase",
        ) -> "ConnectionAnalysisCase":
            return self._parent

        def __getattr__(
            self: "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConnectionAnalysisCase._Cast_ConnectionAnalysisCase":
        return self._Cast_ConnectionAnalysisCase(self)
