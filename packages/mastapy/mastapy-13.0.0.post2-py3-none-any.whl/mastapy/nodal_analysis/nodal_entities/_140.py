"""GearMeshSingleFlankContact"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_SINGLE_FLANK_CONTACT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "GearMeshSingleFlankContact"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshSingleFlankContact",)


Self = TypeVar("Self", bound="GearMeshSingleFlankContact")


class GearMeshSingleFlankContact(_143.NodalComposite):
    """GearMeshSingleFlankContact

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_SINGLE_FLANK_CONTACT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshSingleFlankContact")

    class _Cast_GearMeshSingleFlankContact:
        """Special nested class for casting GearMeshSingleFlankContact to subclasses."""

        def __init__(
            self: "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact",
            parent: "GearMeshSingleFlankContact",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact",
        ):
            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(
            self: "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact",
        ):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def gear_mesh_single_flank_contact(
            self: "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact",
        ) -> "GearMeshSingleFlankContact":
            return self._parent

        def __getattr__(
            self: "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshSingleFlankContact.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshSingleFlankContact._Cast_GearMeshSingleFlankContact":
        return self._Cast_GearMeshSingleFlankContact(self)
