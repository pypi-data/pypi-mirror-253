"""RelativeMeasurementViewModel"""
from __future__ import annotations

from typing import TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_MEASUREMENT_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "RelativeMeasurementViewModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("RelativeMeasurementViewModel",)


Self = TypeVar("Self", bound="RelativeMeasurementViewModel")
T = TypeVar("T")


class RelativeMeasurementViewModel(_0.APIBase, Generic[T]):
    """RelativeMeasurementViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_MEASUREMENT_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RelativeMeasurementViewModel")

    class _Cast_RelativeMeasurementViewModel:
        """Special nested class for casting RelativeMeasurementViewModel to subclasses."""

        def __init__(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
            parent: "RelativeMeasurementViewModel",
        ):
            self._parent = parent

        @property
        def cylindrical_mesh_angular_backlash(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1037

            return self._parent._cast(_1037.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1040

            return self._parent._cast(_1040.CylindricalMeshLinearBacklashSpecification)

        @property
        def toleranced_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1083

            return self._parent._cast(_1083.TolerancedValueSpecification)

        @property
        def nominal_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1091,
            )

            return self._parent._cast(_1091.NominalValueSpecification)

        @property
        def no_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1092,
            )

            return self._parent._cast(_1092.NoValueSpecification)

        @property
        def relative_measurement_view_model(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "RelativeMeasurementViewModel":
            return self._parent

        def __getattr__(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RelativeMeasurementViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel":
        return self._Cast_RelativeMeasurementViewModel(self)
