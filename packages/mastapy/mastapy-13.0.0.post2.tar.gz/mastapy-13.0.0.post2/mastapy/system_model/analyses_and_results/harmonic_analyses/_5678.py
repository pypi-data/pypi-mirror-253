"""AbstractPeriodicExcitationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1379


__docformat__ = "restructuredtext en"
__all__ = ("AbstractPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="AbstractPeriodicExcitationDetail")


class AbstractPeriodicExcitationDetail(_0.APIBase):
    """AbstractPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractPeriodicExcitationDetail")

    class _Cast_AbstractPeriodicExcitationDetail:
        """Special nested class for casting AbstractPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            parent: "AbstractPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(
                _5733.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(
                _5734.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(
                _5735.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(
                _5736.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(
                _5737.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(
                _5738.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(
                _5739.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(
                _5740.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(
                _5741.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(
                _5742.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(
                _5743.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def gear_mesh_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.GearMeshExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.GearMeshTEExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GeneralPeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PeriodicExcitationWithReferenceShaft)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(
                _5808.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.UnbalancedMassExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "AbstractPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractPeriodicExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_load_data(self: Self) -> "_1379.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail":
        return self._Cast_AbstractPeriodicExcitationDetail(self)
