"""PlungeShavingDynamicsCalculationForHobbedGears"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _768,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShavingDynamicsCalculationForHobbedGears",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShavingDynamicsCalculationForHobbedGears",)


Self = TypeVar("Self", bound="PlungeShavingDynamicsCalculationForHobbedGears")


class PlungeShavingDynamicsCalculationForHobbedGears(
    _768.ShavingDynamicsCalculationForHobbedGears["_755.PlungeShaverDynamics"]
):
    """PlungeShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlungeShavingDynamicsCalculationForHobbedGears"
    )

    class _Cast_PlungeShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting PlungeShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
            parent: "PlungeShavingDynamicsCalculationForHobbedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ):
            return self._parent._cast(_768.ShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _766,
            )

            return self._parent._cast(_766.ShavingDynamicsCalculation)

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ) -> "PlungeShavingDynamicsCalculationForHobbedGears":
            return self._parent

        def __getattr__(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
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
        instance_to_wrap: "PlungeShavingDynamicsCalculationForHobbedGears.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears":
        return self._Cast_PlungeShavingDynamicsCalculationForHobbedGears(self)
