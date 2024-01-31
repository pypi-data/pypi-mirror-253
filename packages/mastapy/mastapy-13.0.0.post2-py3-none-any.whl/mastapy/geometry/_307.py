"""DrawStyle"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.geometry import _308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE = python_net_import("SMT.MastaAPI.Geometry", "DrawStyle")


__docformat__ = "restructuredtext en"
__all__ = ("DrawStyle",)


Self = TypeVar("Self", bound="DrawStyle")


class DrawStyle(_308.DrawStyleBase):
    """DrawStyle

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DrawStyle")

    class _Cast_DrawStyle:
        """Special nested class for casting DrawStyle to subclasses."""

        def __init__(self: "DrawStyle._Cast_DrawStyle", parent: "DrawStyle"):
            self._parent = parent

        @property
        def draw_style_base(self: "DrawStyle._Cast_DrawStyle"):
            return self._parent._cast(_308.DrawStyleBase)

        @property
        def model_view_options_draw_style(self: "DrawStyle._Cast_DrawStyle"):
            from mastapy.system_model.drawing import _2252

            return self._parent._cast(_2252.ModelViewOptionsDrawStyle)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "DrawStyle._Cast_DrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(self: "DrawStyle._Cast_DrawStyle"):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PowerFlowDrawStyle)

        @property
        def draw_style(self: "DrawStyle._Cast_DrawStyle") -> "DrawStyle":
            return self._parent

        def __getattr__(self: "DrawStyle._Cast_DrawStyle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def outline_axis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OutlineAxis

        if temp is None:
            return False

        return temp

    @outline_axis.setter
    @enforce_parameter_types
    def outline_axis(self: Self, value: "bool"):
        self.wrapped.OutlineAxis = bool(value) if value is not None else False

    @property
    def show_part_labels(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowPartLabels

        if temp is None:
            return False

        return temp

    @show_part_labels.setter
    @enforce_parameter_types
    def show_part_labels(self: Self, value: "bool"):
        self.wrapped.ShowPartLabels = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "DrawStyle._Cast_DrawStyle":
        return self._Cast_DrawStyle(self)
