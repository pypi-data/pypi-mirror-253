"""StraightBevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6962, _6963


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetLoadCase",)


Self = TypeVar("Self", bound="StraightBevelGearSetLoadCase")


class StraightBevelGearSetLoadCase(_6829.BevelGearSetLoadCase):
    """StraightBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSetLoadCase")

    class _Cast_StraightBevelGearSetLoadCase:
        """Special nested class for casting StraightBevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
            parent: "StraightBevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            return self._parent._cast(_6829.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_load_case(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
        ) -> "StraightBevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2548.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6962.StraightBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase]

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
    def straight_bevel_gears_load_case(
        self: Self,
    ) -> "List[_6962.StraightBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_load_case(
        self: Self,
    ) -> "List[_6963.StraightBevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetLoadCase._Cast_StraightBevelGearSetLoadCase":
        return self._Cast_StraightBevelGearSetLoadCase(self)
