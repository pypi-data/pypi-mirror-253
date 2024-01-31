"""ConceptGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.gears.gear_designs.concept import _1176


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGear",)


Self = TypeVar("Self", bound="ConceptGear")


class ConceptGear(_2530.Gear):
    """ConceptGear

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGear")

    class _Cast_ConceptGear:
        """Special nested class for casting ConceptGear to subclasses."""

        def __init__(self: "ConceptGear._Cast_ConceptGear", parent: "ConceptGear"):
            self._parent = parent

        @property
        def gear(self: "ConceptGear._Cast_ConceptGear"):
            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(self: "ConceptGear._Cast_ConceptGear"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "ConceptGear._Cast_ConceptGear"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "ConceptGear._Cast_ConceptGear"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "ConceptGear._Cast_ConceptGear"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def concept_gear(self: "ConceptGear._Cast_ConceptGear") -> "ConceptGear":
            return self._parent

        def __getattr__(self: "ConceptGear._Cast_ConceptGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self: Self) -> "_2531.GearOrientations":
        """mastapy.system_model.part_model.gears.GearOrientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears._2531", "GearOrientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_2531.GearOrientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self: Self) -> "_1176.ConceptGearDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_design(self: Self) -> "_1176.ConceptGearDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGear._Cast_ConceptGear":
        return self._Cast_ConceptGear(self)
