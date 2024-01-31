"""MountableComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2444
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435, _2445
    from mastapy.system_model.connections_and_sockets import _2272, _2276, _2269


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2444.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(self: "MountableComponent._Cast_MountableComponent"):
            return self._parent._cast(_2444.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bearing(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2439

            return self._parent._cast(_2439.Bearing)

        @property
        def connector(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2447

            return self._parent._cast(_2447.Connector)

        @property
        def mass_disc(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MassDisc)

        @property
        def measurement_component(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.MeasurementComponent)

        @property
        def oil_seal(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.OilSeal)

        @property
        def planet_carrier(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PlanetCarrier)

        @property
        def point_load(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.PointLoad)

        @property
        def power_load(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.PowerLoad)

        @property
        def unbalanced_mass(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2477

            return self._parent._cast(_2477.UnbalancedMass)

        @property
        def virtual_component(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def concept_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConceptGear)

        @property
        def conical_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConicalGear)

        @property
        def cylindrical_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.CylindricalPlanetGear)

        @property
        def face_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def hypoid_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def worm_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.WormGear)

        @property
        def zerol_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def ring_pins(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.cycloidal import _2570

            return self._parent._cast(_2570.RingPins)

        @property
        def clutch_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ClutchHalf)

        @property
        def concept_coupling_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2582

            return self._parent._cast(_2582.ConceptCouplingHalf)

        @property
        def coupling_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CouplingHalf)

        @property
        def cvt_pulley(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2590

            return self._parent._cast(_2590.Pulley)

        @property
        def rolling_ring(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.RollingRing)

        @property
        def shaft_hub_connection(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.ShaftHubConnection)

        @property
        def spring_damper_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.SpringDamperHalf)

        @property
        def synchroniser_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserHalf)

        @property
        def synchroniser_part(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserSleeve)

        @property
        def torque_converter_pump(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2435.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2272.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2276.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2435.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2435.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2445.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)
