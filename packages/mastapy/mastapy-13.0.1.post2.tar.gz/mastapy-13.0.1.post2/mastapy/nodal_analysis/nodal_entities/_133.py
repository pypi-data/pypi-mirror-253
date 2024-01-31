"""ComponentNodalComposite"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ComponentNodalComposite"
)


__docformat__ = "restructuredtext en"
__all__ = ("ComponentNodalComposite",)


Self = TypeVar("Self", bound="ComponentNodalComposite")


class ComponentNodalComposite(_143.NodalComposite):
    """ComponentNodalComposite

    This is a mastapy class.
    """

    TYPE = _COMPONENT_NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentNodalComposite")

    class _Cast_ComponentNodalComposite:
        """Special nested class for casting ComponentNodalComposite to subclasses."""

        def __init__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
            parent: "ComponentNodalComposite",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(self: "ComponentNodalComposite._Cast_ComponentNodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _127

            return self._parent._cast(_127.BarElasticMBD)

        @property
        def bar_mbd(self: "ComponentNodalComposite._Cast_ComponentNodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarMBD)

        @property
        def bar_rigid_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarRigidMBD)

        @property
        def concentric_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.GearMeshPointOnFlankContact)

        @property
        def simple_bar(self: "ComponentNodalComposite._Cast_ComponentNodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.SimpleBar)

        @property
        def torsional_friction_node_pair(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(
                _150.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "ComponentNodalComposite":
            return self._parent

        def __getattr__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentNodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComponentNodalComposite._Cast_ComponentNodalComposite":
        return self._Cast_ComponentNodalComposite(self)
