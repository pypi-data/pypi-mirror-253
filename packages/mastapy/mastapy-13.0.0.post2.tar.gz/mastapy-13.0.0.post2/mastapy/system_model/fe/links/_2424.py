"""MultiNodeConnectorFELink"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe.links import _2425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_CONNECTOR_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiNodeConnectorFELink"
)


__docformat__ = "restructuredtext en"
__all__ = ("MultiNodeConnectorFELink",)


Self = TypeVar("Self", bound="MultiNodeConnectorFELink")


class MultiNodeConnectorFELink(_2425.MultiNodeFELink):
    """MultiNodeConnectorFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_CONNECTOR_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiNodeConnectorFELink")

    class _Cast_MultiNodeConnectorFELink:
        """Special nested class for casting MultiNodeConnectorFELink to subclasses."""

        def __init__(
            self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink",
            parent: "MultiNodeConnectorFELink",
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(
            self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink",
        ):
            return self._parent._cast(_2425.MultiNodeFELink)

        @property
        def fe_link(self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink"):
            from mastapy.system_model.fe.links import _2418

            return self._parent._cast(_2418.FELink)

        @property
        def shaft_hub_connection_fe_link(
            self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink",
        ):
            from mastapy.system_model.fe.links import _2431

            return self._parent._cast(_2431.ShaftHubConnectionFELink)

        @property
        def multi_node_connector_fe_link(
            self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink",
        ) -> "MultiNodeConnectorFELink":
            return self._parent

        def __getattr__(
            self: "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiNodeConnectorFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink":
        return self._Cast_MultiNodeConnectorFELink(self)
