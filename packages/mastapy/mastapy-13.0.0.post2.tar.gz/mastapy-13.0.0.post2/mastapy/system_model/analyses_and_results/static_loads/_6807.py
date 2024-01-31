"""AbstractShaftLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6808
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AbstractShaftLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftLoadCase",)


Self = TypeVar("Self", bound="AbstractShaftLoadCase")


class AbstractShaftLoadCase(_6808.AbstractShaftOrHousingLoadCase):
    """AbstractShaftLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftLoadCase")

    class _Cast_AbstractShaftLoadCase:
        """Special nested class for casting AbstractShaftLoadCase to subclasses."""

        def __init__(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
            parent: "AbstractShaftLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_load_case(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ):
            return self._parent._cast(_6808.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_load_case(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CycloidalDiscLoadCase)

        @property
        def shaft_load_case(self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.ShaftLoadCase)

        @property
        def abstract_shaft_load_case(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase",
        ) -> "AbstractShaftLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2435.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "AbstractShaftLoadCase._Cast_AbstractShaftLoadCase":
        return self._Cast_AbstractShaftLoadCase(self)
