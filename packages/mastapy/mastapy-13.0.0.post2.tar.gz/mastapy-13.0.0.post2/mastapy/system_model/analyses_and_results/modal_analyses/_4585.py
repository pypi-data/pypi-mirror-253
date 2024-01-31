"""BevelDifferentialPlanetGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelDifferentialPlanetGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.system_deflections import _2704


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearModalAnalysis")


class BevelDifferentialPlanetGearModalAnalysis(
    _4583.BevelDifferentialGearModalAnalysis
):
    """BevelDifferentialPlanetGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearModalAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearModalAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
            parent: "BevelDifferentialPlanetGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            return self._parent._cast(_4583.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
        ) -> "BevelDifferentialPlanetGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2704.BevelDifferentialPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearModalAnalysis._Cast_BevelDifferentialPlanetGearModalAnalysis":
        return self._Cast_BevelDifferentialPlanetGearModalAnalysis(self)
