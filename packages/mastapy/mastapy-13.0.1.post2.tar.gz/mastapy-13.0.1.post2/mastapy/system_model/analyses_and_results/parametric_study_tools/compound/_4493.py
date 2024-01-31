"""CylindricalPlanetGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4490,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CylindricalPlanetGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6867
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundParametricStudyTool")


class CylindricalPlanetGearCompoundParametricStudyTool(
    _4490.CylindricalGearCompoundParametricStudyTool
):
    """CylindricalPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundParametricStudyTool"
    )

    class _Cast_CylindricalPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
            parent: "CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4490.CylindricalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ) -> "CylindricalPlanetGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6867.CylindricalPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase

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
    ) -> "List[_4346.CylindricalPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4346.CylindricalPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool]

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
    ) -> "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool":
        return self._Cast_CylindricalPlanetGearCompoundParametricStudyTool(self)
