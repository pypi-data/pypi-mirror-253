"""CylindricalGearDesignAndRatingSettingsDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical",
    "CylindricalGearDesignAndRatingSettingsDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignAndRatingSettingsDatabase",)


Self = TypeVar("Self", bound="CylindricalGearDesignAndRatingSettingsDatabase")


class CylindricalGearDesignAndRatingSettingsDatabase(
    _1828.NamedDatabase["_454.CylindricalGearDesignAndRatingSettingsItem"]
):
    """CylindricalGearDesignAndRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearDesignAndRatingSettingsDatabase"
    )

    class _Cast_CylindricalGearDesignAndRatingSettingsDatabase:
        """Special nested class for casting CylindricalGearDesignAndRatingSettingsDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
            parent: "CylindricalGearDesignAndRatingSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
        ) -> "CylindricalGearDesignAndRatingSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase",
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
        instance_to_wrap: "CylindricalGearDesignAndRatingSettingsDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase":
        return self._Cast_CylindricalGearDesignAndRatingSettingsDatabase(self)
