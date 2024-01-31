"""ClutchLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578


__docformat__ = "restructuredtext en"
__all__ = ("ClutchLoadCase",)


Self = TypeVar("Self", bound="ClutchLoadCase")


class ClutchLoadCase(_6853.CouplingLoadCase):
    """ClutchLoadCase

    This is a mastapy class.
    """

    TYPE = _CLUTCH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchLoadCase")

    class _Cast_ClutchLoadCase:
        """Special nested class for casting ClutchLoadCase to subclasses."""

        def __init__(
            self: "ClutchLoadCase._Cast_ClutchLoadCase", parent: "ClutchLoadCase"
        ):
            self._parent = parent

        @property
        def coupling_load_case(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            return self._parent._cast(_6853.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchLoadCase._Cast_ClutchLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ClutchLoadCase._Cast_ClutchLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_load_case(
            self: "ClutchLoadCase._Cast_ClutchLoadCase",
        ) -> "ClutchLoadCase":
            return self._parent

        def __getattr__(self: "ClutchLoadCase._Cast_ClutchLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchLoadCase._Cast_ClutchLoadCase":
        return self._Cast_ClutchLoadCase(self)
