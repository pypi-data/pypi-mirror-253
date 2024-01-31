"""CycloidalDiscMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CycloidalDiscMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6859


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscMultibodyDynamicsAnalysis")


class CycloidalDiscMultibodyDynamicsAnalysis(
    _5376.AbstractShaftMultibodyDynamicsAnalysis
):
    """CycloidalDiscMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscMultibodyDynamicsAnalysis"
    )

    class _Cast_CycloidalDiscMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5376.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(
                _5377.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def component_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscMultibodyDynamicsAnalysis(self)
