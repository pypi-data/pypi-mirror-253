"""KlingelnbergCycloPalloidConicalGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_conical import _983


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSet",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSet")


class KlingelnbergCycloPalloidConicalGearSet(_2524.ConicalGearSet):
    """KlingelnbergCycloPalloidConicalGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSet"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
            parent: "KlingelnbergCycloPalloidConicalGearSet",
        ):
            self._parent = parent

        @property
        def conical_gear_set(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            return self._parent._cast(_2524.ConicalGearSet)

        @property
        def gear_set(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.GearSet)

        @property
        def specialised_assembly(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def part(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
        ) -> "KlingelnbergCycloPalloidConicalGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_983.KlingelnbergConicalGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_conical.KlingelnbergConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_conical_gear_set_design(
        self: Self,
    ) -> "_983.KlingelnbergConicalGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_conical.KlingelnbergConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSet._Cast_KlingelnbergCycloPalloidConicalGearSet":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSet(self)
