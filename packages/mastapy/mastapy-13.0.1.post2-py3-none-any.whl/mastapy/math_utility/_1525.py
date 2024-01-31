"""RealVector"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility import _1524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_VECTOR = python_net_import("SMT.MastaAPI.MathUtility", "RealVector")


__docformat__ = "restructuredtext en"
__all__ = ("RealVector",)


Self = TypeVar("Self", bound="RealVector")


class RealVector(_1524.RealMatrix):
    """RealVector

    This is a mastapy class.
    """

    TYPE = _REAL_VECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RealVector")

    class _Cast_RealVector:
        """Special nested class for casting RealVector to subclasses."""

        def __init__(self: "RealVector._Cast_RealVector", parent: "RealVector"):
            self._parent = parent

        @property
        def real_matrix(self: "RealVector._Cast_RealVector"):
            return self._parent._cast(_1524.RealMatrix)

        @property
        def generic_matrix(self: "RealVector._Cast_RealVector"):
            from mastapy.math_utility import _1513

            return self._parent._cast(_1513.GenericMatrix)

        @property
        def euler_parameters(self: "RealVector._Cast_RealVector"):
            from mastapy.math_utility import _1508

            return self._parent._cast(_1508.EulerParameters)

        @property
        def quaternion(self: "RealVector._Cast_RealVector"):
            from mastapy.math_utility import _1523

            return self._parent._cast(_1523.Quaternion)

        @property
        def vector_6d(self: "RealVector._Cast_RealVector"):
            from mastapy.math_utility import _1535

            return self._parent._cast(_1535.Vector6D)

        @property
        def real_vector(self: "RealVector._Cast_RealVector") -> "RealVector":
            return self._parent

        def __getattr__(self: "RealVector._Cast_RealVector", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RealVector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RealVector._Cast_RealVector":
        return self._Cast_RealVector(self)
