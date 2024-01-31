"""NodalComponent"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodalComponent",)


Self = TypeVar("Self", bound="NodalComponent")


class NodalComponent(_144.NodalEntity):
    """NodalComponent

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComponent")

    class _Cast_NodalComponent:
        """Special nested class for casting NodalComponent to subclasses."""

        def __init__(
            self: "NodalComponent._Cast_NodalComponent", parent: "NodalComponent"
        ):
            self._parent = parent

        @property
        def nodal_entity(self: "NodalComponent._Cast_NodalComponent"):
            return self._parent._cast(_144.NodalEntity)

        @property
        def arbitrary_nodal_component(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _125

            return self._parent._cast(_125.ArbitraryNodalComponent)

        @property
        def bar(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _126

            return self._parent._cast(_126.Bar)

        @property
        def bearing_axial_mounting_clearance(
            self: "NodalComponent._Cast_NodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _131

            return self._parent._cast(_131.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.CMSNodalComponent)

        @property
        def distributed_rigid_bar_coupling(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.DistributedRigidBarCoupling)

        @property
        def friction_nodal_component(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.FrictionNodalComponent)

        @property
        def gear_mesh_node_pair(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.LineContactStiffnessEntity)

        @property
        def pid_control_nodal_component(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.PIDControlNodalComponent)

        @property
        def rigid_bar(self: "NodalComponent._Cast_NodalComponent"):
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.RigidBar)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ):
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def shaft_section_system_deflection(
            self: "NodalComponent._Cast_NodalComponent",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.ShaftSectionSystemDeflection)

        @property
        def nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "NodalComponent":
            return self._parent

        def __getattr__(self: "NodalComponent._Cast_NodalComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComponent._Cast_NodalComponent":
        return self._Cast_NodalComponent(self)
