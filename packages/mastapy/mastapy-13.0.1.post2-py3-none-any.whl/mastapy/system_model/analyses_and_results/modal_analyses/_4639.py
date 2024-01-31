"""HypoidGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "HypoidGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315
    from mastapy.system_model.analyses_and_results.static_loads import _6907
    from mastapy.system_model.analyses_and_results.system_deflections import _2763


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshModalAnalysis")


class HypoidGearMeshModalAnalysis(_4576.AGMAGleasonConicalGearMeshModalAnalysis):
    """HypoidGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshModalAnalysis")

    class _Cast_HypoidGearMeshModalAnalysis:
        """Special nested class for casting HypoidGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
            parent: "HypoidGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            return self._parent._cast(_4576.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "HypoidGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshModalAnalysis.TYPE"):
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
    def connection_load_case(self: Self) -> "_6907.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2763.HypoidGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis":
        return self._Cast_HypoidGearMeshModalAnalysis(self)
