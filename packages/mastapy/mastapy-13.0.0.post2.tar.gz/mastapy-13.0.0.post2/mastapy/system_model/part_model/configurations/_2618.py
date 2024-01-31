"""PartDetailSelection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_DETAIL_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "PartDetailSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468


__docformat__ = "restructuredtext en"
__all__ = ("PartDetailSelection",)


Self = TypeVar("Self", bound="PartDetailSelection")
TPart = TypeVar("TPart", bound="_2468.Part")
TSelectableItem = TypeVar("TSelectableItem")


class PartDetailSelection(_0.APIBase, Generic[TPart, TSelectableItem]):
    """PartDetailSelection

    This is a mastapy class.

    Generic Types:
        TPart
        TSelectableItem
    """

    TYPE = _PART_DETAIL_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartDetailSelection")

    class _Cast_PartDetailSelection:
        """Special nested class for casting PartDetailSelection to subclasses."""

        def __init__(
            self: "PartDetailSelection._Cast_PartDetailSelection",
            parent: "PartDetailSelection",
        ):
            self._parent = parent

        @property
        def active_cylindrical_gear_set_design_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ):
            from mastapy.system_model.part_model.gears import _2510

            return self._parent._cast(_2510.ActiveCylindricalGearSetDesignSelection)

        @property
        def active_gear_set_design_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.ActiveGearSetDesignSelection)

        @property
        def active_fe_substructure_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ):
            from mastapy.system_model.part_model.configurations import _2611

            return self._parent._cast(_2611.ActiveFESubstructureSelection)

        @property
        def active_shaft_design_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ):
            from mastapy.system_model.part_model.configurations import _2613

            return self._parent._cast(_2613.ActiveShaftDesignSelection)

        @property
        def bearing_detail_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ):
            from mastapy.system_model.part_model.configurations import _2616

            return self._parent._cast(_2616.BearingDetailSelection)

        @property
        def part_detail_selection(
            self: "PartDetailSelection._Cast_PartDetailSelection",
        ) -> "PartDetailSelection":
            return self._parent

        def __getattr__(
            self: "PartDetailSelection._Cast_PartDetailSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartDetailSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def selection(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_TSelectableItem":
        """ListWithSelectedItem[TSelectableItem]"""
        temp = self.wrapped.Selection

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_TSelectableItem",
        )(temp)

    @selection.setter
    @enforce_parameter_types
    def selection(self: Self, value: "TSelectableItem"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_TSelectableItem.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_TSelectableItem.implicit_type()
        )
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.Selection = value

    @property
    def part(self: Self) -> "TPart":
        """TPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_item(self: Self) -> "TSelectableItem":
        """TSelectableItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedItem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "PartDetailSelection._Cast_PartDetailSelection":
        return self._Cast_PartDetailSelection(self)
