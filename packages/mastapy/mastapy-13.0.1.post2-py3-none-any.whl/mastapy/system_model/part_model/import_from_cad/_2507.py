"""RigidConnectorFromCAD"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_CONNECTOR_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "RigidConnectorFromCAD"
)


__docformat__ = "restructuredtext en"
__all__ = ("RigidConnectorFromCAD",)


Self = TypeVar("Self", bound="RigidConnectorFromCAD")


class RigidConnectorFromCAD(_2497.ConnectorFromCAD):
    """RigidConnectorFromCAD

    This is a mastapy class.
    """

    TYPE = _RIGID_CONNECTOR_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RigidConnectorFromCAD")

    class _Cast_RigidConnectorFromCAD:
        """Special nested class for casting RigidConnectorFromCAD to subclasses."""

        def __init__(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD",
            parent: "RigidConnectorFromCAD",
        ):
            self._parent = parent

        @property
        def connector_from_cad(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD",
        ):
            return self._parent._cast(_2497.ConnectorFromCAD)

        @property
        def mountable_component_from_cad(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2504

            return self._parent._cast(_2504.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD",
        ):
            from mastapy.system_model.part_model.import_from_cad import _2495

            return self._parent._cast(_2495.ComponentFromCAD)

        @property
        def rigid_connector_from_cad(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD",
        ) -> "RigidConnectorFromCAD":
            return self._parent

        def __getattr__(
            self: "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RigidConnectorFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "RigidConnectorFromCAD._Cast_RigidConnectorFromCAD":
        return self._Cast_RigidConnectorFromCAD(self)
