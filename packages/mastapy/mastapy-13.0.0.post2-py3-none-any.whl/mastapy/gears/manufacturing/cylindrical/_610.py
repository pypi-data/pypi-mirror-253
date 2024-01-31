"""CylindricalCutterDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalCutterDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _713


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalCutterDatabase",)


Self = TypeVar("Self", bound="CylindricalCutterDatabase")
T = TypeVar("T", bound="_713.CylindricalGearRealCutterDesign")


class CylindricalCutterDatabase(_1828.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalCutterDatabase")

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
            parent: "CylindricalCutterDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705

            return self._parent._cast(_705.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "CylindricalCutterDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalCutterDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase":
        return self._Cast_CylindricalCutterDatabase(self)
