"""MassDisc"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model import _2479
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")


__docformat__ = "restructuredtext en"
__all__ = ("MassDisc",)


Self = TypeVar("Self", bound="MassDisc")


class MassDisc(_2479.VirtualComponent):
    """MassDisc

    This is a mastapy class.
    """

    TYPE = _MASS_DISC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDisc")

    class _Cast_MassDisc:
        """Special nested class for casting MassDisc to subclasses."""

        def __init__(self: "MassDisc._Cast_MassDisc", parent: "MassDisc"):
            self._parent = parent

        @property
        def virtual_component(self: "MassDisc._Cast_MassDisc"):
            return self._parent._cast(_2479.VirtualComponent)

        @property
        def mountable_component(self: "MassDisc._Cast_MassDisc"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "MassDisc._Cast_MassDisc"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "MassDisc._Cast_MassDisc"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "MassDisc._Cast_MassDisc"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def mass_disc(self: "MassDisc._Cast_MassDisc") -> "MassDisc":
            return self._parent

        def __getattr__(self: "MassDisc._Cast_MassDisc", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDisc.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def density(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    @enforce_parameter_types
    def density(self: Self, value: "float"):
        self.wrapped.Density = float(value) if value is not None else 0.0

    @property
    def disc_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiscRotation

        if temp is None:
            return 0.0

        return temp

    @disc_rotation.setter
    @enforce_parameter_types
    def disc_rotation(self: Self, value: "float"):
        self.wrapped.DiscRotation = float(value) if value is not None else 0.0

    @property
    def disc_skew(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiscSkew

        if temp is None:
            return 0.0

        return temp

    @disc_skew.setter
    @enforce_parameter_types
    def disc_skew(self: Self, value: "float"):
        self.wrapped.DiscSkew = float(value) if value is not None else 0.0

    @property
    def inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def is_distributed(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsDistributed

        if temp is None:
            return False

        return temp

    @is_distributed.setter
    @enforce_parameter_types
    def is_distributed(self: Self, value: "bool"):
        self.wrapped.IsDistributed = bool(value) if value is not None else False

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "MassDisc._Cast_MassDisc":
        return self._Cast_MassDisc(self)
