"""AbstractShaftOrHousingLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.system_model.analyses_and_results.mbd_analyses import _5483
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.system_model.analyses_and_results.static_loads import _6837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftOrHousingLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingLoadCase",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingLoadCase")


class AbstractShaftOrHousingLoadCase(_6837.ComponentLoadCase):
    """AbstractShaftOrHousingLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftOrHousingLoadCase")

    class _Cast_AbstractShaftOrHousingLoadCase:
        """Special nested class for casting AbstractShaftOrHousingLoadCase to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
            parent: "AbstractShaftOrHousingLoadCase",
        ):
            self._parent = parent

        @property
        def component_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractShaftLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CycloidalDiscLoadCase)

        @property
        def fe_part_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.FEPartLoadCase)

        @property
        def shaft_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.ShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
        ) -> "AbstractShaftOrHousingLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftOrHousingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_flexibilities_setting(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftAndHousingFlexibilityOption]"""
        temp = self.wrapped.IncludeFlexibilitiesSetting

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @include_flexibilities_setting.setter
    @enforce_parameter_types
    def include_flexibilities_setting(
        self: Self, value: "_5483.ShaftAndHousingFlexibilityOption"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftAndHousingFlexibilityOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.IncludeFlexibilitiesSetting = value

    @property
    def rayleigh_damping_alpha(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_alpha.setter
    @enforce_parameter_types
    def rayleigh_damping_alpha(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingAlpha = value

    @property
    def temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Temperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @temperature.setter
    @enforce_parameter_types
    def temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Temperature = value

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingLoadCase._Cast_AbstractShaftOrHousingLoadCase":
        return self._Cast_AbstractShaftOrHousingLoadCase(self)
