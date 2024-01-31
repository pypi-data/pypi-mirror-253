"""PartToPartShearCouplingHalfLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfLoadCase",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfLoadCase")


class PartToPartShearCouplingHalfLoadCase(_6852.CouplingHalfLoadCase):
    """PartToPartShearCouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCouplingHalfLoadCase")

    class _Cast_PartToPartShearCouplingHalfLoadCase:
        """Special nested class for casting PartToPartShearCouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
            parent: "PartToPartShearCouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            return self._parent._cast(_6852.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "PartToPartShearCouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> (
        "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase"
    ):
        return self._Cast_PartToPartShearCouplingHalfLoadCase(self)
