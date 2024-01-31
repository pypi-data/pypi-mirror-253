"""ConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundHarmonicAnalysis")


class ConnectionCompoundHarmonicAnalysis(_7539.ConnectionCompoundAnalysis):
    """ConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundHarmonicAnalysis")

    class _Cast_ConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
            parent: "ConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(
                _5884.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(_5888.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(
                _5906.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(
                _5923.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(
                _5925.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(
                _5960.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(
                _5972.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(
                _5976.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(
                _5997.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "ConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5715.ConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis]

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
    ) -> "List[_5715.ConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis]

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
    ) -> "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis":
        return self._Cast_ConnectionCompoundHarmonicAnalysis(self)
