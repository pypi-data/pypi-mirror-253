"""ConicalGearMicroGeometryConfigBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _796


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMicroGeometryConfigBase",)


Self = TypeVar("Self", bound="ConicalGearMicroGeometryConfigBase")


class ConicalGearMicroGeometryConfigBase(_1221.GearImplementationDetail):
    """ConicalGearMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMicroGeometryConfigBase")

    class _Cast_ConicalGearMicroGeometryConfigBase:
        """Special nested class for casting ConicalGearMicroGeometryConfigBase to subclasses."""

        def __init__(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
            parent: "ConicalGearMicroGeometryConfigBase",
        ):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.manufacturing.bevel import _777

            return self._parent._cast(_777.ConicalGearMicroGeometryConfig)

        @property
        def conical_pinion_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ):
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
        ) -> "ConicalGearMicroGeometryConfigBase":
            return self._parent

        def __getattr__(
            self: "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConicalGearMicroGeometryConfigBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_measurement_border(self: Self) -> "_796.FlankMeasurementBorder":
        """mastapy.gears.manufacturing.bevel.FlankMeasurementBorder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase":
        return self._Cast_ConicalGearMicroGeometryConfigBase(self)
