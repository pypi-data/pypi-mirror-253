"""Coupling"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("Coupling",)


Self = TypeVar("Self", bound="Coupling")


class Coupling(_2476.SpecialisedAssembly):
    """Coupling

    This is a mastapy class.
    """

    TYPE = _COUPLING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Coupling")

    class _Cast_Coupling:
        """Special nested class for casting Coupling to subclasses."""

        def __init__(self: "Coupling._Cast_Coupling", parent: "Coupling"):
            self._parent = parent

        @property
        def specialised_assembly(self: "Coupling._Cast_Coupling"):
            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def part(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def clutch(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model.couplings import _2578

            return self._parent._cast(_2578.Clutch)

        @property
        def concept_coupling(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.ConceptCoupling)

        @property
        def part_to_part_shear_coupling(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.PartToPartShearCoupling)

        @property
        def spring_damper(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.SpringDamper)

        @property
        def torque_converter(self: "Coupling._Cast_Coupling"):
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.TorqueConverter)

        @property
        def coupling(self: "Coupling._Cast_Coupling") -> "Coupling":
            return self._parent

        def __getattr__(self: "Coupling._Cast_Coupling", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Coupling.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(self: Self, value: "float"):
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def radial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    @enforce_parameter_types
    def radial_stiffness(self: Self, value: "float"):
        self.wrapped.RadialStiffness = float(value) if value is not None else 0.0

    @property
    def tilt_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: Self, value: "float"):
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def torsional_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: Self, value: "float"):
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def halves(self: Self) -> "List[_2584.CouplingHalf]":
        """List[mastapy.system_model.part_model.couplings.CouplingHalf]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Halves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def half_a(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HalfA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def half_b(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HalfB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Coupling._Cast_Coupling":
        return self._Cast_Coupling(self)
