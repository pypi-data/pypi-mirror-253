"""CycloidalAssemblyLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyLoadCase",)


Self = TypeVar("Self", bound="CycloidalAssemblyLoadCase")


class CycloidalAssemblyLoadCase(_6952.SpecialisedAssemblyLoadCase):
    """CycloidalAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyLoadCase")

    class _Cast_CycloidalAssemblyLoadCase:
        """Special nested class for casting CycloidalAssemblyLoadCase to subclasses."""

        def __init__(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
            parent: "CycloidalAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_load_case(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase",
        ) -> "CycloidalAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2568.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblyLoadCase._Cast_CycloidalAssemblyLoadCase":
        return self._Cast_CycloidalAssemblyLoadCase(self)
