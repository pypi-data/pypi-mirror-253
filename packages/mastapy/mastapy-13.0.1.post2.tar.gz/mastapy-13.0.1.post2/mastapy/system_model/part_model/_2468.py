"""Part"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")

if TYPE_CHECKING:
    from mastapy.math_utility import _1517
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.part_model import _2433
    from mastapy.system_model.import_export import _2242


__docformat__ = "restructuredtext en"
__all__ = ("Part",)


Self = TypeVar("Self", bound="Part")


class Part(_2203.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE = _PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Part")

    class _Cast_Part:
        """Special nested class for casting Part to subclasses."""

        def __init__(self: "Part._Cast_Part", parent: "Part"):
            self._parent = parent

        @property
        def design_entity(self: "Part._Cast_Part"):
            return self._parent._cast(_2203.DesignEntity)

        @property
        def assembly(self: "Part._Cast_Part"):
            return self._parent._cast(_2433.Assembly)

        @property
        def abstract_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def abstract_shaft(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2435

            return self._parent._cast(_2435.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2436

            return self._parent._cast(_2436.AbstractShaftOrHousing)

        @property
        def bearing(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2439

            return self._parent._cast(_2439.Bearing)

        @property
        def bolt(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.Bolt)

        @property
        def bolted_joint(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.BoltedJoint)

        @property
        def component(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def connector(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2447

            return self._parent._cast(_2447.Connector)

        @property
        def datum(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2448

            return self._parent._cast(_2448.Datum)

        @property
        def external_cad_model(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.ExternalCADModel)

        @property
        def fe_part(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.FEPart)

        @property
        def flexible_pin_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.GuideDxfModel)

        @property
        def mass_disc(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MassDisc)

        @property
        def measurement_component(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.MeasurementComponent)

        @property
        def mountable_component(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def oil_seal(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.OilSeal)

        @property
        def planet_carrier(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PlanetCarrier)

        @property
        def point_load(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.PointLoad)

        @property
        def power_load(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.PowerLoad)

        @property
        def root_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.RootAssembly)

        @property
        def specialised_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2477

            return self._parent._cast(_2477.UnbalancedMass)

        @property
        def virtual_component(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.VirtualComponent)

        @property
        def shaft(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.shaft_model import _2482

            return self._parent._cast(_2482.Shaft)

        @property
        def agma_gleason_conical_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def bevel_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.BevelGearSet)

        @property
        def concept_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConceptGear)

        @property
        def concept_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConceptGearSet)

        @property
        def conical_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConicalGear)

        @property
        def conical_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.ConicalGearSet)

        @property
        def cylindrical_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.CylindricalPlanetGear)

        @property
        def face_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.FaceGear)

        @property
        def face_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.FaceGearSet)

        @property
        def gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.GearSet)

        @property
        def hypoid_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.HypoidGear)

        @property
        def hypoid_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def worm_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.WormGear)

        @property
        def worm_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.WormGearSet)

        @property
        def zerol_bevel_gear(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.cycloidal import _2568

            return self._parent._cast(_2568.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.cycloidal import _2569

            return self._parent._cast(_2569.CycloidalDisc)

        @property
        def ring_pins(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.cycloidal import _2570

            return self._parent._cast(_2570.RingPins)

        @property
        def belt_drive(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.BeltDrive)

        @property
        def clutch(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2578

            return self._parent._cast(_2578.Clutch)

        @property
        def clutch_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ClutchHalf)

        @property
        def concept_coupling(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.ConceptCoupling)

        @property
        def concept_coupling_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2582

            return self._parent._cast(_2582.ConceptCouplingHalf)

        @property
        def coupling(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.Coupling)

        @property
        def coupling_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CouplingHalf)

        @property
        def cvt(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.CVT)

        @property
        def cvt_pulley(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.CVTPulley)

        @property
        def part_to_part_shear_coupling(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2590

            return self._parent._cast(_2590.Pulley)

        @property
        def rolling_ring(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.RollingRing)

        @property
        def rolling_ring_assembly(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.ShaftHubConnection)

        @property
        def spring_damper(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.SpringDamper)

        @property
        def spring_damper_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.SpringDamperHalf)

        @property
        def synchroniser(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.Synchroniser)

        @property
        def synchroniser_half(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserHalf)

        @property
        def synchroniser_part(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserSleeve)

        @property
        def torque_converter(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.TorqueConverter)

        @property
        def torque_converter_pump(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.TorqueConverterPump)

        @property
        def torque_converter_turbine(self: "Part._Cast_Part"):
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.TorqueConverterTurbine)

        @property
        def part(self: "Part._Cast_Part") -> "Part":
            return self._parent

        def __getattr__(self: "Part._Cast_Part", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Part.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_full_model(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingFullModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_isometric_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def drawing_number(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DrawingNumber

        if temp is None:
            return ""

        return temp

    @drawing_number.setter
    @enforce_parameter_types
    def drawing_number(self: Self, value: "str"):
        self.wrapped.DrawingNumber = str(value) if value is not None else ""

    @property
    def editable_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditableName

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: Self, value: "str"):
        self.wrapped.EditableName = str(value) if value is not None else ""

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def mass_properties_from_design(self: Self) -> "_1517.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_design_including_planetary_duplicates(
        self: Self,
    ) -> "_1517.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesignIncludingPlanetaryDuplicates

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connections(self: Self) -> "List[_2272.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def local_connections(self: Self) -> "List[_2272.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def connections_to(self: Self, part: "Part") -> "List[_2272.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Args:
            part (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ConnectionsTo(part.wrapped if part else None)
        )

    @enforce_parameter_types
    def copy_to(self: Self, container: "_2433.Assembly") -> "Part":
        """mastapy.system_model.part_model.Part

        Args:
            container (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.CopyTo(container.wrapped if container else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_geometry_export_options(self: Self) -> "_2242.GeometryExportOptions":
        """mastapy.system_model.import_export.GeometryExportOptions"""
        method_result = self.wrapped.CreateGeometryExportOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_connections(self: Self):
        """Method does not return."""
        self.wrapped.DeleteConnections()

    @property
    def cast_to(self: Self) -> "Part._Cast_Part":
        return self._Cast_Part(self)
