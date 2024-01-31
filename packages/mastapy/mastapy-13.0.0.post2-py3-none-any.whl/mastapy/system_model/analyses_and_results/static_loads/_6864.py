"""CylindricalGearSetHarmonicLoadData"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetHarmonicLoadData",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetHarmonicLoadData",)


Self = TypeVar("Self", bound="CylindricalGearSetHarmonicLoadData")


class CylindricalGearSetHarmonicLoadData(_6894.GearSetHarmonicLoadData):
    """CylindricalGearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetHarmonicLoadData")

    class _Cast_CylindricalGearSetHarmonicLoadData:
        """Special nested class for casting CylindricalGearSetHarmonicLoadData to subclasses."""

        def __init__(
            self: "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData",
            parent: "CylindricalGearSetHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_load_data(
            self: "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData",
        ):
            return self._parent._cast(_6894.GearSetHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1379

            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def cylindrical_gear_set_harmonic_load_data(
            self: "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData",
        ) -> "CylindricalGearSetHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData",
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
        self: Self, instance_to_wrap: "CylindricalGearSetHarmonicLoadData.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData":
        return self._Cast_CylindricalGearSetHarmonicLoadData(self)
