"""BearingAxialMountingClearance"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_AXIAL_MOUNTING_CLEARANCE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "BearingAxialMountingClearance"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingAxialMountingClearance",)


Self = TypeVar("Self", bound="BearingAxialMountingClearance")


class BearingAxialMountingClearance(_125.ArbitraryNodalComponent):
    """BearingAxialMountingClearance

    This is a mastapy class.
    """

    TYPE = _BEARING_AXIAL_MOUNTING_CLEARANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingAxialMountingClearance")

    class _Cast_BearingAxialMountingClearance:
        """Special nested class for casting BearingAxialMountingClearance to subclasses."""

        def __init__(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
            parent: "BearingAxialMountingClearance",
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ):
            return self._parent._cast(_125.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ):
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ) -> "BearingAxialMountingClearance":
            return self._parent

        def __getattr__(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingAxialMountingClearance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance":
        return self._Cast_BearingAxialMountingClearance(self)
