"""CylindricalGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.gears.rating.cylindrical import _460
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7322,
        _7324,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearAdvancedSystemDeflection")


class CylindricalGearAdvancedSystemDeflection(_7333.GearAdvancedSystemDeflection):
    """CylindricalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
            parent: "CylindricalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(
                _7325.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "CylindricalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_principal_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_principal_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressTension

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressTension

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2525.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_460.CylindricalGearRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6862.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_advanced_system_deflection_meshes(
        self: Self,
    ) -> "List[_7322.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_advanced_system_deflections_in_meshes(
        self: Self,
    ) -> "List[_7324.CylindricalMeshedGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalMeshedGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionsInMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshed_gear_advanced_system_deflections(
        self: Self,
    ) -> "List[_7324.CylindricalMeshedGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalMeshedGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshedGearAdvancedSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection":
        return self._Cast_CylindricalGearAdvancedSystemDeflection(self)
