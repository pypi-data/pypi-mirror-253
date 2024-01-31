"""ChartDefinition"""
from __future__ import annotations

from typing import TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CHART_DEFINITION = python_net_import("SMT.MastaAPI.Utility.Report", "ChartDefinition")


__docformat__ = "restructuredtext en"
__all__ = ("ChartDefinition",)


Self = TypeVar("Self", bound="ChartDefinition")


class ChartDefinition(_0.APIBase):
    """ChartDefinition

    This is a mastapy class.
    """

    TYPE = _CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ChartDefinition")

    class _Cast_ChartDefinition:
        """Special nested class for casting ChartDefinition to subclasses."""

        def __init__(
            self: "ChartDefinition._Cast_ChartDefinition", parent: "ChartDefinition"
        ):
            self._parent = parent

        @property
        def simple_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility.report import _1786

            return self._parent._cast(_1786.SimpleChartDefinition)

        @property
        def bubble_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility_gui.charts import _1852

            return self._parent._cast(_1852.BubbleChartDefinition)

        @property
        def legacy_chart_math_chart_definition(
            self: "ChartDefinition._Cast_ChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1856

            return self._parent._cast(_1856.LegacyChartMathChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "ChartDefinition._Cast_ChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1857

            return self._parent._cast(_1857.MatrixVisualisationDefinition)

        @property
        def nd_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility_gui.charts import _1859

            return self._parent._cast(_1859.NDChartDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "ChartDefinition._Cast_ChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1860

            return self._parent._cast(_1860.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.ScatterChartDefinition)

        @property
        def three_d_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility_gui.charts import _1865

            return self._parent._cast(_1865.ThreeDChartDefinition)

        @property
        def three_d_vector_chart_definition(
            self: "ChartDefinition._Cast_ChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1866

            return self._parent._cast(_1866.ThreeDVectorChartDefinition)

        @property
        def two_d_chart_definition(self: "ChartDefinition._Cast_ChartDefinition"):
            from mastapy.utility_gui.charts import _1867

            return self._parent._cast(_1867.TwoDChartDefinition)

        @property
        def chart_definition(
            self: "ChartDefinition._Cast_ChartDefinition",
        ) -> "ChartDefinition":
            return self._parent

        def __getattr__(self: "ChartDefinition._Cast_ChartDefinition", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def to_bitmap(self: Self) -> "Image":
        """Image"""
        return conversion.pn_to_mp_smt_bitmap(self.wrapped.ToBitmap())

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
    def cast_to(self: Self) -> "ChartDefinition._Cast_ChartDefinition":
        return self._Cast_ChartDefinition(self)
