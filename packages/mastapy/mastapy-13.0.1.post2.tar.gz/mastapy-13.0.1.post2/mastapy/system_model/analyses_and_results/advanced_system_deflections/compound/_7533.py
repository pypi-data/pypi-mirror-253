"""ZerolBevelGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7423,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7404,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundAdvancedSystemDeflection")


class ZerolBevelGearMeshCompoundAdvancedSystemDeflection(
    _7423.BevelGearMeshCompoundAdvancedSystemDeflection
):
    """ZerolBevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
            parent: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ZerolBevelGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_7404.ZerolBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7404.ZerolBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearMeshAdvancedSystemDeflection]

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
    ) -> "ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection(self)
