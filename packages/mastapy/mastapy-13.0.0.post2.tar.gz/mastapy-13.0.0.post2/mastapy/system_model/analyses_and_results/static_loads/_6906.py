"""HypoidGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshLoadCase",)


Self = TypeVar("Self", bound="HypoidGearMeshLoadCase")


class HypoidGearMeshLoadCase(_6814.AGMAGleasonConicalGearMeshLoadCase):
    """HypoidGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshLoadCase")

    class _Cast_HypoidGearMeshLoadCase:
        """Special nested class for casting HypoidGearMeshLoadCase to subclasses."""

        def __init__(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
            parent: "HypoidGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            return self._parent._cast(_6814.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_load_case(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase",
        ) -> "HypoidGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase":
        return self._Cast_HypoidGearMeshLoadCase(self)
