"""GearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearMeshRating")

if TYPE_CHECKING:
    from mastapy.gears.load_case import _875


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshRating",)


Self = TypeVar("Self", bound="GearMeshRating")


class GearMeshRating(_353.AbstractGearMeshRating):
    """GearMeshRating

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshRating")

    class _Cast_GearMeshRating:
        """Special nested class for casting GearMeshRating to subclasses."""

        def __init__(
            self: "GearMeshRating._Cast_GearMeshRating", parent: "GearMeshRating"
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            return self._parent._cast(_353.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.worm import _373

            return self._parent._cast(_373.WormGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(
                _411.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearMeshRating)

        @property
        def face_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.face import _447

            return self._parent._cast(_447.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.conical import _539

            return self._parent._cast(_539.ConicalGearMeshRating)

        @property
        def concept_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.concept import _550

            return self._parent._cast(_550.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ) -> "GearMeshRating":
            return self._parent

        def __getattr__(self: "GearMeshRating._Cast_GearMeshRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driving_gear(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DrivingGear

        if temp is None:
            return ""

        return temp

    @property
    def energy_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionName

        if temp is None:
            return ""

        return temp

    @property
    def pinion_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_pinion_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedPinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_wheel_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedWheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelName

        if temp is None:
            return ""

        return temp

    @property
    def wheel_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_load_case(self: Self) -> "_875.MeshLoadCase":
        """mastapy.gears.load_case.MeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshRating._Cast_GearMeshRating":
        return self._Cast_GearMeshRating(self)
