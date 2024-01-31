"""ElectricMachineRotorYForcePeriodicExcitationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5732
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineRotorYForcePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineRotorYForcePeriodicExcitationDetail")


class ElectricMachineRotorYForcePeriodicExcitationDetail(
    _5732.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineRotorYForcePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineRotorYForcePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachineRotorYForcePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorYForcePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
            parent: "ElectricMachineRotorYForcePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
        ):
            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
        ) -> "ElectricMachineRotorYForcePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail",
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
        instance_to_wrap: "ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail":
        return self._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail(self)
