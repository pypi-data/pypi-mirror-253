"""SimpleBar"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_BAR = python_net_import("SMT.MastaAPI.NodalAnalysis.NodalEntities", "SimpleBar")


__docformat__ = "restructuredtext en"
__all__ = ("SimpleBar",)


Self = TypeVar("Self", bound="SimpleBar")


class SimpleBar(_151.TwoBodyConnectionNodalComponent):
    """SimpleBar

    This is a mastapy class.
    """

    TYPE = _SIMPLE_BAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SimpleBar")

    class _Cast_SimpleBar:
        """Special nested class for casting SimpleBar to subclasses."""

        def __init__(self: "SimpleBar._Cast_SimpleBar", parent: "SimpleBar"):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(self: "SimpleBar._Cast_SimpleBar"):
            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(self: "SimpleBar._Cast_SimpleBar"):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def nodal_composite(self: "SimpleBar._Cast_SimpleBar"):
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(self: "SimpleBar._Cast_SimpleBar"):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def simple_bar(self: "SimpleBar._Cast_SimpleBar") -> "SimpleBar":
            return self._parent

        def __getattr__(self: "SimpleBar._Cast_SimpleBar", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SimpleBar.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SimpleBar._Cast_SimpleBar":
        return self._Cast_SimpleBar(self)
