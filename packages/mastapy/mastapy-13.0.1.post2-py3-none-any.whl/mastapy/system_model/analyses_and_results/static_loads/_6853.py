"""CouplingHalfLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6925
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfLoadCase",)


Self = TypeVar("Self", bound="CouplingHalfLoadCase")


class CouplingHalfLoadCase(_6925.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfLoadCase")

    class _Cast_CouplingHalfLoadCase:
        """Special nested class for casting CouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
            parent: "CouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptCouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CVTPulleyLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartToPartShearCouplingHalfLoadCase)

        @property
        def pulley_load_case(self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PulleyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.RollingRingLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpringDamperHalfLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.TorqueConverterTurbineLoadCase)

        @property
        def coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "CouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase":
        return self._Cast_CouplingHalfLoadCase(self)
