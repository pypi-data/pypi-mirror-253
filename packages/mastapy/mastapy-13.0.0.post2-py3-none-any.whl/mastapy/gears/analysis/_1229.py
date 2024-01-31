"""GearSetImplementationAnalysisAbstract"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysisAbstract"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysisAbstract",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysisAbstract")


class GearSetImplementationAnalysisAbstract(_1226.GearSetDesignAnalysis):
    """GearSetImplementationAnalysisAbstract

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetImplementationAnalysisAbstract"
    )

    class _Cast_GearSetImplementationAnalysisAbstract:
        """Special nested class for casting GearSetImplementationAnalysisAbstract to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
            parent: "GearSetImplementationAnalysisAbstract",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            return self._parent._cast(_1226.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.manufacturing.cylindrical import _621

            return self._parent._cast(_621.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.ltca import _846

            return self._parent._cast(_846.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.ltca.cylindrical import _862

            return self._parent._cast(_862.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalGearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ):
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "GearSetImplementationAnalysisAbstract":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
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
        self: Self, instance_to_wrap: "GearSetImplementationAnalysisAbstract.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract":
        return self._Cast_GearSetImplementationAnalysisAbstract(self)
