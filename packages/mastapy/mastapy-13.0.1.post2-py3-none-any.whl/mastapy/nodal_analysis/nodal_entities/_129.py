"""BarRigidMBD"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_RIGID_MBD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "BarRigidMBD"
)


__docformat__ = "restructuredtext en"
__all__ = ("BarRigidMBD",)


Self = TypeVar("Self", bound="BarRigidMBD")


class BarRigidMBD(_128.BarMBD):
    """BarRigidMBD

    This is a mastapy class.
    """

    TYPE = _BAR_RIGID_MBD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BarRigidMBD")

    class _Cast_BarRigidMBD:
        """Special nested class for casting BarRigidMBD to subclasses."""

        def __init__(self: "BarRigidMBD._Cast_BarRigidMBD", parent: "BarRigidMBD"):
            self._parent = parent

        @property
        def bar_mbd(self: "BarRigidMBD._Cast_BarRigidMBD"):
            return self._parent._cast(_128.BarMBD)

        @property
        def component_nodal_composite(self: "BarRigidMBD._Cast_BarRigidMBD"):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def nodal_composite(self: "BarRigidMBD._Cast_BarRigidMBD"):
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(self: "BarRigidMBD._Cast_BarRigidMBD"):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def bar_rigid_mbd(self: "BarRigidMBD._Cast_BarRigidMBD") -> "BarRigidMBD":
            return self._parent

        def __getattr__(self: "BarRigidMBD._Cast_BarRigidMBD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BarRigidMBD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BarRigidMBD._Cast_BarRigidMBD":
        return self._Cast_BarRigidMBD(self)
