"""PinionBevelGeneratingTiltMachineSettings"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_BEVEL_GENERATING_TILT_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionBevelGeneratingTiltMachineSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("PinionBevelGeneratingTiltMachineSettings",)


Self = TypeVar("Self", bound="PinionBevelGeneratingTiltMachineSettings")


class PinionBevelGeneratingTiltMachineSettings(_806.PinionFinishMachineSettings):
    """PinionBevelGeneratingTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_BEVEL_GENERATING_TILT_MACHINE_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PinionBevelGeneratingTiltMachineSettings"
    )

    class _Cast_PinionBevelGeneratingTiltMachineSettings:
        """Special nested class for casting PinionBevelGeneratingTiltMachineSettings to subclasses."""

        def __init__(
            self: "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings",
            parent: "PinionBevelGeneratingTiltMachineSettings",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings",
        ):
            return self._parent._cast(_806.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings",
        ):
            from mastapy.gears import _320

            return self._parent._cast(_320.ConicalGearToothSurface)

        @property
        def pinion_bevel_generating_tilt_machine_settings(
            self: "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings",
        ) -> "PinionBevelGeneratingTiltMachineSettings":
            return self._parent

        def __getattr__(
            self: "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings",
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
        self: Self, instance_to_wrap: "PinionBevelGeneratingTiltMachineSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionBevelGeneratingTiltMachineSettings._Cast_PinionBevelGeneratingTiltMachineSettings":
        return self._Cast_PinionBevelGeneratingTiltMachineSettings(self)
