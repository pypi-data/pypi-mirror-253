"""ElectricMachineStatorToothRadialLoadsExcitationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_RADIAL_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothRadialLoadsExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineStatorToothRadialLoadsExcitationDetail")


class ElectricMachineStatorToothRadialLoadsExcitationDetail(
    _5739.ElectricMachineStatorToothLoadsExcitationDetail
):
    """ElectricMachineStatorToothRadialLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_RADIAL_LOADS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail"
    )

    class _Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothRadialLoadsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
            parent: "ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ):
            return self._parent._cast(
                _5739.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
        ) -> "ElectricMachineStatorToothRadialLoadsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail",
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
        instance_to_wrap: "ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothRadialLoadsExcitationDetail._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothRadialLoadsExcitationDetail(self)
