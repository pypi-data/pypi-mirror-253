"""APIBase"""
from __future__ import annotations

from typing import TypeVar, Type
from sys import modules

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _7552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import
from mastapy._internal.deprecation import deprecated

_API_BASE = python_net_import("SMT.MastaAPI", "APIBase")


__docformat__ = "restructuredtext en"
__all__ = ("APIBase",)


Self = TypeVar("Self", bound="APIBase")


class APIBase(_7552.MarshalByRefObjectPermanent):
    """APIBase

    This is a mastapy class.
    """

    TYPE = _API_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_APIBase")

    class _Cast_APIBase:
        """Special nested class for casting APIBase to subclasses."""

        def __init__(self: "APIBase._Cast_APIBase", parent: "APIBase"):
            self._parent = parent

        @property
        def api_base(self: "APIBase._Cast_APIBase") -> "APIBase":
            return self._parent

        def __getattr__(self: "APIBase._Cast_APIBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "APIBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def is_instance_of_wrapped_type(self: Self, type_: "type") -> "bool":
        """bool

        Args:
            type_ (type)
        """
        method_result = self.wrapped.IsInstanceOfWrappedType(type_)
        return method_result

    @enforce_parameter_types
    def set_property(self: Self, name: "str", value: "object"):
        """Method does not return.

        Args:
            name (str)
            value (object)
        """
        name = str(name)
        self.wrapped.SetProperty(name if name else "", value)

    @enforce_parameter_types
    def is_valid(self: Self, property_name: "str") -> "bool":
        """bool

        Args:
            property_name (str)
        """
        property_name = str(property_name)
        method_result = self.wrapped.IsValid(property_name if property_name else "")
        return method_result

    @enforce_parameter_types
    def is_read_only(self: Self, property_name: "str") -> "bool":
        """bool

        Args:
            property_name (str)
        """
        property_name = str(property_name)
        method_result = self.wrapped.IsReadOnly(property_name if property_name else "")
        return method_result

    def documentation_url(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.DocumentationUrl()
        return method_result

    def to_string(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToString()
        return method_result

    def __hash__(self: Self) -> "int":
        """int"""
        method_result = self.wrapped.GetHashCode()
        return method_result

    @enforce_parameter_types
    def __eq__(self: Self, other: "APIBase") -> "bool":
        """bool

        Args:
            other (mastapy.APIBase)
        """
        method_result = self.wrapped.op_Equality(
            self.wrapped, other.wrapped if other else None
        )
        return method_result

    @enforce_parameter_types
    def __ne__(self: Self, other: "APIBase") -> "bool":
        """bool

        Args:
            other (mastapy.APIBase)
        """
        method_result = self.wrapped.op_Inequality(
            self.wrapped, other.wrapped if other else None
        )
        return method_result

    T_get_property = TypeVar("T_get_property")

    def get_property(self: Self, name: str, type_: Type) -> "T_get_property":
        """Get a property from the MASTA API by name and expected return type.

        Args:
            name (str): Name of the property.
            type_ (Type): Expected return type.

        Returns:
            T_get_property
        """
        name = str(name)
        method_result = self.wrapped.GetProperty[type_](name if name else "")
        type_ = method_result.GetType()

        try:
            return (
                constructor.new(type_.Namespace, type_.Name)(method_result)
                if method_result is not None
                else None
            )
        except AttributeError:
            return method_result

    def __del__(self: Self):
        self.wrapped.reference_count -= 1
        if self.wrapped.reference_count <= 0:
            self.disconnect_from_masta()

    def disconnect_from_masta(self: Self):
        import contextlib

        with contextlib.suppress(TypeError, ImportError):
            self.wrapped.DisconnectFromMASTA()

    def _cast(self: Self, type_: Type):
        return type_(self.wrapped)

    def is_of_type(self: Self, type_: Type) -> bool:
        """Method for checking if a mastapy object can be cast to another type.

        Note:
            This method follows all standard casting rules from other languages.

        Args:
            type_ (Type): The type to check.

        Returns:
            bool
        """

        a = type(self.wrapped)
        b = getattr(modules[type_.__module__], type_.__name__).TYPE

        return b in a.__mro__

    def cast_or_none(self: Type, type_: Type):
        """Method for casting one mastapy object to another.

        Note:
            This method follows all standard casting rules from other languages.
            This method will return None if the cast fails.

        Args:
            type_ (Type): The type to cast to.
        """

        if not self.is_of_type(type_):
            return None

        return self._cast(type_)

    @deprecated('Use the "cast_to" property or "cast_or_none" function instead.')
    def cast(self: Self, type_: Type):
        """Method for casting one mastapy object to another.

        Note:
            This method follows all standard casting rules from other languages.
            This method will raise a CastException if the cast fails.

        Args:
            type_ (Type): The type to cast to.
        """
        if not self.is_of_type(type_):
            raise CastException(
                "Could not cast {} to type {}. Is it a mastapy type?".format(
                    type(self), type_
                )
            ) from None

        return self._cast(type_)

    def __str__(self: Self) -> str:
        return self.wrapped.ToString()

    def __repr__(self: Self) -> str:
        type_name = self.wrapped.GetType().Name
        part_name = self.unique_name if hasattr(self, "unique_name") else str(self)
        return f"<{type_name} : {part_name}>"

    @property
    def cast_to(self: Self) -> "APIBase._Cast_APIBase":
        return self._Cast_APIBase(self)
