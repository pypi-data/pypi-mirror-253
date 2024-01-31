"""Database"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "Database")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1826


__docformat__ = "restructuredtext en"
__all__ = ("Database",)


Self = TypeVar("Self", bound="Database")
TKey = TypeVar("TKey", bound="_1826.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")


class Database(_0.APIBase, Generic[TKey, TValue]):
    """Database

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Database")

    class _Cast_Database:
        """Special nested class for casting Database to subclasses."""

        def __init__(self: "Database._Cast_Database", parent: "Database"):
            self._parent = parent

        @property
        def shaft_material_database(self: "Database._Cast_Database"):
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(self: "Database._Cast_Database"):
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(self: "Database._Cast_Database"):
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(self: "Database._Cast_Database"):
            from mastapy.materials import _246

            return self._parent._cast(_246.BearingMaterialDatabase)

        @property
        def component_material_database(self: "Database._Cast_Database"):
            from mastapy.materials import _249

            return self._parent._cast(_249.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(self: "Database._Cast_Database"):
            from mastapy.materials import _268

            return self._parent._cast(_268.LubricationDetailDatabase)

        @property
        def material_database(self: "Database._Cast_Database"):
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialDatabase)

        @property
        def materials_settings_database(self: "Database._Cast_Database"):
            from mastapy.materials import _272

            return self._parent._cast(_272.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(self: "Database._Cast_Database"):
            from mastapy.gears import _343

            return self._parent._cast(_343.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.rating.cylindrical import _453

            return self._parent._cast(
                _453.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.rating.cylindrical import _469

            return self._parent._cast(_469.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _584

            return self._parent._cast(_584.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.materials import _599

            return self._parent._cast(
                _599.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(self: "Database._Cast_Database"):
            from mastapy.gears.materials import _607

            return self._parent._cast(_607.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical import _610

            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705

            return self._parent._cast(_705.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(self: "Database._Cast_Database"):
            from mastapy.gears.manufacturing.bevel import _800

            return self._parent._cast(_800.ManufacturingMachineDatabase)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _920

            return self._parent._cast(
                _920.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _923

            return self._parent._cast(
                _923.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(_929.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(
                _933.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(self: "Database._Cast_Database"):
            from mastapy.gears.gear_designs import _940

            return self._parent._cast(_940.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(self: "Database._Cast_Database"):
            from mastapy.gears.gear_designs import _942

            return self._parent._cast(_942.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(self: "Database._Cast_Database"):
            from mastapy.gears.gear_designs import _945

            return self._parent._cast(_945.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1015

            return self._parent._cast(_1015.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1021

            return self._parent._cast(
                _1021.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(self: "Database._Cast_Database"):
            from mastapy.electric_machines import _1283

            return self._parent._cast(_1283.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self: "Database._Cast_Database"):
            from mastapy.electric_machines import _1301

            return self._parent._cast(_1301.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self: "Database._Cast_Database"):
            from mastapy.electric_machines import _1314

            return self._parent._cast(_1314.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self: "Database._Cast_Database"):
            from mastapy.cycloidal import _1456

            return self._parent._cast(_1456.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self: "Database._Cast_Database"):
            from mastapy.cycloidal import _1463

            return self._parent._cast(_1463.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(self: "Database._Cast_Database"):
            from mastapy.bolts import _1466

            return self._parent._cast(_1466.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(self: "Database._Cast_Database"):
            from mastapy.bolts import _1468

            return self._parent._cast(_1468.BoltGeometryDatabase)

        @property
        def bolt_material_database(self: "Database._Cast_Database"):
            from mastapy.bolts import _1470

            return self._parent._cast(_1470.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self: "Database._Cast_Database"):
            from mastapy.bolts import _1475

            return self._parent._cast(_1475.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(self: "Database._Cast_Database"):
            from mastapy.math_utility.optimisation import _1539

            return self._parent._cast(_1539.DesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.math_utility.optimisation import _1541

            return self._parent._cast(
                _1541.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(self: "Database._Cast_Database"):
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(self: "Database._Cast_Database"):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(self: "Database._Cast_Database"):
            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def bearing_settings_database(self: "Database._Cast_Database"):
            from mastapy.bearings import _1880

            return self._parent._cast(_1880.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(self: "Database._Cast_Database"):
            from mastapy.bearings import _1893

            return self._parent._cast(_1893.RollingBearingDatabase)

        @property
        def iso14179_settings_database(self: "Database._Cast_Database"):
            from mastapy.bearings.bearing_results.rolling import _1975

            return self._parent._cast(_1975.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "Database._Cast_Database",
        ):
            from mastapy.system_model.optimization import _2228

            return self._parent._cast(_2228.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(self: "Database._Cast_Database"):
            from mastapy.system_model.optimization import _2236

            return self._parent._cast(_2236.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(self: "Database._Cast_Database"):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2564,
            )

            return self._parent._cast(_2564.SuperchargerRotorSetDatabase)

        @property
        def database(self: "Database._Cast_Database") -> "Database":
            return self._parent

        def __getattr__(self: "Database._Cast_Database", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Database.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def count(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    @enforce_parameter_types
    def can_be_removed(self: Self, item: "TValue") -> "bool":
        """bool

        Args:
            item (TValue)
        """
        method_result = self.wrapped.CanBeRemoved(item)
        return method_result

    def get_all_items(self: Self) -> "List[TValue]":
        """List[TValue]"""
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetAllItems())

    @property
    def cast_to(self: Self) -> "Database._Cast_Database":
        return self._Cast_Database(self)
