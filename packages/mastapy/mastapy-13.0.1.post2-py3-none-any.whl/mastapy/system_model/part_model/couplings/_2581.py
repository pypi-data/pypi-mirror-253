"""ConceptCoupling"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _54
    from mastapy.math_utility import _1534


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCoupling",)


Self = TypeVar("Self", bound="ConceptCoupling")


class ConceptCoupling(_2583.Coupling):
    """ConceptCoupling

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCoupling")

    class _Cast_ConceptCoupling:
        """Special nested class for casting ConceptCoupling to subclasses."""

        def __init__(
            self: "ConceptCoupling._Cast_ConceptCoupling", parent: "ConceptCoupling"
        ):
            self._parent = parent

        @property
        def coupling(self: "ConceptCoupling._Cast_ConceptCoupling"):
            return self._parent._cast(_2583.Coupling)

        @property
        def specialised_assembly(self: "ConceptCoupling._Cast_ConceptCoupling"):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "ConceptCoupling._Cast_ConceptCoupling"):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def part(self: "ConceptCoupling._Cast_ConceptCoupling"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "ConceptCoupling._Cast_ConceptCoupling"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def concept_coupling(
            self: "ConceptCoupling._Cast_ConceptCoupling",
        ) -> "ConceptCoupling":
            return self._parent

        def __getattr__(self: "ConceptCoupling._Cast_ConceptCoupling", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCoupling.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coupling_type(self: Self) -> "_54.CouplingType":
        """mastapy.nodal_analysis.CouplingType"""
        temp = self.wrapped.CouplingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.CouplingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._54", "CouplingType"
        )(value)

    @coupling_type.setter
    @enforce_parameter_types
    def coupling_type(self: Self, value: "_54.CouplingType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.CouplingType"
        )
        self.wrapped.CouplingType = value

    @property
    def default_efficiency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DefaultEfficiency

        if temp is None:
            return 0.0

        return temp

    @default_efficiency.setter
    @enforce_parameter_types
    def default_efficiency(self: Self, value: "float"):
        self.wrapped.DefaultEfficiency = float(value) if value is not None else 0.0

    @property
    def default_speed_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DefaultSpeedRatio

        if temp is None:
            return 0.0

        return temp

    @default_speed_ratio.setter
    @enforce_parameter_types
    def default_speed_ratio(self: Self, value: "float"):
        self.wrapped.DefaultSpeedRatio = float(value) if value is not None else 0.0

    @property
    def display_tilt_in_2d_drawing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DisplayTiltIn2DDrawing

        if temp is None:
            return False

        return temp

    @display_tilt_in_2d_drawing.setter
    @enforce_parameter_types
    def display_tilt_in_2d_drawing(self: Self, value: "bool"):
        self.wrapped.DisplayTiltIn2DDrawing = (
            bool(value) if value is not None else False
        )

    @property
    def efficiency_vs_speed_ratio(self: Self) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.EfficiencyVsSpeedRatio

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @efficiency_vs_speed_ratio.setter
    @enforce_parameter_types
    def efficiency_vs_speed_ratio(self: Self, value: "_1534.Vector2DListAccessor"):
        self.wrapped.EfficiencyVsSpeedRatio = value.wrapped

    @property
    def halves_are_coincident(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HalvesAreCoincident

        if temp is None:
            return False

        return temp

    @halves_are_coincident.setter
    @enforce_parameter_types
    def halves_are_coincident(self: Self, value: "bool"):
        self.wrapped.HalvesAreCoincident = bool(value) if value is not None else False

    @property
    def specify_efficiency_vs_speed_ratio(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyEfficiencyVsSpeedRatio

        if temp is None:
            return False

        return temp

    @specify_efficiency_vs_speed_ratio.setter
    @enforce_parameter_types
    def specify_efficiency_vs_speed_ratio(self: Self, value: "bool"):
        self.wrapped.SpecifyEfficiencyVsSpeedRatio = (
            bool(value) if value is not None else False
        )

    @property
    def tilt_about_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltAboutX

        if temp is None:
            return 0.0

        return temp

    @tilt_about_x.setter
    @enforce_parameter_types
    def tilt_about_x(self: Self, value: "float"):
        self.wrapped.TiltAboutX = float(value) if value is not None else 0.0

    @property
    def tilt_about_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltAboutY

        if temp is None:
            return 0.0

        return temp

    @tilt_about_y.setter
    @enforce_parameter_types
    def tilt_about_y(self: Self, value: "float"):
        self.wrapped.TiltAboutY = float(value) if value is not None else 0.0

    @property
    def torsional_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalDamping

        if temp is None:
            return 0.0

        return temp

    @torsional_damping.setter
    @enforce_parameter_types
    def torsional_damping(self: Self, value: "float"):
        self.wrapped.TorsionalDamping = float(value) if value is not None else 0.0

    @property
    def translational_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TranslationalStiffness

        if temp is None:
            return 0.0

        return temp

    @translational_stiffness.setter
    @enforce_parameter_types
    def translational_stiffness(self: Self, value: "float"):
        self.wrapped.TranslationalStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConceptCoupling._Cast_ConceptCoupling":
        return self._Cast_ConceptCoupling(self)
