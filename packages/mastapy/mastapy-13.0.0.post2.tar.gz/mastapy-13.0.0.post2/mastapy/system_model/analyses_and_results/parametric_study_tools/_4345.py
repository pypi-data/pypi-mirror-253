"""CylindricalPlanetGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalPlanetGearParametricStudyTool")


class CylindricalPlanetGearParametricStudyTool(
    _4343.CylindricalGearParametricStudyTool
):
    """CylindricalPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearParametricStudyTool"
    )

    class _Cast_CylindricalPlanetGearParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
            parent: "CylindricalPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            return self._parent._cast(_4343.CylindricalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "CylindricalPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool":
        return self._Cast_CylindricalPlanetGearParametricStudyTool(self)
