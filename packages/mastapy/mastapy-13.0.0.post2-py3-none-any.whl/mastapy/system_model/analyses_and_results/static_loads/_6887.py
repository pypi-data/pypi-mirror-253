"""FEPartLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import _2383
from mastapy.system_model.analyses_and_results.static_loads import _6808
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FEPartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2359
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6835


__docformat__ = "restructuredtext en"
__all__ = ("FEPartLoadCase",)


Self = TypeVar("Self", bound="FEPartLoadCase")


class FEPartLoadCase(_6808.AbstractShaftOrHousingLoadCase):
    """FEPartLoadCase

    This is a mastapy class.
    """

    TYPE = _FE_PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartLoadCase")

    class _Cast_FEPartLoadCase:
        """Special nested class for casting FEPartLoadCase to subclasses."""

        def __init__(
            self: "FEPartLoadCase._Cast_FEPartLoadCase", parent: "FEPartLoadCase"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_load_case(
            self: "FEPartLoadCase._Cast_FEPartLoadCase",
        ):
            return self._parent._cast(_6808.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(self: "FEPartLoadCase._Cast_FEPartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(self: "FEPartLoadCase._Cast_FEPartLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "FEPartLoadCase._Cast_FEPartLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartLoadCase._Cast_FEPartLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "FEPartLoadCase._Cast_FEPartLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_load_case(
            self: "FEPartLoadCase._Cast_FEPartLoadCase",
        ) -> "FEPartLoadCase":
            return self._parent

        def __getattr__(self: "FEPartLoadCase._Cast_FEPartLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_angle_index(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.ActiveAngleIndex

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @active_angle_index.setter
    @enforce_parameter_types
    def active_angle_index(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.ActiveAngleIndex = value

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def angle_source(self: Self) -> "_2359.AngleSource":
        """mastapy.system_model.fe.AngleSource

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.FE.AngleSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe._2359", "AngleSource"
        )(value)

    @property
    def fe_substructure(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FESubstructure":
        """ListWithSelectedItem[mastapy.system_model.fe.FESubstructure]"""
        temp = self.wrapped.FESubstructure

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FESubstructure",
        )(temp)

    @fe_substructure.setter
    @enforce_parameter_types
    def fe_substructure(self: Self, value: "_2383.FESubstructure"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.FESubstructure = value

    @property
    def mass_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MassScalingFactor

        if temp is None:
            return 0.0

        return temp

    @mass_scaling_factor.setter
    @enforce_parameter_types
    def mass_scaling_factor(self: Self, value: "float"):
        self.wrapped.MassScalingFactor = float(value) if value is not None else 0.0

    @property
    def override_default_fe_substructure(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDefaultFESubstructure

        if temp is None:
            return False

        return temp

    @override_default_fe_substructure.setter
    @enforce_parameter_types
    def override_default_fe_substructure(self: Self, value: "bool"):
        self.wrapped.OverrideDefaultFESubstructure = (
            bool(value) if value is not None else False
        )

    @property
    def stiffness_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StiffnessScalingFactor

        if temp is None:
            return 0.0

        return temp

    @stiffness_scaling_factor.setter
    @enforce_parameter_types
    def stiffness_scaling_factor(self: Self, value: "float"):
        self.wrapped.StiffnessScalingFactor = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def surfaces_for_data_logging(
        self: Self,
    ) -> "List[_6835.CMSElementFaceGroupWithSelectionOption]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CMSElementFaceGroupWithSelectionOption]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfacesForDataLogging

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FEPartLoadCase._Cast_FEPartLoadCase":
        return self._Cast_FEPartLoadCase(self)
