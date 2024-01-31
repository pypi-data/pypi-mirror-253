"""CylindricalGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6594


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshCompoundCriticalSpeedAnalysis")


class CylindricalGearMeshCompoundCriticalSpeedAnalysis(
    _6734.GearMeshCompoundCriticalSpeedAnalysis
):
    """CylindricalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CylindricalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
            parent: "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6734.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CylindricalGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

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
    ) -> "List[_6594.CylindricalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CylindricalGearMeshCriticalSpeedAnalysis]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.CylindricalGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6594.CylindricalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CylindricalGearMeshCriticalSpeedAnalysis]

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
    ) -> "CylindricalGearMeshCompoundCriticalSpeedAnalysis._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_CylindricalGearMeshCompoundCriticalSpeedAnalysis(self)
