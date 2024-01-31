"""ConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6043,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConnectionCompoundHarmonicAnalysisOfSingleExcitation")


class ConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _7539.ConnectionCompoundAnalysis
):
    """ConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6142,
            )

            return self._parent._cast(
                _6142.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6144,
            )

            return self._parent._cast(
                _6144.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6156,
            )

            return self._parent._cast(
                _6156.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6187,
            )

            return self._parent._cast(
                _6187.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6043.ConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6043.ConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConnectionCompoundHarmonicAnalysisOfSingleExcitation(self)
