"""ShaftSectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _126
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftSectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2802


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSectionSystemDeflection",)


Self = TypeVar("Self", bound="ShaftSectionSystemDeflection")


class ShaftSectionSystemDeflection(_126.Bar):
    """ShaftSectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSectionSystemDeflection")

    class _Cast_ShaftSectionSystemDeflection:
        """Special nested class for casting ShaftSectionSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
            parent: "ShaftSectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def bar(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ):
            return self._parent._cast(_126.Bar)

        @property
        def nodal_component(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ):
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def shaft_section_system_deflection(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ) -> "ShaftSectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSectionSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_end(self: Self) -> "_2802.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_end(self: Self) -> "_2802.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection":
        return self._Cast_ShaftSectionSystemDeflection(self)
