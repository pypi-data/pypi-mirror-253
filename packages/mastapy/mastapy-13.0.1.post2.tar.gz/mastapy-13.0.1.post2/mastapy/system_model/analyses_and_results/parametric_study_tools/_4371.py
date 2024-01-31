"""KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"
)


class KlingelnbergCycloPalloidConicalGearSetParametricStudyTool(
    _4330.ConicalGearSetParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4330.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(
                _4374.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(
                _4377.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetParametricStudyTool(
            self
        )
