"""ConnectorLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6924
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorLoadCase",)


Self = TypeVar("Self", bound="ConnectorLoadCase")


class ConnectorLoadCase(_6924.MountableComponentLoadCase):
    """ConnectorLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorLoadCase")

    class _Cast_ConnectorLoadCase:
        """Special nested class for casting ConnectorLoadCase to subclasses."""

        def __init__(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
            parent: "ConnectorLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BearingLoadCase)

        @property
        def oil_seal_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.OilSealLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.ShaftHubConnectionLoadCase)

        @property
        def connector_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ) -> "ConnectorLoadCase":
            return self._parent

        def __getattr__(self: "ConnectorLoadCase._Cast_ConnectorLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectorLoadCase._Cast_ConnectorLoadCase":
        return self._Cast_ConnectorLoadCase(self)
