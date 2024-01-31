"""ArbitraryNodalComponent"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ARBITRARY_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ArbitraryNodalComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("ArbitraryNodalComponent",)


Self = TypeVar("Self", bound="ArbitraryNodalComponent")


class ArbitraryNodalComponent(_142.NodalComponent):
    """ArbitraryNodalComponent

    This is a mastapy class.
    """

    TYPE = _ARBITRARY_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ArbitraryNodalComponent")

    class _Cast_ArbitraryNodalComponent:
        """Special nested class for casting ArbitraryNodalComponent to subclasses."""

        def __init__(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
            parent: "ArbitraryNodalComponent",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _131

            return self._parent._cast(_131.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.CMSNodalComponent)

        @property
        def gear_mesh_node_pair(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.LineContactStiffnessEntity)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def arbitrary_nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "ArbitraryNodalComponent":
            return self._parent

        def __getattr__(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ArbitraryNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent":
        return self._Cast_ArbitraryNodalComponent(self)
