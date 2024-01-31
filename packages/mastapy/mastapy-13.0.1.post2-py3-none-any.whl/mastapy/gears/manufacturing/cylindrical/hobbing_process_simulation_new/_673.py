"""HobbingProcessSimulationNew"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_NEW = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessSimulationNew",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _667,
        _668,
        _669,
        _670,
        _671,
        _675,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessSimulationNew",)


Self = TypeVar("Self", bound="HobbingProcessSimulationNew")


class HobbingProcessSimulationNew(
    _686.ProcessSimulationNew["_672.HobbingProcessSimulationInput"]
):
    """HobbingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_NEW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessSimulationNew")

    class _Cast_HobbingProcessSimulationNew:
        """Special nested class for casting HobbingProcessSimulationNew to subclasses."""

        def __init__(
            self: "HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew",
            parent: "HobbingProcessSimulationNew",
        ):
            self._parent = parent

        @property
        def process_simulation_new(
            self: "HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew",
        ):
            return self._parent._cast(_686.ProcessSimulationNew)

        @property
        def hobbing_process_simulation_new(
            self: "HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew",
        ) -> "HobbingProcessSimulationNew":
            return self._parent

        def __getattr__(
            self: "HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessSimulationNew.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hobbing_process_gear_shape_calculation(
        self: Self,
    ) -> "_667.HobbingProcessGearShape":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessGearShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessGearShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hobbing_process_lead_calculation(
        self: Self,
    ) -> "_668.HobbingProcessLeadCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessLeadCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessLeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hobbing_process_mark_on_shaft_calculation(
        self: Self,
    ) -> "_669.HobbingProcessMarkOnShaft":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessMarkOnShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessMarkOnShaftCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hobbing_process_pitch_calculation(
        self: Self,
    ) -> "_670.HobbingProcessPitchCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessPitchCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessPitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hobbing_process_profile_calculation(
        self: Self,
    ) -> "_671.HobbingProcessProfileCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessProfileCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hobbing_process_total_modification(
        self: Self,
    ) -> "_675.HobbingProcessTotalModificationCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.HobbingProcessTotalModificationCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobbingProcessTotalModification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew":
        return self._Cast_HobbingProcessSimulationNew(self)
