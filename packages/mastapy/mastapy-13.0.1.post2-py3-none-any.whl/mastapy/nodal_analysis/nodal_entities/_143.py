"""NodalComposite"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComposite"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodalComposite",)


Self = TypeVar("Self", bound="NodalComposite")


class NodalComposite(_144.NodalEntity):
    """NodalComposite

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComposite")

    class _Cast_NodalComposite:
        """Special nested class for casting NodalComposite to subclasses."""

        def __init__(
            self: "NodalComposite._Cast_NodalComposite", parent: "NodalComposite"
        ):
            self._parent = parent

        @property
        def nodal_entity(self: "NodalComposite._Cast_NodalComposite"):
            return self._parent._cast(_144.NodalEntity)

        @property
        def bar_elastic_mbd(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _127

            return self._parent._cast(_127.BarElasticMBD)

        @property
        def bar_mbd(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarMBD)

        @property
        def bar_rigid_mbd(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarRigidMBD)

        @property
        def component_nodal_composite(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_nodal_component(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.GearMeshNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "NodalComposite._Cast_NodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _140

            return self._parent._cast(_140.GearMeshSingleFlankContact)

        @property
        def simple_bar(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.SimpleBar)

        @property
        def torsional_friction_node_pair(self: "NodalComposite._Cast_NodalComposite"):
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "NodalComposite._Cast_NodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(
                _150.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ):
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def nodal_composite(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "NodalComposite":
            return self._parent

        def __getattr__(self: "NodalComposite._Cast_NodalComposite", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComposite._Cast_NodalComposite":
        return self._Cast_NodalComposite(self)
