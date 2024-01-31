"""CylindricalGearFEModel"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.gears.fe_model import _1197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Cylindrical", "CylindricalGearFEModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFEModel",)


Self = TypeVar("Self", bound="CylindricalGearFEModel")


class CylindricalGearFEModel(_1197.GearFEModel):
    """CylindricalGearFEModel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFEModel")

    class _Cast_CylindricalGearFEModel:
        """Special nested class for casting CylindricalGearFEModel to subclasses."""

        def __init__(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel",
            parent: "CylindricalGearFEModel",
        ):
            self._parent = parent

        @property
        def gear_fe_model(self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel"):
            return self._parent._cast(_1197.GearFEModel)

        @property
        def gear_implementation_detail(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel",
        ):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def cylindrical_gear_fe_model(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel",
        ) -> "CylindricalGearFEModel":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFEModel._Cast_CylindricalGearFEModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def thickness_for_analyses(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ThicknessForAnalyses

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @thickness_for_analyses.setter
    @enforce_parameter_types
    def thickness_for_analyses(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ThicknessForAnalyses = value

    @property
    def use_specified_web(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSpecifiedWeb

        if temp is None:
            return False

        return temp

    @use_specified_web.setter
    @enforce_parameter_types
    def use_specified_web(self: Self, value: "bool"):
        self.wrapped.UseSpecifiedWeb = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CylindricalGearFEModel._Cast_CylindricalGearFEModel":
        return self._Cast_CylindricalGearFEModel(self)
