"""ConicalMeshFEModel"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.fe_model import _1198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Conical", "ConicalMeshFEModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshFEModel",)


Self = TypeVar("Self", bound="ConicalMeshFEModel")


class ConicalMeshFEModel(_1198.GearMeshFEModel):
    """ConicalMeshFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshFEModel")

    class _Cast_ConicalMeshFEModel:
        """Special nested class for casting ConicalMeshFEModel to subclasses."""

        def __init__(
            self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel",
            parent: "ConicalMeshFEModel",
        ):
            self._parent = parent

        @property
        def gear_mesh_fe_model(self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel"):
            return self._parent._cast(_1198.GearMeshFEModel)

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel",
        ):
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_fe_model(
            self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel",
        ) -> "ConicalMeshFEModel":
            return self._parent

        def __getattr__(self: "ConicalMeshFEModel._Cast_ConicalMeshFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalMeshFEModel._Cast_ConicalMeshFEModel":
        return self._Cast_ConicalMeshFEModel(self)
