"""GearLoadCaseBase"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_CASE_BASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase", "GearLoadCaseBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearLoadCaseBase",)


Self = TypeVar("Self", bound="GearLoadCaseBase")


class GearLoadCaseBase(_1218.GearDesignAnalysis):
    """GearLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_CASE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearLoadCaseBase")

    class _Cast_GearLoadCaseBase:
        """Special nested class for casting GearLoadCaseBase to subclasses."""

        def __init__(
            self: "GearLoadCaseBase._Cast_GearLoadCaseBase", parent: "GearLoadCaseBase"
        ):
            self._parent = parent

        @property
        def gear_design_analysis(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def worm_gear_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.worm import _876

            return self._parent._cast(_876.WormGearLoadCase)

        @property
        def face_gear_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.face import _879

            return self._parent._cast(_879.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.cylindrical import _882

            return self._parent._cast(_882.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.conical import _885

            return self._parent._cast(_885.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.concept import _888

            return self._parent._cast(_888.ConceptGearLoadCase)

        @property
        def bevel_load_case(self: "GearLoadCaseBase._Cast_GearLoadCaseBase"):
            from mastapy.gears.load_case.bevel import _891

            return self._parent._cast(_891.BevelLoadCase)

        @property
        def gear_load_case_base(
            self: "GearLoadCaseBase._Cast_GearLoadCaseBase",
        ) -> "GearLoadCaseBase":
            return self._parent

        def __getattr__(self: "GearLoadCaseBase._Cast_GearLoadCaseBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearLoadCaseBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearTemperature

        if temp is None:
            return 0.0

        return temp

    @gear_temperature.setter
    @enforce_parameter_types
    def gear_temperature(self: Self, value: "float"):
        self.wrapped.GearTemperature = float(value) if value is not None else 0.0

    @property
    def rotation_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationSpeed

        if temp is None:
            return 0.0

        return temp

    @rotation_speed.setter
    @enforce_parameter_types
    def rotation_speed(self: Self, value: "float"):
        self.wrapped.RotationSpeed = float(value) if value is not None else 0.0

    @property
    def sump_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SumpTemperature

        if temp is None:
            return 0.0

        return temp

    @sump_temperature.setter
    @enforce_parameter_types
    def sump_temperature(self: Self, value: "float"):
        self.wrapped.SumpTemperature = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GearLoadCaseBase._Cast_GearLoadCaseBase":
        return self._Cast_GearLoadCaseBase(self)
