"""AbstractShaftOrHousingAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingAdvancedSystemDeflection")


class AbstractShaftOrHousingAdvancedSystemDeflection(
    _7298.ComponentAdvancedSystemDeflection
):
    """AbstractShaftOrHousingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingAdvancedSystemDeflection"
    )

    class _Cast_AbstractShaftOrHousingAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
            parent: "AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(_7271.AbstractShaftAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.CycloidalDiscAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.FEPartAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.ShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
        ) -> "AbstractShaftOrHousingAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftOrHousingAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingAdvancedSystemDeflection._Cast_AbstractShaftOrHousingAdvancedSystemDeflection":
        return self._Cast_AbstractShaftOrHousingAdvancedSystemDeflection(self)
