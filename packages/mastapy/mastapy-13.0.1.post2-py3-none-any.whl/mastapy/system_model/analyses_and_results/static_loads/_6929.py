"""PartLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6898, _6805
from mastapy.system_model.analyses_and_results import _2657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6806
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
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6808

            return self._parent._cast(_6808.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(_6809.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6814

            return self._parent._cast(_6814.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.AssemblyLoadCase)

        @property
        def bearing_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BearingLoadCase)

        @property
        def belt_drive_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BoltedJointLoadCase)

        @property
        def bolt_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BoltLoadCase)

        @property
        def clutch_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ClutchHalfLoadCase)

        @property
        def clutch_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ClutchLoadCase)

        @property
        def component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearSetLoadCase)

        @property
        def connector_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CouplingHalfLoadCase)

        @property
        def coupling_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CouplingLoadCase)

        @property
        def cvt_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.CVTLoadCase)

        @property
        def cvt_pulley_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.DatumLoadCase)

        @property
        def external_cad_model_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6889

            return self._parent._cast(_6889.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.GearLoadCase)

        @property
        def gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6897

            return self._parent._cast(_6897.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6906

            return self._parent._cast(_6906.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(
                _6919.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(
                _6921.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(_6923.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PointLoadLoadCase)

        @property
        def power_load_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PowerLoadLoadCase)

        @property
        def pulley_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PulleyLoadCase)

        @property
        def ring_pins_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.RollingRingLoadCase)

        @property
        def root_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self: "PartLoadCase._Cast_PartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.ZerolBevelGearSetLoadCase)

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
    def harmonic_excitation_type(self: Self, value: "_6898.HarmonicExcitationType"):
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
        self: Self, value: "_6805.StaticLoadCase"
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
