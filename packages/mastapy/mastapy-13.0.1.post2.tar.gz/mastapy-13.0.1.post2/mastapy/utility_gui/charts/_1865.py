"""ThreeDChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import _1859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_D_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ThreeDChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1743
    from mastapy.math_utility import _1488
    from mastapy.utility_gui.charts import _1861


__docformat__ = "restructuredtext en"
__all__ = ("ThreeDChartDefinition",)


Self = TypeVar("Self", bound="ThreeDChartDefinition")


class ThreeDChartDefinition(_1859.NDChartDefinition):
    """ThreeDChartDefinition

    This is a mastapy class.
    """

    TYPE = _THREE_D_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThreeDChartDefinition")

    class _Cast_ThreeDChartDefinition:
        """Special nested class for casting ThreeDChartDefinition to subclasses."""

        def __init__(
            self: "ThreeDChartDefinition._Cast_ThreeDChartDefinition",
            parent: "ThreeDChartDefinition",
        ):
            self._parent = parent

        @property
        def nd_chart_definition(
            self: "ThreeDChartDefinition._Cast_ThreeDChartDefinition",
        ):
            return self._parent._cast(_1859.NDChartDefinition)

        @property
        def chart_definition(self: "ThreeDChartDefinition._Cast_ThreeDChartDefinition"):
            from mastapy.utility.report import _1748

            return self._parent._cast(_1748.ChartDefinition)

        @property
        def three_d_chart_definition(
            self: "ThreeDChartDefinition._Cast_ThreeDChartDefinition",
        ) -> "ThreeDChartDefinition":
            return self._parent

        def __getattr__(
            self: "ThreeDChartDefinition._Cast_ThreeDChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThreeDChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def z_axis(self: Self) -> "_1743.AxisSettings":
        """mastapy.utility.report.AxisSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def x_axis_range(self: Self) -> "_1488.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.XAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @x_axis_range.setter
    @enforce_parameter_types
    def x_axis_range(self: Self, value: "_1488.Range"):
        self.wrapped.XAxisRange = value.wrapped

    @property
    def y_axis_range(self: Self) -> "_1488.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.YAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @y_axis_range.setter
    @enforce_parameter_types
    def y_axis_range(self: Self, value: "_1488.Range"):
        self.wrapped.YAxisRange = value.wrapped

    @property
    def z_axis_range(self: Self) -> "_1488.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.ZAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @z_axis_range.setter
    @enforce_parameter_types
    def z_axis_range(self: Self, value: "_1488.Range"):
        self.wrapped.ZAxisRange = value.wrapped

    def data_points_for_surfaces(self: Self) -> "List[_1861.PointsForSurface]":
        """List[mastapy.utility_gui.charts.PointsForSurface]"""
        return conversion.pn_to_mp_objects_in_list(self.wrapped.DataPointsForSurfaces())

    @property
    def cast_to(self: Self) -> "ThreeDChartDefinition._Cast_ThreeDChartDefinition":
        return self._Cast_ThreeDChartDefinition(self)
