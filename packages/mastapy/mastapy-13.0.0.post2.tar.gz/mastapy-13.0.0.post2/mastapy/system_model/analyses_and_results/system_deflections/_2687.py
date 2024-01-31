"""AbstractShaftSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.power_flows import _4034


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftSystemDeflection")


class AbstractShaftSystemDeflection(_2686.AbstractShaftOrHousingSystemDeflection):
    """AbstractShaftSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftSystemDeflection")

    class _Cast_AbstractShaftSystemDeflection:
        """Special nested class for casting AbstractShaftSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            parent: "AbstractShaftSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            return self._parent._cast(_2686.AbstractShaftOrHousingSystemDeflection)

        @property
        def component_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CycloidalDiscSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.ShaftSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "AbstractShaftSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2435.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4034.AbstractShaftPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection":
        return self._Cast_AbstractShaftSystemDeflection(self)
