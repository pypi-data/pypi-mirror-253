"""ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7046,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7539.ConnectionCompoundAnalysis
):
    """ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7144,
            )

            return self._parent._cast(
                _7144.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7146,
            )

            return self._parent._cast(
                _7146.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7187,
            )

            return self._parent._cast(
                _7187.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7046.ConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7046.ConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
