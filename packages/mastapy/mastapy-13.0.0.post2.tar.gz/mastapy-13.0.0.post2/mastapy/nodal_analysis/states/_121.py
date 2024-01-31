"""ElementVectorState"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.states import _122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_VECTOR_STATE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.States", "ElementVectorState"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementVectorState",)


Self = TypeVar("Self", bound="ElementVectorState")


class ElementVectorState(_122.EntityVectorState):
    """ElementVectorState

    This is a mastapy class.
    """

    TYPE = _ELEMENT_VECTOR_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementVectorState")

    class _Cast_ElementVectorState:
        """Special nested class for casting ElementVectorState to subclasses."""

        def __init__(
            self: "ElementVectorState._Cast_ElementVectorState",
            parent: "ElementVectorState",
        ):
            self._parent = parent

        @property
        def entity_vector_state(self: "ElementVectorState._Cast_ElementVectorState"):
            return self._parent._cast(_122.EntityVectorState)

        @property
        def element_scalar_state(self: "ElementVectorState._Cast_ElementVectorState"):
            from mastapy.nodal_analysis.states import _120

            return self._parent._cast(_120.ElementScalarState)

        @property
        def element_vector_state(
            self: "ElementVectorState._Cast_ElementVectorState",
        ) -> "ElementVectorState":
            return self._parent

        def __getattr__(self: "ElementVectorState._Cast_ElementVectorState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementVectorState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElementVectorState._Cast_ElementVectorState":
        return self._Cast_ElementVectorState(self)
