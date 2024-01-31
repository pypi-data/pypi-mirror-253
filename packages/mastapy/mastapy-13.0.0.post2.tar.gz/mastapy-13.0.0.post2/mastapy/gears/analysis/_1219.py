"""GearImplementationAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationAnalysis",)


Self = TypeVar("Self", bound="GearImplementationAnalysis")


class GearImplementationAnalysis(_1218.GearDesignAnalysis):
    """GearImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationAnalysis")

    class _Cast_GearImplementationAnalysis:
        """Special nested class for casting GearImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            parent: "GearImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _617

            return self._parent._cast(_617.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _775

            return self._parent._cast(_775.ConicalGearManufacturingAnalysis)

        @property
        def gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca import _840

            return self._parent._cast(_840.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _856

            return self._parent._cast(_856.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca.conical import _867

            return self._parent._cast(_867.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "GearImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationAnalysis._Cast_GearImplementationAnalysis":
        return self._Cast_GearImplementationAnalysis(self)
