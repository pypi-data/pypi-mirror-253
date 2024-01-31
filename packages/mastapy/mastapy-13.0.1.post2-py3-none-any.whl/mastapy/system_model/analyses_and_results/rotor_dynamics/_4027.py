"""ShaftComplexShape"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPLEX_SHAPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics", "ShaftComplexShape"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1605


__docformat__ = "restructuredtext en"
__all__ = ("ShaftComplexShape",)


Self = TypeVar("Self", bound="ShaftComplexShape")
TLinearMeasurement = TypeVar("TLinearMeasurement", bound="_1605.MeasurementBase")
TAngularMeasurement = TypeVar("TAngularMeasurement", bound="_1605.MeasurementBase")


class ShaftComplexShape(_0.APIBase, Generic[TLinearMeasurement, TAngularMeasurement]):
    """ShaftComplexShape

    This is a mastapy class.

    Generic Types:
        TLinearMeasurement
        TAngularMeasurement
    """

    TYPE = _SHAFT_COMPLEX_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftComplexShape")

    class _Cast_ShaftComplexShape:
        """Special nested class for casting ShaftComplexShape to subclasses."""

        def __init__(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
            parent: "ShaftComplexShape",
        ):
            self._parent = parent

        @property
        def shaft_forced_complex_shape(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
        ):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4028

            return self._parent._cast(_4028.ShaftForcedComplexShape)

        @property
        def shaft_modal_complex_shape(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
        ):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4029

            return self._parent._cast(_4029.ShaftModalComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
        ):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4030

            return self._parent._cast(_4030.ShaftModalComplexShapeAtSpeeds)

        @property
        def shaft_modal_complex_shape_at_stiffness(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
        ):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4031

            return self._parent._cast(_4031.ShaftModalComplexShapeAtStiffness)

        @property
        def shaft_complex_shape(
            self: "ShaftComplexShape._Cast_ShaftComplexShape",
        ) -> "ShaftComplexShape":
            return self._parent

        def __getattr__(self: "ShaftComplexShape._Cast_ShaftComplexShape", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftComplexShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_imaginary(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularImaginary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def angular_magnitude(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMagnitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def angular_phase(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularPhase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def angular_real(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularReal

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def linear_imaginary(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearImaginary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def linear_magnitude(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearMagnitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def linear_phase(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearPhase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def linear_real(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearReal

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftComplexShape._Cast_ShaftComplexShape":
        return self._Cast_ShaftComplexShape(self)
