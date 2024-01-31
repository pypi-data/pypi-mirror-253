"""ConnectionFEAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "ConnectionFEAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionFEAnalysis",)


Self = TypeVar("Self", bound="ConnectionFEAnalysis")


class ConnectionFEAnalysis(_7541.ConnectionStaticLoadAnalysisCase):
    """ConnectionFEAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionFEAnalysis")

    class _Cast_ConnectionFEAnalysis:
        """Special nested class for casting ConnectionFEAnalysis to subclasses."""

        def __init__(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
            parent: "ConnectionFEAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(
                _2688.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearMeshSystemDeflection)

        @property
        def connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(
                _2736.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(
                _2737.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(
                _2786.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(
                _2805.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearMeshSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(
                _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(
                _6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(
                _6323.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(
                _6359.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis",
        ) -> "ConnectionFEAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConnectionFEAnalysis._Cast_ConnectionFEAnalysis":
        return self._Cast_ConnectionFEAnalysis(self)
