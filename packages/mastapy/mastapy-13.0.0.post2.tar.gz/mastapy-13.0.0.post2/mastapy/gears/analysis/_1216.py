"""AbstractGearMeshAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearMeshAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1215


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshAnalysis",)


Self = TypeVar("Self", bound="AbstractGearMeshAnalysis")


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshAnalysis")

    class _Cast_AbstractGearMeshAnalysis:
        """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
            parent: "AbstractGearMeshAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.worm import _373

            return self._parent._cast(_373.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.worm import _377

            return self._parent._cast(_377.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(
                _411.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.face import _446

            return self._parent._cast(_446.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.face import _447

            return self._parent._cast(_447.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _466

            return self._parent._cast(_466.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.conical import _539

            return self._parent._cast(_539.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.conical import _544

            return self._parent._cast(_544.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.concept import _549

            return self._parent._cast(_549.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.concept import _550

            return self._parent._cast(_550.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearMeshRating)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca import _841

            return self._parent._cast(_841.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _857

            return self._parent._cast(_857.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca.conical import _870

            return self._parent._cast(_870.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case import _875

            return self._parent._cast(_875.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.worm import _878

            return self._parent._cast(_878.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.face import _881

            return self._parent._cast(_881.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _884

            return self._parent._cast(_884.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.conical import _887

            return self._parent._cast(_887.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.concept import _890

            return self._parent._cast(_890.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _892

            return self._parent._cast(_892.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _894

            return self._parent._cast(_894.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _895

            return self._parent._cast(_895.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _992

            return self._parent._cast(_992.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098

            return self._parent._cast(_1098.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model import _1198

            return self._parent._cast(_1198.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1202

            return self._parent._cast(_1202.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1205

            return self._parent._cast(_1205.ConicalMeshFEModel)

        @property
        def gear_mesh_design_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.GearMeshImplementationDetail)

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "AbstractGearMeshAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshName

        if temp is None:
            return ""

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def gear_a(self: Self) -> "_1215.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1215.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis":
        return self._Cast_AbstractGearMeshAnalysis(self)
