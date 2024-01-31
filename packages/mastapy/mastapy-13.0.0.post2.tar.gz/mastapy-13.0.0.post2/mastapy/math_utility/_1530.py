"""SquareMatrix"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility import _1524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQUARE_MATRIX = python_net_import("SMT.MastaAPI.MathUtility", "SquareMatrix")


__docformat__ = "restructuredtext en"
__all__ = ("SquareMatrix",)


Self = TypeVar("Self", bound="SquareMatrix")


class SquareMatrix(_1524.RealMatrix):
    """SquareMatrix

    This is a mastapy class.
    """

    TYPE = _SQUARE_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SquareMatrix")

    class _Cast_SquareMatrix:
        """Special nested class for casting SquareMatrix to subclasses."""

        def __init__(self: "SquareMatrix._Cast_SquareMatrix", parent: "SquareMatrix"):
            self._parent = parent

        @property
        def real_matrix(self: "SquareMatrix._Cast_SquareMatrix"):
            return self._parent._cast(_1524.RealMatrix)

        @property
        def generic_matrix(self: "SquareMatrix._Cast_SquareMatrix"):
            from mastapy.math_utility import _1513

            return self._parent._cast(_1513.GenericMatrix)

        @property
        def square_matrix(self: "SquareMatrix._Cast_SquareMatrix") -> "SquareMatrix":
            return self._parent

        def __getattr__(self: "SquareMatrix._Cast_SquareMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SquareMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SquareMatrix._Cast_SquareMatrix":
        return self._Cast_SquareMatrix(self)
