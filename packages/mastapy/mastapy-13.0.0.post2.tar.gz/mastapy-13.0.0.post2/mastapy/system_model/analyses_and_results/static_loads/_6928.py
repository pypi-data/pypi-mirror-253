"""PartLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6897, _6804
from mastapy.system_model.analyses_and_results import _2657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6805
    from mastapy.electric_machines.harmonic_load_data import _1379


__docformat__ = "restructuredtext en"
__all__ = ("PartLoadCase",)


Self = TypeVar("Self", bound="PartLoadCase")


class PartLoadCase(_2657.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartLoadCase")

    class _Cast_PartLoadCase:
        """Special nested class for casting PartLoadCase to subclasses."""

        def __init__(self: "PartLoadCase._Cast_PartLoadCase", parent: "PartLoadCase"):
            self._parent = parent

        @property
        def part_analysis(self: "PartLoadCase._Cast_PartLoadCase"):
            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6808

            return self._parent._cast(_6808.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.AssemblyLoadCase)

        @property
        def bearing_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BearingLoadCase)

        @property
        def belt_drive_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BoltedJointLoadCase)

        @property
        def bolt_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BoltLoadCase)

        @property
        def clutch_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.ClutchHalfLoadCase)

        @property
        def clutch_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ClutchLoadCase)

        @property
        def component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConicalGearSetLoadCase)

        @property
        def connector_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.CouplingHalfLoadCase)

        @property
        def coupling_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CouplingLoadCase)

        @property
        def cvt_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CVTLoadCase)

        @property
        def cvt_pulley_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6869

            return self._parent._cast(_6869.DatumLoadCase)

        @property
        def external_cad_model_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(
                _6920.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(_6935.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PointLoadLoadCase)

        @property
        def power_load_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PowerLoadLoadCase)

        @property
        def pulley_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PulleyLoadCase)

        @property
        def ring_pins_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.RollingRingLoadCase)

        @property
        def root_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.ZerolBevelGearSetLoadCase)

        @property
        def part_load_case(self: "PartLoadCase._Cast_PartLoadCase") -> "PartLoadCase":
            return self._parent

        def __getattr__(self: "PartLoadCase._Cast_PartLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]"""
        temp = self.wrapped.HarmonicExcitationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @harmonic_excitation_type.setter
    @enforce_parameter_types
    def harmonic_excitation_type(self: Self, value: "_6897.HarmonicExcitationType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HarmonicExcitationType = value

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = (
            self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "_6804.StaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            value
        )

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "bool"
    ):
        self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            bool(value) if value is not None else False
        )

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
    def static_load_case(self: Self) -> "_6804.StaticLoadCase":
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
    def time_series_load_case(self: Self) -> "_6805.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_this_load_case(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForThisLoadCase()

    def get_harmonic_load_data_for_import(self: Self) -> "_1379.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartLoadCase._Cast_PartLoadCase":
        return self._Cast_PartLoadCase(self)
