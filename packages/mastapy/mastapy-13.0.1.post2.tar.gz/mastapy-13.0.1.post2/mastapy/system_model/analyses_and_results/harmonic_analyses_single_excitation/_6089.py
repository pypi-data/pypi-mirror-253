"""PartHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PartHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5766
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6070,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4662


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PartHarmonicAnalysisOfSingleExcitation")


class PartHarmonicAnalysisOfSingleExcitation(_7548.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
            parent: "PartHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6009,
            )

            return self._parent._cast(
                _6009.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(_6015.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(_6016.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(_6018.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(_6024.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(_6028.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(
                _6030.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(_6031.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(_6084.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(
                _6094.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(_6098.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(_6099.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(_6105.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(_6133.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "PartHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "PartHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2468.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5766.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "_6070.HarmonicAnalysisOfSingleExcitation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def uncoupled_modal_analysis(self: Self) -> "_4662.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartHarmonicAnalysisOfSingleExcitation(self)
