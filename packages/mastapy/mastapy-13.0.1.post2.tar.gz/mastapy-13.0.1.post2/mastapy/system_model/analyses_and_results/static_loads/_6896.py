"""GearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy.system_model.analyses_and_results.static_loads import _6924, _6953
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7013,
    )
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6891, _6893


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadCase",)


Self = TypeVar("Self", bound="GearSetLoadCase")


class GearSetLoadCase(_6953.SpecialisedAssemblyLoadCase):
    """GearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadCase")

    class _Cast_GearSetLoadCase:
        """Special nested class for casting GearSetLoadCase to subclasses."""

        def __init__(
            self: "GearSetLoadCase._Cast_GearSetLoadCase", parent: "GearSetLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            return self._parent._cast(_6953.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BevelGearSetLoadCase)

        @property
        def concept_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.FaceGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(
                _6921.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def planetary_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.PlanetaryGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelGearSetLoadCase)

        @property
        def worm_gear_set_load_case(self: "GearSetLoadCase._Cast_GearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.ZerolBevelGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "GearSetLoadCase":
            return self._parent

        def __getattr__(self: "GearSetLoadCase._Cast_GearSetLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def gear_mesh_stiffness_model(self: Self) -> "_5438.GearMeshStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel"""
        temp = self.wrapped.GearMeshStiffnessModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5438",
            "GearMeshStiffnessModel",
        )(value)

    @gear_mesh_stiffness_model.setter
    @enforce_parameter_types
    def gear_mesh_stiffness_model(self: Self, value: "_5438.GearMeshStiffnessModel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )
        self.wrapped.GearMeshStiffnessModel = value

    @property
    def mesh_stiffness_source(
        self: Self,
    ) -> "overridable.Overridable_MeshStiffnessSource":
        """Overridable[mastapy.system_model.analyses_and_results.static_loads.MeshStiffnessSource]"""
        temp = self.wrapped.MeshStiffnessSource

        if temp is None:
            return None

        value = overridable.Overridable_MeshStiffnessSource.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @mesh_stiffness_source.setter
    @enforce_parameter_types
    def mesh_stiffness_source(
        self: Self,
        value: "Union[_6924.MeshStiffnessSource, Tuple[_6924.MeshStiffnessSource, bool]]",
    ):
        wrapper_type = overridable.Overridable_MeshStiffnessSource.wrapper_type()
        enclosed_type = overridable.Overridable_MeshStiffnessSource.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.MeshStiffnessSource = value

    @property
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return False

        return temp

    @use_advanced_model_in_advanced_time_stepping_analysis_for_modulation.setter
    @enforce_parameter_types
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self, value: "bool"
    ):
        self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation = (
            bool(value) if value is not None else False
        )

    @property
    def advanced_time_stepping_analysis_for_modulation_options(
        self: Self,
    ) -> "_7013.AdvancedTimeSteppingAnalysisForModulationOptions":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulationOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2532.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6891.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

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
    def gears_without_clones(self: Self) -> "List[_6891.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsWithoutClones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_without_planetary_duplicates(
        self: Self,
    ) -> "List[_6893.GearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesWithoutPlanetaryDuplicates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearSetLoadCase._Cast_GearSetLoadCase":
        return self._Cast_GearSetLoadCase(self)
