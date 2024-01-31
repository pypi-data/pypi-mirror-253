"""GearImplementationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1741


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationDetail",)


Self = TypeVar("Self", bound="GearImplementationDetail")


class GearImplementationDetail(_1218.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationDetail")

    class _Cast_GearImplementationDetail:
        """Special nested class for casting GearImplementationDetail to subclasses."""

        def __init__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
            parent: "GearImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.cylindrical import _612

            return self._parent._cast(_612.CylindricalGearManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _777

            return self._parent._cast(_777.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalWheelManufacturingConfig)

        @property
        def face_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.face import _993

            return self._parent._cast(_993.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100

            return self._parent._cast(_1100.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101

            return self._parent._cast(_1101.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104

            return self._parent._cast(_1104.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model import _1197

            return self._parent._cast(_1197.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model.cylindrical import _1201

            return self._parent._cast(_1201.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model.conical import _1204

            return self._parent._cast(_1204.ConicalGearFEModel)

        @property
        def gear_implementation_detail(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "GearImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def user_specified_data(self: Self) -> "_1741.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationDetail._Cast_GearImplementationDetail":
        return self._Cast_GearImplementationDetail(self)
