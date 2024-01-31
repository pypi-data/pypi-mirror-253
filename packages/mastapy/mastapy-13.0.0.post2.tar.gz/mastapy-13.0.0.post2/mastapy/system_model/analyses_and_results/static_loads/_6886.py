"""FaceGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6884, _6885


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetLoadCase",)


Self = TypeVar("Self", bound="FaceGearSetLoadCase")


class FaceGearSetLoadCase(_6895.GearSetLoadCase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetLoadCase")

    class _Cast_FaceGearSetLoadCase:
        """Special nested class for casting FaceGearSetLoadCase to subclasses."""

        def __init__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
            parent: "FaceGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase"):
            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "FaceGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6884.FaceGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_load_case(self: Self) -> "List[_6884.FaceGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_load_case(self: Self) -> "List[_6885.FaceGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase":
        return self._Cast_FaceGearSetLoadCase(self)
