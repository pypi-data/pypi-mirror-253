"""RealMatrix"""
from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.math_utility import _1513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_MATRIX = python_net_import("SMT.MastaAPI.MathUtility", "RealMatrix")


__docformat__ = "restructuredtext en"
__all__ = ("RealMatrix",)


Self = TypeVar("Self", bound="RealMatrix")


class RealMatrix(_1513.GenericMatrix[float, "RealMatrix"]):
    """RealMatrix

    This is a mastapy class.
    """

    TYPE = _REAL_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RealMatrix")

    class _Cast_RealMatrix:
        """Special nested class for casting RealMatrix to subclasses."""

        def __init__(self: "RealMatrix._Cast_RealMatrix", parent: "RealMatrix"):
            self._parent = parent

        @property
        def generic_matrix(self: "RealMatrix._Cast_RealMatrix"):
            pass

            return self._parent._cast(_1513.GenericMatrix)

        @property
        def euler_parameters(self: "RealMatrix._Cast_RealMatrix"):
            from mastapy.math_utility import _1508

            return self._parent._cast(_1508.EulerParameters)

        @property
        def quaternion(self: "RealMatrix._Cast_RealMatrix"):
            from mastapy.math_utility import _1523

            return self._parent._cast(_1523.Quaternion)

        @property
        def real_vector(self: "RealMatrix._Cast_RealMatrix"):
            from mastapy.math_utility import _1525

            return self._parent._cast(_1525.RealVector)

        @property
        def square_matrix(self: "RealMatrix._Cast_RealMatrix"):
            from mastapy.math_utility import _1530

            return self._parent._cast(_1530.SquareMatrix)

        @property
        def vector_6d(self: "RealMatrix._Cast_RealMatrix"):
            from mastapy.math_utility import _1535

            return self._parent._cast(_1535.Vector6D)

        @property
        def real_matrix(self: "RealMatrix._Cast_RealMatrix") -> "RealMatrix":
            return self._parent

        def __getattr__(self: "RealMatrix._Cast_RealMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RealMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def get_column_at(self: Self, index: "int") -> "List[float]":
        """List[float]

        Args:
            index (int)
        """
        index = int(index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetColumnAt(index if index else 0), float
        )

    @enforce_parameter_types
    def get_row_at(self: Self, index: "int") -> "List[float]":
        """List[float]

        Args:
            index (int)
        """
        index = int(index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetRowAt(index if index else 0), float
        )

    @property
    def cast_to(self: Self) -> "RealMatrix._Cast_RealMatrix":
        return self._Cast_RealMatrix(self)
