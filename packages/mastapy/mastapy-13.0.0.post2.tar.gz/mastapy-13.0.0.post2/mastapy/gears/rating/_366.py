"""MeshSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _319
    from mastapy.materials.efficiency import _294
    from mastapy.gears.rating import _364


__docformat__ = "restructuredtext en"
__all__ = ("MeshSingleFlankRating",)


Self = TypeVar("Self", bound="MeshSingleFlankRating")


class MeshSingleFlankRating(_0.APIBase):
    """MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshSingleFlankRating")

    class _Cast_MeshSingleFlankRating:
        """Special nested class for casting MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
            parent: "MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _414

            return self._parent._cast(_414.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _418

            return self._parent._cast(
                _418.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _419

            return self._parent._cast(
                _419.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
            )

        @property
        def iso10300_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _422

            return self._parent._cast(_422.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _423

            return self._parent._cast(_423.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _424

            return self._parent._cast(_424.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _425

            return self._parent._cast(_425.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _426

            return self._parent._cast(_426.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.hypoid.standards import _443

            return self._parent._cast(_443.GleasonHypoidMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalMeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _490

            return self._parent._cast(
                _490.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
            )

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _492

            return self._parent._cast(
                _492.PlasticGearVDI2736AbstractMeshSingleFlankRating
            )

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494

            return self._parent._cast(_494.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _512

            return self._parent._cast(_512.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _514

            return self._parent._cast(_514.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _516

            return self._parent._cast(_516.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO6336AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _520

            return self._parent._cast(_520.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.din3990 import _533

            return self._parent._cast(_533.DIN3990MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.agma import _535

            return self._parent._cast(_535.AGMA2101MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _558

            return self._parent._cast(_558.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _560

            return self._parent._cast(_560.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _562

            return self._parent._cast(_562.SpiralBevelMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_calculation_method(
        self: Self,
    ) -> "_319.CoefficientOfFrictionCalculationMethod":
        """mastapy.gears.CoefficientOfFrictionCalculationMethod"""
        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._319", "CoefficientOfFrictionCalculationMethod"
        )(value)

    @coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_calculation_method(
        self: Self, value: "_319.CoefficientOfFrictionCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self: Self) -> "_294.EfficiencyRatingMethod":
        """mastapy.materials.efficiency.EfficiencyRatingMethod"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._294", "EfficiencyRatingMethod"
        )(value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(self: Self, value: "_294.EfficiencyRatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )
        self.wrapped.EfficiencyRatingMethod = value

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
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def gear_single_flank_ratings(self: Self) -> "List[_364.GearSingleFlankRating]":
        """List[mastapy.gears.rating.GearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def cast_to(self: Self) -> "MeshSingleFlankRating._Cast_MeshSingleFlankRating":
        return self._Cast_MeshSingleFlankRating(self)
