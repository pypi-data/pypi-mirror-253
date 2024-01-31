"""CylindricalGearSetLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearSetLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _464
    from mastapy.gears.gear_two_d_fe_analysis import _896
    from mastapy.gears.ltca.cylindrical import _857


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetLoadDistributionAnalysis")


class CylindricalGearSetLoadDistributionAnalysis(_846.GearSetLoadDistributionAnalysis):
    """CylindricalGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetLoadDistributionAnalysis"
    )

    class _Cast_CylindricalGearSetLoadDistributionAnalysis:
        """Special nested class for casting CylindricalGearSetLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
            parent: "CylindricalGearSetLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_load_distribution_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            return self._parent._cast(_846.GearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _862

            return self._parent._cast(_862.FaceGearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
        ) -> "CylindricalGearSetLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_464.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tiff_analysis(self: Self) -> "_896.CylindricalGearSetTIFFAnalysis":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearSetTIFFAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshes(self: Self) -> "List[_857.CylindricalGearMeshLoadDistributionAnalysis]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetLoadDistributionAnalysis._Cast_CylindricalGearSetLoadDistributionAnalysis":
        return self._Cast_CylindricalGearSetLoadDistributionAnalysis(self)
