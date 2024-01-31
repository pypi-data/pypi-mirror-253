"""SpringDamperLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperLoadCase",)


Self = TypeVar("Self", bound="SpringDamperLoadCase")


class SpringDamperLoadCase(_6853.CouplingLoadCase):
    """SpringDamperLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperLoadCase")

    class _Cast_SpringDamperLoadCase:
        """Special nested class for casting SpringDamperLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
            parent: "SpringDamperLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_load_case(self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase"):
            return self._parent._cast(_6853.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "SpringDamperLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpringDamperLoadCase._Cast_SpringDamperLoadCase":
        return self._Cast_SpringDamperLoadCase(self)
