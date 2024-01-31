"""SynchroniserPart"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.couplings import _2584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPart",)


Self = TypeVar("Self", bound="SynchroniserPart")


class SynchroniserPart(_2584.CouplingHalf):
    """SynchroniserPart

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPart")

    class _Cast_SynchroniserPart:
        """Special nested class for casting SynchroniserPart to subclasses."""

        def __init__(
            self: "SynchroniserPart._Cast_SynchroniserPart", parent: "SynchroniserPart"
        ):
            self._parent = parent

        @property
        def coupling_half(self: "SynchroniserPart._Cast_SynchroniserPart"):
            return self._parent._cast(_2584.CouplingHalf)

        @property
        def mountable_component(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def synchroniser_half(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserHalf)

        @property
        def synchroniser_sleeve(self: "SynchroniserPart._Cast_SynchroniserPart"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserSleeve)

        @property
        def synchroniser_part(
            self: "SynchroniserPart._Cast_SynchroniserPart",
        ) -> "SynchroniserPart":
            return self._parent

        def __getattr__(self: "SynchroniserPart._Cast_SynchroniserPart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SynchroniserPart._Cast_SynchroniserPart":
        return self._Cast_SynchroniserPart(self)
