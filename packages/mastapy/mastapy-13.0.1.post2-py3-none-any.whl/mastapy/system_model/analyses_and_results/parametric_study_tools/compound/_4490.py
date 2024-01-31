"""CylindricalGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4501,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CylindricalGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalGearCompoundParametricStudyTool")


class CylindricalGearCompoundParametricStudyTool(_4501.GearCompoundParametricStudyTool):
    """CylindricalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundParametricStudyTool"
    )

    class _Cast_CylindricalGearCompoundParametricStudyTool:
        """Special nested class for casting CylindricalGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
            parent: "CylindricalGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(
                _4493.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
        ) -> "CylindricalGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6862.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4344.CylindricalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4344.CylindricalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCompoundParametricStudyTool._Cast_CylindricalGearCompoundParametricStudyTool":
        return self._Cast_CylindricalGearCompoundParametricStudyTool(self)
