"""WormGrindingProcessCalculation"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _680
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessCalculation",
)


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessCalculation",)


Self = TypeVar("Self", bound="WormGrindingProcessCalculation")


class WormGrindingProcessCalculation(_680.ProcessCalculation):
    """WormGrindingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessCalculation")

    class _Cast_WormGrindingProcessCalculation:
        """Special nested class for casting WormGrindingProcessCalculation to subclasses."""

        def __init__(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
            parent: "WormGrindingProcessCalculation",
        ):
            self._parent = parent

        @property
        def process_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            return self._parent._cast(_680.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _692,
            )

            return self._parent._cast(_692.WormGrindingCutterCalculation)

        @property
        def worm_grinding_lead_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _693,
            )

            return self._parent._cast(_693.WormGrindingLeadCalculation)

        @property
        def worm_grinding_process_gear_shape(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _695,
            )

            return self._parent._cast(_695.WormGrindingProcessGearShape)

        @property
        def worm_grinding_process_mark_on_shaft(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _696,
            )

            return self._parent._cast(_696.WormGrindingProcessMarkOnShaft)

        @property
        def worm_grinding_process_pitch_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _697,
            )

            return self._parent._cast(_697.WormGrindingProcessPitchCalculation)

        @property
        def worm_grinding_process_profile_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _698,
            )

            return self._parent._cast(_698.WormGrindingProcessProfileCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _702,
            )

            return self._parent._cast(
                _702.WormGrindingProcessTotalModificationCalculation
            )

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "WormGrindingProcessCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingProcessCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation":
        return self._Cast_WormGrindingProcessCalculation(self)
