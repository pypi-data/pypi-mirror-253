"""SpiralBevelGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshLoadCase",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshLoadCase")


class SpiralBevelGearMeshLoadCase(_6828.BevelGearMeshLoadCase):
    """SpiralBevelGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshLoadCase")

    class _Cast_SpiralBevelGearMeshLoadCase:
        """Special nested class for casting SpiralBevelGearMeshLoadCase to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
            parent: "SpiralBevelGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            return self._parent._cast(_6828.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6814

            return self._parent._cast(_6814.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "SpiralBevelGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase":
        return self._Cast_SpiralBevelGearMeshLoadCase(self)
