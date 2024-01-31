"""PlanetBasedFELink"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe.links import _2425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_BASED_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "PlanetBasedFELink"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetBasedFELink",)


Self = TypeVar("Self", bound="PlanetBasedFELink")


class PlanetBasedFELink(_2425.MultiNodeFELink):
    """PlanetBasedFELink

    This is a mastapy class.
    """

    TYPE = _PLANET_BASED_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetBasedFELink")

    class _Cast_PlanetBasedFELink:
        """Special nested class for casting PlanetBasedFELink to subclasses."""

        def __init__(
            self: "PlanetBasedFELink._Cast_PlanetBasedFELink",
            parent: "PlanetBasedFELink",
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(self: "PlanetBasedFELink._Cast_PlanetBasedFELink"):
            return self._parent._cast(_2425.MultiNodeFELink)

        @property
        def fe_link(self: "PlanetBasedFELink._Cast_PlanetBasedFELink"):
            from mastapy.system_model.fe.links import _2418

            return self._parent._cast(_2418.FELink)

        @property
        def gear_with_duplicated_meshes_fe_link(
            self: "PlanetBasedFELink._Cast_PlanetBasedFELink",
        ):
            from mastapy.system_model.fe.links import _2422

            return self._parent._cast(_2422.GearWithDuplicatedMeshesFELink)

        @property
        def planetary_connector_multi_node_fe_link(
            self: "PlanetBasedFELink._Cast_PlanetBasedFELink",
        ):
            from mastapy.system_model.fe.links import _2426

            return self._parent._cast(_2426.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_carrier_fe_link(self: "PlanetBasedFELink._Cast_PlanetBasedFELink"):
            from mastapy.system_model.fe.links import _2428

            return self._parent._cast(_2428.PlanetCarrierFELink)

        @property
        def planet_based_fe_link(
            self: "PlanetBasedFELink._Cast_PlanetBasedFELink",
        ) -> "PlanetBasedFELink":
            return self._parent

        def __getattr__(self: "PlanetBasedFELink._Cast_PlanetBasedFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetBasedFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PlanetBasedFELink._Cast_PlanetBasedFELink":
        return self._Cast_PlanetBasedFELink(self)
