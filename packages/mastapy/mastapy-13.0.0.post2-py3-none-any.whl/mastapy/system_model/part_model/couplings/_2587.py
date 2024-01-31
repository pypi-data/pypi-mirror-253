"""CVTPulley"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.couplings import _2598, _2590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulley",)


Self = TypeVar("Self", bound="CVTPulley")


class CVTPulley(_2590.Pulley):
    """CVTPulley

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulley")

    class _Cast_CVTPulley:
        """Special nested class for casting CVTPulley to subclasses."""

        def __init__(self: "CVTPulley._Cast_CVTPulley", parent: "CVTPulley"):
            self._parent = parent

        @property
        def pulley(self: "CVTPulley._Cast_CVTPulley"):
            return self._parent._cast(_2590.Pulley)

        @property
        def coupling_half(self: "CVTPulley._Cast_CVTPulley"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CouplingHalf)

        @property
        def mountable_component(self: "CVTPulley._Cast_CVTPulley"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "CVTPulley._Cast_CVTPulley"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "CVTPulley._Cast_CVTPulley"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "CVTPulley._Cast_CVTPulley"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def cvt_pulley(self: "CVTPulley._Cast_CVTPulley") -> "CVTPulley":
            return self._parent

        def __getattr__(self: "CVTPulley._Cast_CVTPulley", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulley.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_moving_sheave_on_the_left(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMovingSheaveOnTheLeft

        if temp is None:
            return False

        return temp

    @is_moving_sheave_on_the_left.setter
    @enforce_parameter_types
    def is_moving_sheave_on_the_left(self: Self, value: "bool"):
        self.wrapped.IsMovingSheaveOnTheLeft = (
            bool(value) if value is not None else False
        )

    @property
    def sliding_connection(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ShaftHubConnection":
        """ListWithSelectedItem[mastapy.system_model.part_model.couplings.ShaftHubConnection]"""
        temp = self.wrapped.SlidingConnection

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ShaftHubConnection",
        )(temp)

    @sliding_connection.setter
    @enforce_parameter_types
    def sliding_connection(self: Self, value: "_2598.ShaftHubConnection"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SlidingConnection = value

    @property
    def cast_to(self: Self) -> "CVTPulley._Cast_CVTPulley":
        return self._Cast_CVTPulley(self)
