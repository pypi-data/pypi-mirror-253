"""GearSetDesignAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetDesignAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignAnalysis",)


Self = TypeVar("Self", bound="GearSetDesignAnalysis")


class GearSetDesignAnalysis(_1217.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesignAnalysis")

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
            parent: "GearSetDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _621

            return self._parent._cast(_621.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca import _846

            return self._parent._cast(_846.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _862

            return self._parent._cast(_862.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case import _874

            return self._parent._cast(_874.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.worm import _877

            return self._parent._cast(_877.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.face import _880

            return self._parent._cast(_880.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _883

            return self._parent._cast(_883.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.conical import _886

            return self._parent._cast(_886.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.concept import _889

            return self._parent._cast(_889.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _893

            return self._parent._cast(_893.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _896

            return self._parent._cast(_896.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _897

            return self._parent._cast(_897.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _996

            return self._parent._cast(_996.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107

            return self._parent._cast(_1107.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model import _1200

            return self._parent._cast(_1200.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1203

            return self._parent._cast(_1203.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1206

            return self._parent._cast(_1206.ConicalSetFEModel)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "GearSetDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis":
        return self._Cast_GearSetDesignAnalysis(self)
