"""InteriorPermanentMagnetAndSynchronousReluctanceRotor"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1289
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1270, _1295, _1254, _1287, _1309, _1310


__docformat__ = "restructuredtext en"
__all__ = ("InteriorPermanentMagnetAndSynchronousReluctanceRotor",)


Self = TypeVar("Self", bound="InteriorPermanentMagnetAndSynchronousReluctanceRotor")


class InteriorPermanentMagnetAndSynchronousReluctanceRotor(_1289.PermanentMagnetRotor):
    """InteriorPermanentMagnetAndSynchronousReluctanceRotor

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor"
    )

    class _Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor:
        """Special nested class for casting InteriorPermanentMagnetAndSynchronousReluctanceRotor to subclasses."""

        def __init__(
            self: "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor",
            parent: "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
        ):
            self._parent = parent

        @property
        def permanent_magnet_rotor(
            self: "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor",
        ):
            return self._parent._cast(_1289.PermanentMagnetRotor)

        @property
        def rotor(
            self: "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor",
        ):
            from mastapy.electric_machines import _1292

            return self._parent._cast(_1292.Rotor)

        @property
        def interior_permanent_magnet_and_synchronous_reluctance_rotor(
            self: "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor",
        ) -> "InteriorPermanentMagnetAndSynchronousReluctanceRotor":
            return self._parent

        def __getattr__(
            self: "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor",
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
        self: Self,
        instance_to_wrap: "InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flux_barrier_style(self: Self) -> "_1270.FluxBarrierStyle":
        """mastapy.electric_machines.FluxBarrierStyle"""
        temp = self.wrapped.FluxBarrierStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.FluxBarrierStyle"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1270", "FluxBarrierStyle"
        )(value)

    @flux_barrier_style.setter
    @enforce_parameter_types
    def flux_barrier_style(self: Self, value: "_1270.FluxBarrierStyle"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.FluxBarrierStyle"
        )
        self.wrapped.FluxBarrierStyle = value

    @property
    def number_of_cooling_duct_layers(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfCoolingDuctLayers

        if temp is None:
            return 0

        return temp

    @number_of_cooling_duct_layers.setter
    @enforce_parameter_types
    def number_of_cooling_duct_layers(self: Self, value: "int"):
        self.wrapped.NumberOfCoolingDuctLayers = int(value) if value is not None else 0

    @property
    def number_of_magnet_flux_barrier_layers(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfMagnetFluxBarrierLayers

        if temp is None:
            return 0

        return temp

    @number_of_magnet_flux_barrier_layers.setter
    @enforce_parameter_types
    def number_of_magnet_flux_barrier_layers(self: Self, value: "int"):
        self.wrapped.NumberOfMagnetFluxBarrierLayers = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_notch_specifications(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfNotchSpecifications

        if temp is None:
            return 0

        return temp

    @number_of_notch_specifications.setter
    @enforce_parameter_types
    def number_of_notch_specifications(self: Self, value: "int"):
        self.wrapped.NumberOfNotchSpecifications = (
            int(value) if value is not None else 0
        )

    @property
    def rotor_type(self: Self) -> "_1295.RotorType":
        """mastapy.electric_machines.RotorType"""
        temp = self.wrapped.RotorType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.RotorType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1295", "RotorType"
        )(value)

    @rotor_type.setter
    @enforce_parameter_types
    def rotor_type(self: Self, value: "_1295.RotorType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.RotorType"
        )
        self.wrapped.RotorType = value

    @property
    def cooling_duct_layers(self: Self) -> "List[_1254.CoolingDuctLayerSpecification]":
        """List[mastapy.electric_machines.CoolingDuctLayerSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoolingDuctLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def notch_specifications(self: Self) -> "List[_1287.NotchSpecification]":
        """List[mastapy.electric_machines.NotchSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def u_shape_layers(self: Self) -> "List[_1309.UShapedLayerSpecification]":
        """List[mastapy.electric_machines.UShapedLayerSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UShapeLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def v_shape_magnet_layers(
        self: Self,
    ) -> "List[_1310.VShapedMagnetLayerSpecification]":
        """List[mastapy.electric_machines.VShapedMagnetLayerSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VShapeMagnetLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "InteriorPermanentMagnetAndSynchronousReluctanceRotor._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor":
        return self._Cast_InteriorPermanentMagnetAndSynchronousReluctanceRotor(self)
