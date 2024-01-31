"""ZerolBevelGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4461,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.static_loads import _6988
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4442
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4569,
        _4570,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundParametricStudyTool")


class ZerolBevelGearSetCompoundParametricStudyTool(
    _4461.BevelGearSetCompoundParametricStudyTool
):
    """ZerolBevelGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundParametricStudyTool"
    )

    class _Cast_ZerolBevelGearSetCompoundParametricStudyTool:
        """Special nested class for casting ZerolBevelGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
            parent: "ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4461.BevelGearSetCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(
                _4449.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
        ) -> "ZerolBevelGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "ZerolBevelGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6988.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4442.ZerolBevelGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4569.ZerolBevelGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4570.ZerolBevelGearMeshCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearMeshCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4442.ZerolBevelGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetCompoundParametricStudyTool._Cast_ZerolBevelGearSetCompoundParametricStudyTool":
        return self._Cast_ZerolBevelGearSetCompoundParametricStudyTool(self)
