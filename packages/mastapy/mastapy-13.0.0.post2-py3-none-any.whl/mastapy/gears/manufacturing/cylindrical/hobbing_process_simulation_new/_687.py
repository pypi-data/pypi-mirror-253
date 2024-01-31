"""ProcessSimulationViewModel"""
from __future__ import annotations

from typing import TypeVar, Generic

from mastapy.gears.manufacturing.cylindrical import _628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROCESS_SIMULATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "ProcessSimulationViewModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("ProcessSimulationViewModel",)


Self = TypeVar("Self", bound="ProcessSimulationViewModel")
T = TypeVar("T")


class ProcessSimulationViewModel(
    _628.GearManufacturingConfigurationViewModel, Generic[T]
):
    """ProcessSimulationViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _PROCESS_SIMULATION_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProcessSimulationViewModel")

    class _Cast_ProcessSimulationViewModel:
        """Special nested class for casting ProcessSimulationViewModel to subclasses."""

        def __init__(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
            parent: "ProcessSimulationViewModel",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
        ):
            return self._parent._cast(_628.GearManufacturingConfigurationViewModel)

        @property
        def hobbing_process_simulation_view_model(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _674,
            )

            return self._parent._cast(_674.HobbingProcessSimulationViewModel)

        @property
        def worm_grinding_process_simulation_view_model(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _701,
            )

            return self._parent._cast(_701.WormGrindingProcessSimulationViewModel)

        @property
        def process_simulation_view_model(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
        ) -> "ProcessSimulationViewModel":
            return self._parent

        def __getattr__(
            self: "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProcessSimulationViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ProcessSimulationViewModel._Cast_ProcessSimulationViewModel":
        return self._Cast_ProcessSimulationViewModel(self)
