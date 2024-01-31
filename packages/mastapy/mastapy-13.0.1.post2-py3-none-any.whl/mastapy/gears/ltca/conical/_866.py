"""ConicalGearContactStiffnessNode"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CONTACT_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearContactStiffnessNode"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearContactStiffnessNode",)


Self = TypeVar("Self", bound="ConicalGearContactStiffnessNode")


class ConicalGearContactStiffnessNode(_836.GearContactStiffnessNode):
    """ConicalGearContactStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CONTACT_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearContactStiffnessNode")

    class _Cast_ConicalGearContactStiffnessNode:
        """Special nested class for casting ConicalGearContactStiffnessNode to subclasses."""

        def __init__(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
            parent: "ConicalGearContactStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_contact_stiffness_node(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
        ):
            return self._parent._cast(_836.GearContactStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
        ):
            from mastapy.gears.ltca import _848

            return self._parent._cast(_848.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
        ):
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
        ) -> "ConicalGearContactStiffnessNode":
            return self._parent

        def __getattr__(
            self: "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearContactStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearContactStiffnessNode._Cast_ConicalGearContactStiffnessNode":
        return self._Cast_ConicalGearContactStiffnessNode(self)
