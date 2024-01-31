"""GearStiffness"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis import _66
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS = python_net_import("SMT.MastaAPI.Gears.LTCA", "GearStiffness")


__docformat__ = "restructuredtext en"
__all__ = ("GearStiffness",)


Self = TypeVar("Self", bound="GearStiffness")


class GearStiffness(_66.FEStiffness):
    """GearStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearStiffness")

    class _Cast_GearStiffness:
        """Special nested class for casting GearStiffness to subclasses."""

        def __init__(
            self: "GearStiffness._Cast_GearStiffness", parent: "GearStiffness"
        ):
            self._parent = parent

        @property
        def fe_stiffness(self: "GearStiffness._Cast_GearStiffness"):
            return self._parent._cast(_66.FEStiffness)

        @property
        def gear_bending_stiffness(self: "GearStiffness._Cast_GearStiffness"):
            from mastapy.gears.ltca import _833

            return self._parent._cast(_833.GearBendingStiffness)

        @property
        def gear_contact_stiffness(self: "GearStiffness._Cast_GearStiffness"):
            from mastapy.gears.ltca import _835

            return self._parent._cast(_835.GearContactStiffness)

        @property
        def cylindrical_gear_bending_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ):
            from mastapy.gears.ltca.cylindrical import _851

            return self._parent._cast(_851.CylindricalGearBendingStiffness)

        @property
        def cylindrical_gear_contact_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ):
            from mastapy.gears.ltca.cylindrical import _853

            return self._parent._cast(_853.CylindricalGearContactStiffness)

        @property
        def conical_gear_bending_stiffness(self: "GearStiffness._Cast_GearStiffness"):
            from mastapy.gears.ltca.conical import _863

            return self._parent._cast(_863.ConicalGearBendingStiffness)

        @property
        def conical_gear_contact_stiffness(self: "GearStiffness._Cast_GearStiffness"):
            from mastapy.gears.ltca.conical import _865

            return self._parent._cast(_865.ConicalGearContactStiffness)

        @property
        def gear_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "GearStiffness":
            return self._parent

        def __getattr__(self: "GearStiffness._Cast_GearStiffness", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearStiffness._Cast_GearStiffness":
        return self._Cast_GearStiffness(self)
