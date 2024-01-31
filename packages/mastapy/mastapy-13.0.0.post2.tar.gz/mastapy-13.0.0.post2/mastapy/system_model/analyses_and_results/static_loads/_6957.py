"""SpringDamperHalfLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfLoadCase",)


Self = TypeVar("Self", bound="SpringDamperHalfLoadCase")


class SpringDamperHalfLoadCase(_6852.CouplingHalfLoadCase):
    """SpringDamperHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfLoadCase")

    class _Cast_SpringDamperHalfLoadCase:
        """Special nested class for casting SpringDamperHalfLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
            parent: "SpringDamperHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            return self._parent._cast(_6852.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "SpringDamperHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase":
        return self._Cast_SpringDamperHalfLoadCase(self)
