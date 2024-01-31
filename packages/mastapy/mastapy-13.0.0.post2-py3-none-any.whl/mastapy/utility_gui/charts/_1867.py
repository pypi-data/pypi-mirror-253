"""TwoDChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility_gui.charts import _1859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_D_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "TwoDChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1853, _1863


__docformat__ = "restructuredtext en"
__all__ = ("TwoDChartDefinition",)


Self = TypeVar("Self", bound="TwoDChartDefinition")


class TwoDChartDefinition(_1859.NDChartDefinition):
    """TwoDChartDefinition

    This is a mastapy class.
    """

    TYPE = _TWO_D_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TwoDChartDefinition")

    class _Cast_TwoDChartDefinition:
        """Special nested class for casting TwoDChartDefinition to subclasses."""

        def __init__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
            parent: "TwoDChartDefinition",
        ):
            self._parent = parent

        @property
        def nd_chart_definition(self: "TwoDChartDefinition._Cast_TwoDChartDefinition"):
            return self._parent._cast(_1859.NDChartDefinition)

        @property
        def chart_definition(self: "TwoDChartDefinition._Cast_TwoDChartDefinition"):
            from mastapy.utility.report import _1748

            return self._parent._cast(_1748.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1852

            return self._parent._cast(_1852.BubbleChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1857

            return self._parent._cast(_1857.MatrixVisualisationDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1860

            return self._parent._cast(_1860.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1862

            return self._parent._cast(_1862.ScatterChartDefinition)

        @property
        def two_d_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "TwoDChartDefinition":
            return self._parent

        def __getattr__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TwoDChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def const_lines(self: Self) -> "List[_1853.ConstantLine]":
        """List[mastapy.utility_gui.charts.ConstantLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def series_list(self: Self) -> "List[_1863.Series2D]":
        """List[mastapy.utility_gui.charts.Series2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeriesList

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "TwoDChartDefinition._Cast_TwoDChartDefinition":
        return self._Cast_TwoDChartDefinition(self)
