"""InterMountableComponentConnection"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


Self = TypeVar("Self", bound="InterMountableComponentConnection")


class InterMountableComponentConnection(_2272.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterMountableComponentConnection")

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            parent: "InterMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2268

            return self._parent._cast(_2268.BeltConnection)

        @property
        def cvt_belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2273

            return self._parent._cast(_2273.CVTBeltConnection)

        @property
        def rolling_ring_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.RollingRingConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2303

            return self._parent._cast(_2303.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2305

            return self._parent._cast(_2305.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.FaceGearMesh)

        @property
        def gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.ZerolBevelGearMesh)

        @property
        def ring_pins_to_disc_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2342

            return self._parent._cast(_2342.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2344

            return self._parent._cast(_2344.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2346

            return self._parent._cast(_2346.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2348

            return self._parent._cast(_2348.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2352

            return self._parent._cast(_2352.TorqueConverterConnection)

        @property
        def inter_mountable_component_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "InterMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnection._Cast_InterMountableComponentConnection":
        return self._Cast_InterMountableComponentConnection(self)
