"""PeriodicExcitationWithReferenceShaft"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PeriodicExcitationWithReferenceShaft",
)


__docformat__ = "restructuredtext en"
__all__ = ("PeriodicExcitationWithReferenceShaft",)


Self = TypeVar("Self", bound="PeriodicExcitationWithReferenceShaft")


class PeriodicExcitationWithReferenceShaft(_5678.AbstractPeriodicExcitationDetail):
    """PeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PeriodicExcitationWithReferenceShaft")

    class _Cast_PeriodicExcitationWithReferenceShaft:
        """Special nested class for casting PeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
            parent: "PeriodicExcitationWithReferenceShaft",
        ):
            self._parent = parent

        @property
        def abstract_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            return self._parent._cast(_5678.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(
                _5733.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(
                _5734.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(
                _5735.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(
                _5736.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(
                _5737.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(
                _5738.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(
                _5739.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(
                _5740.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(
                _5741.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(
                _5742.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(
                _5743.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def general_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GeneralPeriodicExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(
                _5808.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.UnbalancedMassExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "PeriodicExcitationWithReferenceShaft":
            return self._parent

        def __getattr__(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
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
        self: Self, instance_to_wrap: "PeriodicExcitationWithReferenceShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft":
        return self._Cast_PeriodicExcitationWithReferenceShaft(self)
