"""GearDesignAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearDesignAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignAnalysis",)


Self = TypeVar("Self", bound="GearDesignAnalysis")


class GearDesignAnalysis(_1215.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignAnalysis")

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
            parent: "GearDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _612

            return self._parent._cast(_612.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _616

            return self._parent._cast(_616.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _617

            return self._parent._cast(_617.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _775

            return self._parent._cast(_775.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _777

            return self._parent._cast(_777.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca import _840

            return self._parent._cast(_840.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _856

            return self._parent._cast(_856.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _867

            return self._parent._cast(_867.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case import _873

            return self._parent._cast(_873.GearLoadCaseBase)

        @property
        def worm_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.worm import _876

            return self._parent._cast(_876.WormGearLoadCase)

        @property
        def face_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.face import _879

            return self._parent._cast(_879.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _882

            return self._parent._cast(_882.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.conical import _885

            return self._parent._cast(_885.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.concept import _888

            return self._parent._cast(_888.ConceptGearLoadCase)

        @property
        def bevel_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.bevel import _891

            return self._parent._cast(_891.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _898

            return self._parent._cast(_898.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _899

            return self._parent._cast(_899.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _993

            return self._parent._cast(_993.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100

            return self._parent._cast(_1100.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101

            return self._parent._cast(_1101.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104

            return self._parent._cast(_1104.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.fe_model import _1197

            return self._parent._cast(_1197.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1201

            return self._parent._cast(_1201.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.fe_model.conical import _1204

            return self._parent._cast(_1204.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1219

            return self._parent._cast(_1219.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1220

            return self._parent._cast(_1220.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "GearDesignAnalysis":
            return self._parent

        def __getattr__(self: "GearDesignAnalysis._Cast_GearDesignAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearDesignAnalysis._Cast_GearDesignAnalysis":
        return self._Cast_GearDesignAnalysis(self)
