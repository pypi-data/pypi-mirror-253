"""MaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_DATABASE = python_net_import("SMT.MastaAPI.Materials", "MaterialDatabase")

if TYPE_CHECKING:
    from mastapy.materials import _269


__docformat__ = "restructuredtext en"
__all__ = ("MaterialDatabase",)


Self = TypeVar("Self", bound="MaterialDatabase")
T = TypeVar("T", bound="_269.Material")


class MaterialDatabase(_1828.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialDatabase")

    class _Cast_MaterialDatabase:
        """Special nested class for casting MaterialDatabase to subclasses."""

        def __init__(
            self: "MaterialDatabase._Cast_MaterialDatabase", parent: "MaterialDatabase"
        ):
            self._parent = parent

        @property
        def named_database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def shaft_material_database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _584

            return self._parent._cast(_584.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.BevelGearISOMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearPlasticMaterialDatabase)

        @property
        def magnet_material_database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            from mastapy.electric_machines import _1283

            return self._parent._cast(_1283.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.electric_machines import _1301

            return self._parent._cast(_1301.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self: "MaterialDatabase._Cast_MaterialDatabase"):
            from mastapy.electric_machines import _1314

            return self._parent._cast(_1314.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.cycloidal import _1456

            return self._parent._cast(_1456.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ):
            from mastapy.cycloidal import _1463

            return self._parent._cast(_1463.RingPinsMaterialDatabase)

        @property
        def material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "MaterialDatabase":
            return self._parent

        def __getattr__(self: "MaterialDatabase._Cast_MaterialDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MaterialDatabase._Cast_MaterialDatabase":
        return self._Cast_MaterialDatabase(self)
