"""CouplingConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2729


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundSystemDeflection")


class CouplingConnectionCompoundSystemDeflection(
    _2917.InterMountableComponentConnectionCompoundSystemDeflection
):
    """CouplingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundSystemDeflection"
    )

    class _Cast_CouplingConnectionCompoundSystemDeflection:
        """Special nested class for casting CouplingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
            parent: "CouplingConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2917.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ClutchConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(
                _2878.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(
                _2933.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(
                _2956.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "CouplingConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2729.CouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection]

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
    ) -> "List[_2729.CouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection]

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
    ) -> "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection":
        return self._Cast_CouplingConnectionCompoundSystemDeflection(self)
