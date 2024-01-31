"""ConicalGearMicroGeometryConfig"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearMicroGeometryConfig"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalGearMicroGeometryConfig")


class ConicalGearMicroGeometryConfig(_778.ConicalGearMicroGeometryConfigBase):
    """ConicalGearMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMicroGeometryConfig")

    class _Cast_ConicalGearMicroGeometryConfig:
        """Special nested class for casting ConicalGearMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
            parent: "ConicalGearMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ):
            return self._parent._cast(_778.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def conical_pinion_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalPinionMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
        ) -> "ConicalGearMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMicroGeometryConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMicroGeometryConfig._Cast_ConicalGearMicroGeometryConfig":
        return self._Cast_ConicalGearMicroGeometryConfig(self)
