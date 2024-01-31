"""CylindricalGearGrindingWorm"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_GRINDING_WORM = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearGrindingWorm",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _730, _728


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearGrindingWorm",)


Self = TypeVar("Self", bound="CylindricalGearGrindingWorm")


class CylindricalGearGrindingWorm(_712.CylindricalGearRackDesign):
    """CylindricalGearGrindingWorm

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_GRINDING_WORM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearGrindingWorm")

    class _Cast_CylindricalGearGrindingWorm:
        """Special nested class for casting CylindricalGearGrindingWorm to subclasses."""

        def __init__(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
            parent: "CylindricalGearGrindingWorm",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_rack_design(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
        ):
            return self._parent._cast(_712.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _706

            return self._parent._cast(_706.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
        ):
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def cylindrical_gear_grinding_worm(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
        ) -> "CylindricalGearGrindingWorm":
            return self._parent

        def __getattr__(
            self: "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearGrindingWorm.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edge_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @edge_height.setter
    @enforce_parameter_types
    def edge_height(self: Self, value: "float"):
        self.wrapped.EdgeHeight = float(value) if value is not None else 0.0

    @property
    def flat_tip_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @flat_tip_width.setter
    @enforce_parameter_types
    def flat_tip_width(self: Self, value: "float"):
        self.wrapped.FlatTipWidth = float(value) if value is not None else 0.0

    @property
    def has_tolerances(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    @enforce_parameter_types
    def has_tolerances(self: Self, value: "bool"):
        self.wrapped.HasTolerances = bool(value) if value is not None else False

    @property
    def nominal_rack_shape(self: Self) -> "_730.RackShape":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.RackShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalRackShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def nominal_worm_grinder_shape(
        self: Self,
    ) -> "_728.CylindricalGearWormGrinderShape":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CylindricalGearWormGrinderShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalWormGrinderShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearGrindingWorm._Cast_CylindricalGearGrindingWorm":
        return self._Cast_CylindricalGearGrindingWorm(self)
