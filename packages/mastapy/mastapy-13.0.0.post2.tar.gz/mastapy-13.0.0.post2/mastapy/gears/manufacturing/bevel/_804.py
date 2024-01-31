"""PinionConicalMachineSettingsSpecified"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_CONICAL_MACHINE_SETTINGS_SPECIFIED = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionConicalMachineSettingsSpecified"
)


__docformat__ = "restructuredtext en"
__all__ = ("PinionConicalMachineSettingsSpecified",)


Self = TypeVar("Self", bound="PinionConicalMachineSettingsSpecified")


class PinionConicalMachineSettingsSpecified(_806.PinionFinishMachineSettings):
    """PinionConicalMachineSettingsSpecified

    This is a mastapy class.
    """

    TYPE = _PINION_CONICAL_MACHINE_SETTINGS_SPECIFIED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PinionConicalMachineSettingsSpecified"
    )

    class _Cast_PinionConicalMachineSettingsSpecified:
        """Special nested class for casting PinionConicalMachineSettingsSpecified to subclasses."""

        def __init__(
            self: "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified",
            parent: "PinionConicalMachineSettingsSpecified",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified",
        ):
            return self._parent._cast(_806.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified",
        ):
            from mastapy.gears import _320

            return self._parent._cast(_320.ConicalGearToothSurface)

        @property
        def pinion_conical_machine_settings_specified(
            self: "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified",
        ) -> "PinionConicalMachineSettingsSpecified":
            return self._parent

        def __getattr__(
            self: "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified",
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
        self: Self, instance_to_wrap: "PinionConicalMachineSettingsSpecified.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified":
        return self._Cast_PinionConicalMachineSettingsSpecified(self)
