"""CompoundAdvancedSystemDeflectionSubAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("CompoundAdvancedSystemDeflectionSubAnalysis",)


Self = TypeVar("Self", bound="CompoundAdvancedSystemDeflectionSubAnalysis")


class CompoundAdvancedSystemDeflectionSubAnalysis(_2619.CompoundAnalysis):
    """CompoundAdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundAdvancedSystemDeflectionSubAnalysis"
    )

    class _Cast_CompoundAdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting CompoundAdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(
            self: "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis",
            parent: "CompoundAdvancedSystemDeflectionSubAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis",
        ):
            return self._parent._cast(_2619.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_system_deflection_sub_analysis(
            self: "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis",
        ) -> "CompoundAdvancedSystemDeflectionSubAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis",
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
        self: Self, instance_to_wrap: "CompoundAdvancedSystemDeflectionSubAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis":
        return self._Cast_CompoundAdvancedSystemDeflectionSubAnalysis(self)
