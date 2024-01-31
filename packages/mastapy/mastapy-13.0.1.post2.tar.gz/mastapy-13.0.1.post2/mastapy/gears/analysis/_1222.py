"""GearMeshDesignAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1218, _1226


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDesignAnalysis",)


Self = TypeVar("Self", bound="GearMeshDesignAnalysis")


class GearMeshDesignAnalysis(_1216.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDesignAnalysis")

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
            parent: "GearMeshDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca import _841

            return self._parent._cast(_841.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _857

            return self._parent._cast(_857.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _870

            return self._parent._cast(_870.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis"):
            from mastapy.gears.load_case import _875

            return self._parent._cast(_875.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.worm import _878

            return self._parent._cast(_878.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.face import _881

            return self._parent._cast(_881.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _884

            return self._parent._cast(_884.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.conical import _887

            return self._parent._cast(_887.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.concept import _890

            return self._parent._cast(_890.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _892

            return self._parent._cast(_892.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _894

            return self._parent._cast(_894.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _895

            return self._parent._cast(_895.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _992

            return self._parent._cast(_992.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098

            return self._parent._cast(_1098.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model import _1198

            return self._parent._cast(_1198.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1202

            return self._parent._cast(_1202.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1205

            return self._parent._cast(_1205.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "GearMeshDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self: Self) -> "_1218.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1218.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: Self) -> "_1226.GearSetDesignAnalysis":
        """mastapy.gears.analysis.GearSetDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis":
        return self._Cast_GearMeshDesignAnalysis(self)
