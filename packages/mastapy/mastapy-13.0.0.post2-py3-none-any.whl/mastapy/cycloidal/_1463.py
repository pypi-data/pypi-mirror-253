"""RingPinsMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.materials import _270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Cycloidal", "RingPinsMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsMaterialDatabase",)


Self = TypeVar("Self", bound="RingPinsMaterialDatabase")


class RingPinsMaterialDatabase(_270.MaterialDatabase["_1462.RingPinsMaterial"]):
    """RingPinsMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsMaterialDatabase")

    class _Cast_RingPinsMaterialDatabase:
        """Special nested class for casting RingPinsMaterialDatabase to subclasses."""

        def __init__(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase",
            parent: "RingPinsMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase",
        ):
            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def ring_pins_material_database(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase",
        ) -> "RingPinsMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsMaterialDatabase._Cast_RingPinsMaterialDatabase":
        return self._Cast_RingPinsMaterialDatabase(self)
