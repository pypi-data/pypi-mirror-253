"""ConicalGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.conical import _887
    from mastapy.gears.rating.conical import _545


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshRating",)


Self = TypeVar("Self", bound="ConicalGearMeshRating")


class ConicalGearMeshRating(_360.GearMeshRating):
    """ConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshRating")

    class _Cast_ConicalGearMeshRating:
        """Special nested class for casting ConicalGearMeshRating to subclasses."""

        def __init__(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
            parent: "ConicalGearMeshRating",
        ):
            self._parent = parent

        @property
        def gear_mesh_rating(self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating"):
            return self._parent._cast(_360.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(
                _411.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating",
        ) -> "ConicalGearMeshRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshRating._Cast_ConicalGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_load_case(self: Self) -> "_887.ConicalMeshLoadCase":
        """mastapy.gears.load_case.conical.ConicalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_mesh_load_case(self: Self) -> "_887.ConicalMeshLoadCase":
        """mastapy.gears.load_case.conical.ConicalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_545.ConicalMeshedGearRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshedGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearMeshRating._Cast_ConicalGearMeshRating":
        return self._Cast_ConicalGearMeshRating(self)
