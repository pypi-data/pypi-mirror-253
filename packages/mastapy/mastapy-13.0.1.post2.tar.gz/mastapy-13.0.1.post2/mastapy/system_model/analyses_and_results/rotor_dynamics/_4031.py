"""ShaftModalComplexShapeAtStiffness"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE_AT_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics",
    "ShaftModalComplexShapeAtStiffness",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalComplexShapeAtStiffness",)


Self = TypeVar("Self", bound="ShaftModalComplexShapeAtStiffness")


class ShaftModalComplexShapeAtStiffness(_4029.ShaftModalComplexShape):
    """ShaftModalComplexShapeAtStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE_AT_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalComplexShapeAtStiffness")

    class _Cast_ShaftModalComplexShapeAtStiffness:
        """Special nested class for casting ShaftModalComplexShapeAtStiffness to subclasses."""

        def __init__(
            self: "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness",
            parent: "ShaftModalComplexShapeAtStiffness",
        ):
            self._parent = parent

        @property
        def shaft_modal_complex_shape(
            self: "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness",
        ):
            return self._parent._cast(_4029.ShaftModalComplexShape)

        @property
        def shaft_complex_shape(
            self: "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness",
        ):
            pass

            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4027

            return self._parent._cast(_4027.ShaftComplexShape)

        @property
        def shaft_modal_complex_shape_at_stiffness(
            self: "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness",
        ) -> "ShaftModalComplexShapeAtStiffness":
            return self._parent

        def __getattr__(
            self: "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ShaftModalComplexShapeAtStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness":
        return self._Cast_ShaftModalComplexShapeAtStiffness(self)
