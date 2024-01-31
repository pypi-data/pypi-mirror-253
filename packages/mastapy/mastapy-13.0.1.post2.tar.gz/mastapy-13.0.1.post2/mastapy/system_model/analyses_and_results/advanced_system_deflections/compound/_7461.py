"""FaceGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7466,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "FaceGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7330,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7459,
        _7460,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearSetCompoundAdvancedSystemDeflection")


class FaceGearSetCompoundAdvancedSystemDeflection(
    _7466.GearSetCompoundAdvancedSystemDeflection
):
    """FaceGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_FaceGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting FaceGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
            parent: "FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "FaceGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "FaceGearSetCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7330.FaceGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7459.FaceGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7460.FaceGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7330.FaceGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_FaceGearSetCompoundAdvancedSystemDeflection(self)
