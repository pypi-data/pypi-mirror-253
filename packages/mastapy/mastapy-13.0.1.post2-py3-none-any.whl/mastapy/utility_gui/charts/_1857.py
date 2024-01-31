"""MatrixVisualisationDefinition"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui.charts import _1867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATRIX_VISUALISATION_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "MatrixVisualisationDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("MatrixVisualisationDefinition",)


Self = TypeVar("Self", bound="MatrixVisualisationDefinition")


class MatrixVisualisationDefinition(_1867.TwoDChartDefinition):
    """MatrixVisualisationDefinition

    This is a mastapy class.
    """

    TYPE = _MATRIX_VISUALISATION_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MatrixVisualisationDefinition")

    class _Cast_MatrixVisualisationDefinition:
        """Special nested class for casting MatrixVisualisationDefinition to subclasses."""

        def __init__(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
            parent: "MatrixVisualisationDefinition",
        ):
            self._parent = parent

        @property
        def two_d_chart_definition(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
        ):
            return self._parent._cast(_1867.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
        ):
            from mastapy.utility_gui.charts import _1859

            return self._parent._cast(_1859.NDChartDefinition)

        @property
        def chart_definition(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
        ):
            from mastapy.utility.report import _1748

            return self._parent._cast(_1748.ChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
        ) -> "MatrixVisualisationDefinition":
            return self._parent

        def __getattr__(
            self: "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MatrixVisualisationDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MatrixVisualisationDefinition._Cast_MatrixVisualisationDefinition":
        return self._Cast_MatrixVisualisationDefinition(self)
