"""CylindricalGearMeshSystemDeflectionWithLTCAResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _857


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshSystemDeflectionWithLTCAResults",)


Self = TypeVar("Self", bound="CylindricalGearMeshSystemDeflectionWithLTCAResults")


class CylindricalGearMeshSystemDeflectionWithLTCAResults(
    _2739.CylindricalGearMeshSystemDeflection
):
    """CylindricalGearMeshSystemDeflectionWithLTCAResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults"
    )

    class _Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults:
        """Special nested class for casting CylindricalGearMeshSystemDeflectionWithLTCAResults to subclasses."""

        def __init__(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
            parent: "CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            return self._parent._cast(_2739.CylindricalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
        ) -> "CylindricalGearMeshSystemDeflectionWithLTCAResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults",
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
        instance_to_wrap: "CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_ltca_results(
        self: Self,
    ) -> "_857.CylindricalGearMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def advanced_ltca_results_only_first_planetary_mesh(
        self: Self,
    ) -> "_857.CylindricalGearMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def basic_ltca_results(
        self: Self,
    ) -> "_857.CylindricalGearMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def basic_ltca_results_only_first_planetary_mesh(
        self: Self,
    ) -> "_857.CylindricalGearMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshSystemDeflectionWithLTCAResults._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults":
        return self._Cast_CylindricalGearMeshSystemDeflectionWithLTCAResults(self)
