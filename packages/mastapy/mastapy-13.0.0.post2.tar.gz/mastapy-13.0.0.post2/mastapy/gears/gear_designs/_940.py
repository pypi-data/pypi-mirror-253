"""BevelHypoidGearDesignSettingsDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "BevelHypoidGearDesignSettingsDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearDesignSettingsDatabase",)


Self = TypeVar("Self", bound="BevelHypoidGearDesignSettingsDatabase")


class BevelHypoidGearDesignSettingsDatabase(
    _1828.NamedDatabase["_941.BevelHypoidGearDesignSettingsItem"]
):
    """BevelHypoidGearDesignSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelHypoidGearDesignSettingsDatabase"
    )

    class _Cast_BevelHypoidGearDesignSettingsDatabase:
        """Special nested class for casting BevelHypoidGearDesignSettingsDatabase to subclasses."""

        def __init__(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
            parent: "BevelHypoidGearDesignSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
        ):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
        ):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
        ) -> "BevelHypoidGearDesignSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase",
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
        self: Self, instance_to_wrap: "BevelHypoidGearDesignSettingsDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearDesignSettingsDatabase._Cast_BevelHypoidGearDesignSettingsDatabase":
        return self._Cast_BevelHypoidGearDesignSettingsDatabase(self)
