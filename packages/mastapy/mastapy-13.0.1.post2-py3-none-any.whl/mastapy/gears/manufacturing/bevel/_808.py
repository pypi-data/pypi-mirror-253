"""PinionHypoidGeneratingTiltMachineSettings"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_HYPOID_GENERATING_TILT_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel",
    "PinionHypoidGeneratingTiltMachineSettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("PinionHypoidGeneratingTiltMachineSettings",)


Self = TypeVar("Self", bound="PinionHypoidGeneratingTiltMachineSettings")


class PinionHypoidGeneratingTiltMachineSettings(_806.PinionFinishMachineSettings):
    """PinionHypoidGeneratingTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_HYPOID_GENERATING_TILT_MACHINE_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PinionHypoidGeneratingTiltMachineSettings"
    )

    class _Cast_PinionHypoidGeneratingTiltMachineSettings:
        """Special nested class for casting PinionHypoidGeneratingTiltMachineSettings to subclasses."""

        def __init__(
            self: "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings",
            parent: "PinionHypoidGeneratingTiltMachineSettings",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings",
        ):
            return self._parent._cast(_806.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings",
        ):
            from mastapy.gears import _320

            return self._parent._cast(_320.ConicalGearToothSurface)

        @property
        def pinion_hypoid_generating_tilt_machine_settings(
            self: "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings",
        ) -> "PinionHypoidGeneratingTiltMachineSettings":
            return self._parent

        def __getattr__(
            self: "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings",
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
        self: Self, instance_to_wrap: "PinionHypoidGeneratingTiltMachineSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings":
        return self._Cast_PinionHypoidGeneratingTiltMachineSettings(self)
