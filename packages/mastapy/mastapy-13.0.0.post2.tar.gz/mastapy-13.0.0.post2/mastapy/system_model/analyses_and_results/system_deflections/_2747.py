"""CylindricalGearSystemDeflectionWithLTCAResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSystemDeflectionWithLTCAResults",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _856


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSystemDeflectionWithLTCAResults",)


Self = TypeVar("Self", bound="CylindricalGearSystemDeflectionWithLTCAResults")


class CylindricalGearSystemDeflectionWithLTCAResults(
    _2745.CylindricalGearSystemDeflection
):
    """CylindricalGearSystemDeflectionWithLTCAResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSystemDeflectionWithLTCAResults"
    )

    class _Cast_CylindricalGearSystemDeflectionWithLTCAResults:
        """Special nested class for casting CylindricalGearSystemDeflectionWithLTCAResults to subclasses."""

        def __init__(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
            parent: "CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            return self._parent._cast(_2745.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.CylindricalPlanetGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
        ) -> "CylindricalGearSystemDeflectionWithLTCAResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults",
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
        instance_to_wrap: "CylindricalGearSystemDeflectionWithLTCAResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_ltca_results(
        self: Self,
    ) -> "_856.CylindricalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSystemDeflectionWithLTCAResults._Cast_CylindricalGearSystemDeflectionWithLTCAResults":
        return self._Cast_CylindricalGearSystemDeflectionWithLTCAResults(self)
