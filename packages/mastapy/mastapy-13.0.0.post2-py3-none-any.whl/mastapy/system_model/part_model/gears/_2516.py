"""BevelDifferentialGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1182
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.connections_and_sockets.gears import _2303


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSet",)


Self = TypeVar("Self", bound="BevelDifferentialGearSet")


class BevelDifferentialGearSet(_2520.BevelGearSet):
    """BevelDifferentialGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearSet")

    class _Cast_BevelDifferentialGearSet:
        """Special nested class for casting BevelDifferentialGearSet to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
            parent: "BevelDifferentialGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            return self._parent._cast(_2520.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.ConicalGearSet)

        @property
        def gear_set(self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.GearSet)

        @property
        def specialised_assembly(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def part(self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet",
        ) -> "BevelDifferentialGearSet":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_1182.BevelGearSetDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_set_design(self: Self) -> "_1182.BevelGearSetDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears(self: Self) -> "List[_2519.BevelGear]":
        """List[mastapy.system_model.part_model.gears.BevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes(self: Self) -> "List[_2303.BevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.BevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSet._Cast_BevelDifferentialGearSet":
        return self._Cast_BevelDifferentialGearSet(self)
