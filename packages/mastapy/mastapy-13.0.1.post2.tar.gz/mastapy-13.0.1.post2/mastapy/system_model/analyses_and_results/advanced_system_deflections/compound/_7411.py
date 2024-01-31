"""AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7439,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7278,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"
)


class AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection(
    _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7278.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7278.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection(
            self
        )
