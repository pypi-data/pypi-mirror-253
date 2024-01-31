"""PermanentMagnetRotor"""
from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines import _1292
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ROTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "PermanentMagnetRotor"
)


__docformat__ = "restructuredtext en"
__all__ = ("PermanentMagnetRotor",)


Self = TypeVar("Self", bound="PermanentMagnetRotor")


class PermanentMagnetRotor(_1292.Rotor):
    """PermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ROTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PermanentMagnetRotor")

    class _Cast_PermanentMagnetRotor:
        """Special nested class for casting PermanentMagnetRotor to subclasses."""

        def __init__(
            self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor",
            parent: "PermanentMagnetRotor",
        ):
            self._parent = parent

        @property
        def rotor(self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor"):
            return self._parent._cast(_1292.Rotor)

        @property
        def interior_permanent_magnet_and_synchronous_reluctance_rotor(
            self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor",
        ):
            from mastapy.electric_machines import _1274

            return self._parent._cast(
                _1274.InteriorPermanentMagnetAndSynchronousReluctanceRotor
            )

        @property
        def surface_permanent_magnet_rotor(
            self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor",
        ):
            from mastapy.electric_machines import _1303

            return self._parent._cast(_1303.SurfacePermanentMagnetRotor)

        @property
        def permanent_magnet_rotor(
            self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor",
        ) -> "PermanentMagnetRotor":
            return self._parent

        def __getattr__(
            self: "PermanentMagnetRotor._Cast_PermanentMagnetRotor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PermanentMagnetRotor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PermanentMagnetRotor._Cast_PermanentMagnetRotor":
        return self._Cast_PermanentMagnetRotor(self)
