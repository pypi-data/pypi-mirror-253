"""ElectricMachineStatorToothMomentsExcitationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_MOMENTS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothMomentsExcitationDetail",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothMomentsExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineStatorToothMomentsExcitationDetail")


class ElectricMachineStatorToothMomentsExcitationDetail(
    _5739.ElectricMachineStatorToothLoadsExcitationDetail
):
    """ElectricMachineStatorToothMomentsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_MOMENTS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineStatorToothMomentsExcitationDetail"
    )

    class _Cast_ElectricMachineStatorToothMomentsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothMomentsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
            parent: "ElectricMachineStatorToothMomentsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
        ):
            return self._parent._cast(
                _5739.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
        ) -> "ElectricMachineStatorToothMomentsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail",
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
        instance_to_wrap: "ElectricMachineStatorToothMomentsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothMomentsExcitationDetail._Cast_ElectricMachineStatorToothMomentsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothMomentsExcitationDetail(self)
