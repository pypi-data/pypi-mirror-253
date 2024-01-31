"""SuperchargerRotorSetDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET_DATABASE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("SuperchargerRotorSetDatabase",)


Self = TypeVar("Self", bound="SuperchargerRotorSetDatabase")


class SuperchargerRotorSetDatabase(_1828.NamedDatabase["_2563.SuperchargerRotorSet"]):
    """SuperchargerRotorSetDatabase

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SuperchargerRotorSetDatabase")

    class _Cast_SuperchargerRotorSetDatabase:
        """Special nested class for casting SuperchargerRotorSetDatabase to subclasses."""

        def __init__(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
            parent: "SuperchargerRotorSetDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def supercharger_rotor_set_database(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
        ) -> "SuperchargerRotorSetDatabase":
            return self._parent

        def __getattr__(
            self: "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SuperchargerRotorSetDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase":
        return self._Cast_SuperchargerRotorSetDatabase(self)
