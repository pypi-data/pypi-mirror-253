"""CylindricalHobDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical import _610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_HOB_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalHobDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalHobDatabase",)


Self = TypeVar("Self", bound="CylindricalHobDatabase")


class CylindricalHobDatabase(
    _610.CylindricalCutterDatabase["_709.CylindricalGearHobDesign"]
):
    """CylindricalHobDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_HOB_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalHobDatabase")

    class _Cast_CylindricalHobDatabase:
        """Special nested class for casting CylindricalHobDatabase to subclasses."""

        def __init__(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
            parent: "CylindricalHobDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ):
            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def named_database(self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase"):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase"):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "CylindricalHobDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalHobDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalHobDatabase._Cast_CylindricalHobDatabase":
        return self._Cast_CylindricalHobDatabase(self)
