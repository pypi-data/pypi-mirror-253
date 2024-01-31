"""SpiralBevelGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7423,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7376,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundAdvancedSystemDeflection")


class SpiralBevelGearMeshCompoundAdvancedSystemDeflection(
    _7423.BevelGearMeshCompoundAdvancedSystemDeflection
):
    """SpiralBevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpiralBevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
            parent: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "SpiralBevelGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7376.SpiralBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpiralBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7376.SpiralBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpiralBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_SpiralBevelGearMeshCompoundAdvancedSystemDeflection(self)
