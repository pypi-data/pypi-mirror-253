"""ConicalMeshMicroGeometryConfig"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshMicroGeometryConfig"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalMeshMicroGeometryConfig")


class ConicalMeshMicroGeometryConfig(_787.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshMicroGeometryConfig")

    class _Cast_ConicalMeshMicroGeometryConfig:
        """Special nested class for casting ConicalMeshMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
            parent: "ConicalMeshMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
        ):
            return self._parent._cast(_787.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_micro_geometry_config(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
        ) -> "ConicalMeshMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshMicroGeometryConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig":
        return self._Cast_ConicalMeshMicroGeometryConfig(self)
