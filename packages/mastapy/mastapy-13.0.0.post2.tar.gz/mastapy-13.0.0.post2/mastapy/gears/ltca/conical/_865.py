"""ConicalGearContactStiffness"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CONTACT_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearContactStiffness"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearContactStiffness",)


Self = TypeVar("Self", bound="ConicalGearContactStiffness")


class ConicalGearContactStiffness(_835.GearContactStiffness):
    """ConicalGearContactStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CONTACT_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearContactStiffness")

    class _Cast_ConicalGearContactStiffness:
        """Special nested class for casting ConicalGearContactStiffness to subclasses."""

        def __init__(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
            parent: "ConicalGearContactStiffness",
        ):
            self._parent = parent

        @property
        def gear_contact_stiffness(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
        ):
            return self._parent._cast(_835.GearContactStiffness)

        @property
        def gear_stiffness(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
        ):
            from mastapy.gears.ltca import _847

            return self._parent._cast(_847.GearStiffness)

        @property
        def fe_stiffness(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
        ):
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def conical_gear_contact_stiffness(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
        ) -> "ConicalGearContactStiffness":
            return self._parent

        def __getattr__(
            self: "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearContactStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearContactStiffness._Cast_ConicalGearContactStiffness":
        return self._Cast_ConicalGearContactStiffness(self)
