"""AbstractGearMeshRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearMeshRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshRating",)


Self = TypeVar("Self", bound="AbstractGearMeshRating")


class AbstractGearMeshRating(_1216.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshRating")

    class _Cast_AbstractGearMeshRating:
        """Special nested class for casting AbstractGearMeshRating to subclasses."""

        def __init__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
            parent: "AbstractGearMeshRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.worm import _373

            return self._parent._cast(_373.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.worm import _377

            return self._parent._cast(_377.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(
                _411.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.face import _446

            return self._parent._cast(_446.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.face import _447

            return self._parent._cast(_447.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.cylindrical import _466

            return self._parent._cast(_466.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.conical import _539

            return self._parent._cast(_539.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.conical import _544

            return self._parent._cast(_544.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.concept import _549

            return self._parent._cast(_549.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.concept import _550

            return self._parent._cast(_550.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "AbstractGearMeshRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def normalized_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "AbstractGearMeshRating._Cast_AbstractGearMeshRating":
        return self._Cast_AbstractGearMeshRating(self)
