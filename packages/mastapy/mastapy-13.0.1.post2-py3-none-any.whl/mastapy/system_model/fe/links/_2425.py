"""MultiNodeFELink"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe.links import _2418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiNodeFELink"
)


__docformat__ = "restructuredtext en"
__all__ = ("MultiNodeFELink",)


Self = TypeVar("Self", bound="MultiNodeFELink")


class MultiNodeFELink(_2418.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiNodeFELink")

    class _Cast_MultiNodeFELink:
        """Special nested class for casting MultiNodeFELink to subclasses."""

        def __init__(
            self: "MultiNodeFELink._Cast_MultiNodeFELink", parent: "MultiNodeFELink"
        ):
            self._parent = parent

        @property
        def fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            return self._parent._cast(_2418.FELink)

        @property
        def electric_machine_stator_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ):
            from mastapy.system_model.fe.links import _2419

            return self._parent._cast(_2419.ElectricMachineStatorFELink)

        @property
        def gear_mesh_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2421

            return self._parent._cast(_2421.GearMeshFELink)

        @property
        def gear_with_duplicated_meshes_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ):
            from mastapy.system_model.fe.links import _2422

            return self._parent._cast(_2422.GearWithDuplicatedMeshesFELink)

        @property
        def multi_angle_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ):
            from mastapy.system_model.fe.links import _2423

            return self._parent._cast(_2423.MultiAngleConnectionFELink)

        @property
        def multi_node_connector_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2424

            return self._parent._cast(_2424.MultiNodeConnectorFELink)

        @property
        def planetary_connector_multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ):
            from mastapy.system_model.fe.links import _2426

            return self._parent._cast(_2426.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_based_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2427

            return self._parent._cast(_2427.PlanetBasedFELink)

        @property
        def planet_carrier_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2428

            return self._parent._cast(_2428.PlanetCarrierFELink)

        @property
        def point_load_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2429

            return self._parent._cast(_2429.PointLoadFELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ):
            from mastapy.system_model.fe.links import _2430

            return self._parent._cast(_2430.RollingRingConnectionFELink)

        @property
        def shaft_hub_connection_fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink"):
            from mastapy.system_model.fe.links import _2431

            return self._parent._cast(_2431.ShaftHubConnectionFELink)

        @property
        def multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "MultiNodeFELink":
            return self._parent

        def __getattr__(self: "MultiNodeFELink._Cast_MultiNodeFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiNodeFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MultiNodeFELink._Cast_MultiNodeFELink":
        return self._Cast_MultiNodeFELink(self)
