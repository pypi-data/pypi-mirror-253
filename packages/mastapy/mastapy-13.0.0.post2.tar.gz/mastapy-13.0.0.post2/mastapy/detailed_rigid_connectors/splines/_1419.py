"""StandardSplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.detailed_rigid_connectors.splines import _1402, _1403, _1414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "StandardSplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1404


__docformat__ = "restructuredtext en"
__all__ = ("StandardSplineJointDesign",)


Self = TypeVar("Self", bound="StandardSplineJointDesign")


class StandardSplineJointDesign(_1414.SplineJointDesign):
    """StandardSplineJointDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StandardSplineJointDesign")

    class _Cast_StandardSplineJointDesign:
        """Special nested class for casting StandardSplineJointDesign to subclasses."""

        def __init__(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
            parent: "StandardSplineJointDesign",
        ):
            self._parent = parent

        @property
        def spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            return self._parent._cast(_1414.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors import _1386

            return self._parent._cast(_1386.DetailedRigidConnectorDesign)

        @property
        def din5480_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors.splines import _1392

            return self._parent._cast(_1392.DIN5480SplineJointDesign)

        @property
        def gbt3478_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors.splines import _1396

            return self._parent._cast(_1396.GBT3478SplineJointDesign)

        @property
        def iso4156_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors.splines import _1399

            return self._parent._cast(_1399.ISO4156SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors.splines import _1400

            return self._parent._cast(_1400.JISB1603SplineJointDesign)

        @property
        def sae_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ):
            from mastapy.detailed_rigid_connectors.splines import _1407

            return self._parent._cast(_1407.SAESplineJointDesign)

        @property
        def standard_spline_joint_design(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign",
        ) -> "StandardSplineJointDesign":
            return self._parent

        def __getattr__(
            self: "StandardSplineJointDesign._Cast_StandardSplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StandardSplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diametral_pitch(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch.setter
    @enforce_parameter_types
    def diametral_pitch(self: Self, value: "float"):
        self.wrapped.DiametralPitch = float(value) if value is not None else 0.0

    @property
    def module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: Self, value: "float"):
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def module_preferred(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_Modules":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.splines.Modules]"""
        temp = self.wrapped.ModulePreferred

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_Modules.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @module_preferred.setter
    @enforce_parameter_types
    def module_preferred(self: Self, value: "_1402.Modules"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_Modules.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ModulePreferred = value

    @property
    def module_from_preferred_series(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModuleFromPreferredSeries

        if temp is None:
            return False

        return temp

    @module_from_preferred_series.setter
    @enforce_parameter_types
    def module_from_preferred_series(self: Self, value: "bool"):
        self.wrapped.ModuleFromPreferredSeries = (
            bool(value) if value is not None else False
        )

    @property
    def pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    @enforce_parameter_types
    def pressure_angle(self: Self, value: "float"):
        self.wrapped.PressureAngle = float(value) if value is not None else 0.0

    @property
    def pressure_angle_preferred(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.splines.PressureAngleTypes]"""
        temp = self.wrapped.PressureAnglePreferred

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @pressure_angle_preferred.setter
    @enforce_parameter_types
    def pressure_angle_preferred(self: Self, value: "_1403.PressureAngleTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PressureAnglePreferred = value

    @property
    def root_type(self: Self) -> "_1404.RootTypes":
        """mastapy.detailed_rigid_connectors.splines.RootTypes"""
        temp = self.wrapped.RootType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.RootTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1404", "RootTypes"
        )(value)

    @root_type.setter
    @enforce_parameter_types
    def root_type(self: Self, value: "_1404.RootTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.RootTypes"
        )
        self.wrapped.RootType = value

    @property
    def cast_to(
        self: Self,
    ) -> "StandardSplineJointDesign._Cast_StandardSplineJointDesign":
        return self._Cast_StandardSplineJointDesign(self)
