"""AbstractShaftFromCAD"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2495
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "AbstractShaftFromCAD"
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftFromCAD",)


Self = TypeVar("Self", bound="AbstractShaftFromCAD")


class AbstractShaftFromCAD(_2495.ComponentFromCAD):
    """AbstractShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftFromCAD")

    class _Cast_AbstractShaftFromCAD:
        """Special nested class for casting AbstractShaftFromCAD to subclasses."""

        def __init__(
            self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD",
            parent: "AbstractShaftFromCAD",
        ):
            self._parent = parent

        @property
        def component_from_cad(self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD"):
            return self._parent._cast(_2495.ComponentFromCAD)

        @property
        def planet_shaft_from_cad(
            self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2505

            return self._parent._cast(_2505.PlanetShaftFromCAD)

        @property
        def shaft_from_cad(self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD"):
            from mastapy.system_model.part_model.import_from_cad import _2509

            return self._parent._cast(_2509.ShaftFromCAD)

        @property
        def abstract_shaft_from_cad(
            self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD",
        ) -> "AbstractShaftFromCAD":
            return self._parent

        def __getattr__(
            self: "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @inner_diameter.setter
    @enforce_parameter_types
    def inner_diameter(self: Self, value: "float"):
        self.wrapped.InnerDiameter = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "AbstractShaftFromCAD._Cast_AbstractShaftFromCAD":
        return self._Cast_AbstractShaftFromCAD(self)
