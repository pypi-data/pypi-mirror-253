"""ElectricMachineHarmonicLoadDataFromExcel"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_EXCEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromExcel",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromExcel",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromExcel")


class ElectricMachineHarmonicLoadDataFromExcel(_6871.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromExcel

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_EXCEL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromExcel"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromExcel:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromExcel to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
            parent: "ElectricMachineHarmonicLoadDataFromExcel",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
        ):
            return self._parent._cast(_6871.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1377

            return self._parent._cast(_1377.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1382

            return self._parent._cast(_1382.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
        ):
            from mastapy.electric_machines.harmonic_load_data import _1379

            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
        ) -> "ElectricMachineHarmonicLoadDataFromExcel":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataFromExcel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel":
        return self._Cast_ElectricMachineHarmonicLoadDataFromExcel(self)
