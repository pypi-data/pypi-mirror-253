"""GearMeshPointOnFlankContact"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_POINT_ON_FLANK_CONTACT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "GearMeshPointOnFlankContact"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshPointOnFlankContact",)


Self = TypeVar("Self", bound="GearMeshPointOnFlankContact")


class GearMeshPointOnFlankContact(_151.TwoBodyConnectionNodalComponent):
    """GearMeshPointOnFlankContact

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_POINT_ON_FLANK_CONTACT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshPointOnFlankContact")

    class _Cast_GearMeshPointOnFlankContact:
        """Special nested class for casting GearMeshPointOnFlankContact to subclasses."""

        def __init__(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
            parent: "GearMeshPointOnFlankContact",
        ):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
        ):
            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
        ):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
        ):
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
        ):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
        ) -> "GearMeshPointOnFlankContact":
            return self._parent

        def __getattr__(
            self: "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshPointOnFlankContact.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshPointOnFlankContact._Cast_GearMeshPointOnFlankContact":
        return self._Cast_GearMeshPointOnFlankContact(self)
