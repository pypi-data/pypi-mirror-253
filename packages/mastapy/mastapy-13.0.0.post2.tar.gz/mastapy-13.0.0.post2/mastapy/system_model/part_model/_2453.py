"""FEPart"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2383
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2436
from mastapy._internal.cast_exception import CastException

_STRING = python_net_import("System", "String")
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")

if TYPE_CHECKING:
    from mastapy.math_utility import _1498


__docformat__ = "restructuredtext en"
__all__ = ("FEPart",)


Self = TypeVar("Self", bound="FEPart")


class FEPart(_2436.AbstractShaftOrHousing):
    """FEPart

    This is a mastapy class.
    """

    TYPE = _FE_PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPart")

    class _Cast_FEPart:
        """Special nested class for casting FEPart to subclasses."""

        def __init__(self: "FEPart._Cast_FEPart", parent: "FEPart"):
            self._parent = parent

        @property
        def abstract_shaft_or_housing(self: "FEPart._Cast_FEPart"):
            return self._parent._cast(_2436.AbstractShaftOrHousing)

        @property
        def component(self: "FEPart._Cast_FEPart"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "FEPart._Cast_FEPart"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "FEPart._Cast_FEPart"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def fe_part(self: "FEPart._Cast_FEPart") -> "FEPart":
            return self._parent

        def __getattr__(self: "FEPart._Cast_FEPart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def three_d_node_size(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThreeDNodeSize

        if temp is None:
            return 0.0

        return temp

    @three_d_node_size.setter
    @enforce_parameter_types
    def three_d_node_size(self: Self, value: "float"):
        self.wrapped.ThreeDNodeSize = float(value) if value is not None else 0.0

    @property
    def default_fe_substructure(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FESubstructure":
        """ListWithSelectedItem[mastapy.system_model.fe.FESubstructure]"""
        temp = self.wrapped.DefaultFESubstructure

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FESubstructure",
        )(temp)

    @default_fe_substructure.setter
    @enforce_parameter_types
    def default_fe_substructure(self: Self, value: "_2383.FESubstructure"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DefaultFESubstructure = value

    @property
    def knows_scalar_mass(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KnowsScalarMass

        if temp is None:
            return False

        return temp

    @property
    def local_coordinate_system(self: Self) -> "_1498.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_fe_substructure(self: Self) -> "_2383.FESubstructure":
        """mastapy.system_model.fe.FESubstructure"""
        method_result = self.wrapped.CreateFESubstructure()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_fe_substructure_with_name(
        self: Self, name: "str"
    ) -> "_2383.FESubstructure":
        """mastapy.system_model.fe.FESubstructure

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.CreateFESubstructure.Overloads[_STRING](
            name if name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_fe_substructure(
        self: Self, fe_substructure: "_2383.FESubstructure"
    ) -> "bool":
        """bool

        Args:
            fe_substructure (mastapy.system_model.fe.FESubstructure)
        """
        method_result = self.wrapped.RemoveFESubstructure(
            fe_substructure.wrapped if fe_substructure else None
        )
        return method_result

    @enforce_parameter_types
    def select_fe_substructure(self: Self, fe_substructure: "_2383.FESubstructure"):
        """Method does not return.

        Args:
            fe_substructure (mastapy.system_model.fe.FESubstructure)
        """
        self.wrapped.SelectFESubstructure(
            fe_substructure.wrapped if fe_substructure else None
        )

    @property
    def cast_to(self: Self) -> "FEPart._Cast_FEPart":
        return self._Cast_FEPart(self)
