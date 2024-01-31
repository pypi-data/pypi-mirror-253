"""PartToPartShearCouplingConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.system_deflections import _2786


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionAdvancedSystemDeflection"
)


class PartToPartShearCouplingConnectionAdvancedSystemDeflection(
    _7311.CouplingConnectionAdvancedSystemDeflection
):
    """PartToPartShearCouplingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    )

    class _Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
            parent: "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_system_deflection(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7311.CouplingConnectionAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
        ) -> "PartToPartShearCouplingConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6929.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2786.PartToPartShearCouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionAdvancedSystemDeflection._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection":
        return self._Cast_PartToPartShearCouplingConnectionAdvancedSystemDeflection(
            self
        )
