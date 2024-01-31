"""TorsionalFrictionNodePairSimpleLockedStiffness"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities",
    "TorsionalFrictionNodePairSimpleLockedStiffness",
)


__docformat__ = "restructuredtext en"
__all__ = ("TorsionalFrictionNodePairSimpleLockedStiffness",)


Self = TypeVar("Self", bound="TorsionalFrictionNodePairSimpleLockedStiffness")


class TorsionalFrictionNodePairSimpleLockedStiffness(_149.TorsionalFrictionNodePair):
    """TorsionalFrictionNodePairSimpleLockedStiffness

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorsionalFrictionNodePairSimpleLockedStiffness"
    )

    class _Cast_TorsionalFrictionNodePairSimpleLockedStiffness:
        """Special nested class for casting TorsionalFrictionNodePairSimpleLockedStiffness to subclasses."""

        def __init__(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
            parent: "TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            self._parent = parent

        @property
        def torsional_friction_node_pair(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            return self._parent._cast(_149.TorsionalFrictionNodePair)

        @property
        def concentric_connection_nodal_component(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ConcentricConnectionNodalComponent)

        @property
        def two_body_connection_nodal_component(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "TorsionalFrictionNodePairSimpleLockedStiffness":
            return self._parent

        def __getattr__(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
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
        self: Self,
        instance_to_wrap: "TorsionalFrictionNodePairSimpleLockedStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness":
        return self._Cast_TorsionalFrictionNodePairSimpleLockedStiffness(self)
