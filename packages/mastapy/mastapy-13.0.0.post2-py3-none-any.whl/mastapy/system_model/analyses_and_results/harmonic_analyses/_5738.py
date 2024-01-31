"""ElectricMachineStatorToothAxialLoadsExcitationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_AXIAL_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothAxialLoadsExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineStatorToothAxialLoadsExcitationDetail")


class ElectricMachineStatorToothAxialLoadsExcitationDetail(
    _5739.ElectricMachineStatorToothLoadsExcitationDetail
):
    """ElectricMachineStatorToothAxialLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_AXIAL_LOADS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail"
    )

    class _Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothAxialLoadsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
            parent: "ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ):
            return self._parent._cast(
                _5739.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
        ) -> "ElectricMachineStatorToothAxialLoadsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail",
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
        instance_to_wrap: "ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothAxialLoadsExcitationDetail._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothAxialLoadsExcitationDetail(self)
