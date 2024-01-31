"""PlungeShavingDynamicsViewModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _770,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShavingDynamicsViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _756,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShavingDynamicsViewModel",)


Self = TypeVar("Self", bound="PlungeShavingDynamicsViewModel")


class PlungeShavingDynamicsViewModel(
    _770.ShavingDynamicsViewModel["_755.PlungeShaverDynamics"]
):
    """PlungeShavingDynamicsViewModel

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShavingDynamicsViewModel")

    class _Cast_PlungeShavingDynamicsViewModel:
        """Special nested class for casting PlungeShavingDynamicsViewModel to subclasses."""

        def __init__(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
            parent: "PlungeShavingDynamicsViewModel",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_view_model(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
        ):
            return self._parent._cast(_770.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _771,
            )

            return self._parent._cast(_771.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.GearManufacturingConfigurationViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
        ) -> "PlungeShavingDynamicsViewModel":
            return self._parent

        def __getattr__(
            self: "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShavingDynamicsViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def transverse_plane_on_gear_for_analysis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransversePlaneOnGearForAnalysis

        if temp is None:
            return 0.0

        return temp

    @transverse_plane_on_gear_for_analysis.setter
    @enforce_parameter_types
    def transverse_plane_on_gear_for_analysis(self: Self, value: "float"):
        self.wrapped.TransversePlaneOnGearForAnalysis = (
            float(value) if value is not None else 0.0
        )

    @property
    def settings(self: Self) -> "_756.PlungeShaverDynamicSettings":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel":
        return self._Cast_PlungeShavingDynamicsViewModel(self)
