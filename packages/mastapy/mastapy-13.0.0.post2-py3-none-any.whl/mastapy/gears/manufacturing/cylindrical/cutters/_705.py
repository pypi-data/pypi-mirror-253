"""CylindricalFormedWheelGrinderDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical import _610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_FORMED_WHEEL_GRINDER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalFormedWheelGrinderDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalFormedWheelGrinderDatabase",)


Self = TypeVar("Self", bound="CylindricalFormedWheelGrinderDatabase")


class CylindricalFormedWheelGrinderDatabase(
    _610.CylindricalCutterDatabase["_707.CylindricalGearFormGrindingWheel"]
):
    """CylindricalFormedWheelGrinderDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_FORMED_WHEEL_GRINDER_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalFormedWheelGrinderDatabase"
    )

    class _Cast_CylindricalFormedWheelGrinderDatabase:
        """Special nested class for casting CylindricalFormedWheelGrinderDatabase to subclasses."""

        def __init__(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
            parent: "CylindricalFormedWheelGrinderDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
        ):
            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
        ):
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
        ) -> "CylindricalFormedWheelGrinderDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase",
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
        self: Self, instance_to_wrap: "CylindricalFormedWheelGrinderDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalFormedWheelGrinderDatabase._Cast_CylindricalFormedWheelGrinderDatabase":
        return self._Cast_CylindricalFormedWheelGrinderDatabase(self)
