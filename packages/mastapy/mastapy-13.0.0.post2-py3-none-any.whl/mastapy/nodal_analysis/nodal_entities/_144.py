"""NodalEntity"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalEntity"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodalEntity",)


Self = TypeVar("Self", bound="NodalEntity")


class NodalEntity(_0.APIBase):
    """NodalEntity

    This is a mastapy class.
    """

    TYPE = _NODAL_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalEntity")

    class _Cast_NodalEntity:
        """Special nested class for casting NodalEntity to subclasses."""

        def __init__(self: "NodalEntity._Cast_NodalEntity", parent: "NodalEntity"):
            self._parent = parent

        @property
        def arbitrary_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _125

            return self._parent._cast(_125.ArbitraryNodalComponent)

        @property
        def bar(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _126

            return self._parent._cast(_126.Bar)

        @property
        def bar_elastic_mbd(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _127

            return self._parent._cast(_127.BarElasticMBD)

        @property
        def bar_mbd(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarMBD)

        @property
        def bar_rigid_mbd(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarRigidMBD)

        @property
        def bearing_axial_mounting_clearance(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _131

            return self._parent._cast(_131.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.CMSNodalComponent)

        @property
        def component_nodal_composite(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ):
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ConcentricConnectionNodalComponent)

        @property
        def distributed_rigid_bar_coupling(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.DistributedRigidBarCoupling)

        @property
        def friction_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.FrictionNodalComponent)

        @property
        def gear_mesh_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.GearMeshNodalComponent)

        @property
        def gear_mesh_node_pair(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.GearMeshNodePair)

        @property
        def gear_mesh_point_on_flank_contact(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _140

            return self._parent._cast(_140.GearMeshSingleFlankContact)

        @property
        def line_contact_stiffness_entity(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.LineContactStiffnessEntity)

        @property
        def nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_composite(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.NodalComposite)

        @property
        def pid_control_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.PIDControlNodalComponent)

        @property
        def rigid_bar(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.RigidBar)

        @property
        def simple_bar(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.SimpleBar)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ):
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def torsional_friction_node_pair(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "NodalEntity._Cast_NodalEntity",
        ):
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(
                _150.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def shaft_section_system_deflection(self: "NodalEntity._Cast_NodalEntity"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.ShaftSectionSystemDeflection)

        @property
        def nodal_entity(self: "NodalEntity._Cast_NodalEntity") -> "NodalEntity":
            return self._parent

        def __getattr__(self: "NodalEntity._Cast_NodalEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "NodalEntity._Cast_NodalEntity":
        return self._Cast_NodalEntity(self)
