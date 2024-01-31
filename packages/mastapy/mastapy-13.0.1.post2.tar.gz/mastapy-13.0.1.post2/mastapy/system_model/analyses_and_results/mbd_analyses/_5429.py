"""CylindricalPlanetGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5427
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CylindricalPlanetGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearMultibodyDynamicsAnalysis")


class CylindricalPlanetGearMultibodyDynamicsAnalysis(
    _5427.CylindricalGearMultibodyDynamicsAnalysis
):
    """CylindricalPlanetGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalPlanetGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
            parent: "CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5427.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ) -> "CylindricalPlanetGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis(self)
