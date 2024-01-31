"""WormMeshLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Worm", "WormMeshLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("WormMeshLoadCase",)


Self = TypeVar("Self", bound="WormMeshLoadCase")


class WormMeshLoadCase(_875.MeshLoadCase):
    """WormMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormMeshLoadCase")

    class _Cast_WormMeshLoadCase:
        """Special nested class for casting WormMeshLoadCase to subclasses."""

        def __init__(
            self: "WormMeshLoadCase._Cast_WormMeshLoadCase", parent: "WormMeshLoadCase"
        ):
            self._parent = parent

        @property
        def mesh_load_case(self: "WormMeshLoadCase._Cast_WormMeshLoadCase"):
            return self._parent._cast(_875.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self: "WormMeshLoadCase._Cast_WormMeshLoadCase"):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "WormMeshLoadCase._Cast_WormMeshLoadCase",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_load_case(
            self: "WormMeshLoadCase._Cast_WormMeshLoadCase",
        ) -> "WormMeshLoadCase":
            return self._parent

        def __getattr__(self: "WormMeshLoadCase._Cast_WormMeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WormMeshLoadCase._Cast_WormMeshLoadCase":
        return self._Cast_WormMeshLoadCase(self)
