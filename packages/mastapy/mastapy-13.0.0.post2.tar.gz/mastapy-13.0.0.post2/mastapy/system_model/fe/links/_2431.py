"""ShaftHubConnectionFELink"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe.links import _2424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "ShaftHubConnectionFELink"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionFELink",)


Self = TypeVar("Self", bound="ShaftHubConnectionFELink")


class ShaftHubConnectionFELink(_2424.MultiNodeConnectorFELink):
    """ShaftHubConnectionFELink

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionFELink")

    class _Cast_ShaftHubConnectionFELink:
        """Special nested class for casting ShaftHubConnectionFELink to subclasses."""

        def __init__(
            self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink",
            parent: "ShaftHubConnectionFELink",
        ):
            self._parent = parent

        @property
        def multi_node_connector_fe_link(
            self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink",
        ):
            return self._parent._cast(_2424.MultiNodeConnectorFELink)

        @property
        def multi_node_fe_link(
            self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink",
        ):
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.MultiNodeFELink)

        @property
        def fe_link(self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink"):
            from mastapy.system_model.fe.links import _2418

            return self._parent._cast(_2418.FELink)

        @property
        def shaft_hub_connection_fe_link(
            self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink",
        ) -> "ShaftHubConnectionFELink":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHubConnectionFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink":
        return self._Cast_ShaftHubConnectionFELink(self)
